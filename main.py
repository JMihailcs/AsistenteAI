from voz import escuchar_comando
from nlp import interpretar_comando
from acciones import ejecutar_comando

if __name__ == "__main__":
    while True:
        comando = escuchar_comando()
        if comando:
            resultado = interpretar_comando(comando)
            accion = resultado["accion"]
            parametro = resultado["parametro"]

            print(f"🤖 Acción: {accion}, Parámetro: {parametro}")
            ejecutar_comando(accion, parametro)
