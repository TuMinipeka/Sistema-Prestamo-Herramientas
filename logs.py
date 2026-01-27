from datetime import datetime

ARCHIVO_LOGS = "logs.txt"

def registrar_log(nivel, mensaje):
    """
    nivel: INFO | WARNING | ERROR 
    mensaje: texto descriptivo del evento
    """
    fecha = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    linea = f"{fecha} | {nivel} | {mensaje}\n"

    with open(ARCHIVO_LOGS, "a", encoding="utf-8") as f:
        f.write(linea)
