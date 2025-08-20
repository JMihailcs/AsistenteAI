from voz import escuchar_comando
from nlp import interpretar_comando
from acciones import ejecutar_comando

if __name__ == "__main__":
    while True:
        comando = escuchar_comando()
        if comando:
            resultado = interpretar_comando(comando)
            print(resultado)
            accion = resultado["accion"]
            programa = resultado["aplicacion"]
            parametro = resultado["parametro"]

            print(f"🤖 Acción: {accion}, Aplicacion: {programa}, Parámetro: {parametro}")
            ejecutar_comando(accion, programa, parametro)
