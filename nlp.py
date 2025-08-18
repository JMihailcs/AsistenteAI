import json
import ollama

def interpretar_comando(texto: str) -> dict:
    """
    Usa Llama3 para interpretar un comando y devolverlo como JSON estructurado.
    El modelo debe responder SOLO con JSON válido.
    """

    system_prompt = """Eres un intérprete de comandos.
    Convierte la entrada del usuario en un objeto JSON válido con este formato:
    {
        "accion": "ejecutar" | "abrir" | "buscar" | "desconocido",
        "aplicacion": "nombre de la aplicación",
        "parametro": "texto o URL a buscar o abrir (puede estar vacío si no aplica)"
    }
    Reglas:
    - Responde SOLO con JSON válido, sin texto adicional.
    - Siempre intenta separar:
    • "accion" = tipo de operación solicitada.
    • "aplicacion" = programa, servicio o sitio.
    • "parametro" = el contenido concreto a buscar, abrir o usar.
    - Si el usuario pide "abrir google y buscar futbol":
    {
        "accion": "buscar",
        "aplicacion": "google",
        "parametro": "futbol"
    }
    - Si el usuario pide "entra a youtube y busca musicas en portugues":
    {
        "accion": "buscar",
        "aplicacion": "youtube",
        "parametro": "musicas en portugues"
    }
    - Si el usuario pide "ejecuta calculadora":
    {
        "accion": "ejecutar",
        "aplicacion": "calculadora",
        "parametro": ""
    }
    - Si no entiendes, usa "desconocido" y deja "aplicacion" y "parametro" en vacío.
    """


    user_prompt = f"Entrada: {texto}"

    respuesta = ollama.chat(
        model="gemma3:1b",  # usa la versión ligera
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ],
    )

    contenido = respuesta["message"]["content"].strip()

    # Intentar limpiar si viene rodeado de texto accidental
    if contenido.startswith("```"):
        contenido = contenido.strip("`").strip()
        # A veces viene con "json" en la primera línea
        if contenido.lower().startswith("json"):
            contenido = "\n".join(contenido.splitlines()[1:])

    try:
        return json.loads(contenido)
    except json.JSONDecodeError:
        return {"accion": "desconocido", "parametro": ""}

