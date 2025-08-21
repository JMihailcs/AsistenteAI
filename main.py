from voz import escuchar_comando, hablar
from nlp import interpretar_comando
from acciones import ejecutar_comando

if __name__ == "__main__":
    while True:
        # Paso 1: esperar a escuchar "mila"
        comando = escuchar_comando()
        if not comando:
            continue

        comando = comando.strip().lower()

        if "mila" in comando:
            hablar("Sí que desea?")
            
            # Paso 2: ahora espera el siguiente comando real
            comando_real = escuchar_comando()
            if not comando_real:
                continue

            comando_real = comando_real.strip().lower()

            resultado = interpretar_comando(comando_real)
            print(resultado)

            accion = resultado["accion"]
            programa = resultado["aplicacion"]
            parametro = resultado["parametro"]

            print(f"🤖 Acción: {accion}, Aplicación: {programa}, Parámetro: {parametro}")
            ejecutar_comando(accion, programa, parametro)
        else:
            print("🔇 Esperando que digas 'Mila'...")
