import json
from datetime import datetime

ARCHIVO_HERRAMIENTAS = "herramientas.json"
ARCHIVO_PRESTAMOS = "prestamos.json"
ARCHIVO_USUARIOS = "vecino.json"

def herramientas_stock_bajo(limite=3):
    print("\n=== HERRAMIENTAS CON STOCK BAJO ===")

    try:
        with open(ARCHIVO_HERRAMIENTAS, "r", encoding="utf-8") as f:
            herramientas = json.load(f)

        encontrado = False
        for id_h, h in herramientas.items():
            if h["cantidad"] < limite:
                encontrado = True
                print("----------------------------")
                print(f"ID: {id_h}")
                print(f"Nombre: {h['nombre']}")
                print(f"Cantidad: {h['cantidad']}")
                print(f"Estado: {h['estado']}")

        if not encontrado:
            print("No hay herramientas con stock bajo.")

    except FileNotFoundError:
        print("No hay herramientas registradas.")

def prestamos_activos_y_vencidos():
    print("\n=== PRÉSTAMOS ACTIVOS Y VENCIDOS ===")

    hoy = datetime.now().date()

    try:
        with open(ARCHIVO_PRESTAMOS, "r", encoding="utf-8") as f:
            prestamos = json.load(f)

        for id_p, p in prestamos.items():
            fecha_dev = datetime.strptime(p["fecha_devolucion"], "%Y-%m-%d").date()

            estado_real = p["estado"]
            if p["estado"] == "Activo" and fecha_dev < hoy:
                estado_real = "Vencido"

            print("----------------------------")
            print(f"ID Préstamo: {id_p}")
            print(f"Usuario: {p['usuario_id']}")
            print(f"Herramienta: {p['herramienta_id']}")
            print(f"Devolución: {p['fecha_devolucion']}")
            print(f"Estado: {estado_real}")

    except FileNotFoundError:
        print("No hay préstamos registrados.")

def historial_usuario():
    usuario_id = input("Ingrese el ID del vecino: ")

    print("\n=== HISTORIAL DE PRÉSTAMOS ===")

    try:
        with open(ARCHIVO_PRESTAMOS, "r", encoding="utf-8") as f:
            prestamos = json.load(f)

        encontrado = False
        for id_p, p in prestamos.items():
            if p["usuario_id"] == usuario_id:
                encontrado = True
                print("----------------------------")
                print(f"Préstamo: {id_p}")
                print(f"Herramienta: {p['herramienta_id']}")
                print(f"Cantidad: {p['cantidad']}")
                print(f"Estado: {p['estado']}")
                print(f"Inicio: {p['fecha_inicio']}")
                print(f"Devolución: {p['fecha_devolucion']}")

        if not encontrado:
            print("Este usuario no tiene préstamos registrados.")

    except FileNotFoundError:
        print("No hay préstamos registrados.")

def herramientas_mas_solicitadas():
    print("\n=== HERRAMIENTAS MÁS SOLICITADAS ===")

    try:
        with open(ARCHIVO_PRESTAMOS, "r", encoding="utf-8") as f:
            prestamos = json.load(f)

        conteo = {}
        for p in prestamos.values():
            h_id = p["herramienta_id"]
            conteo[h_id] = conteo.get(h_id, 0) + p["cantidad"]

        for h_id, total in sorted(conteo.items(), key=lambda x: x[1], reverse=True):
            print(f"Herramienta {h_id}: {total} préstamos")

    except FileNotFoundError:
        print("No hay préstamos registrados.")

def usuarios_mas_activos():
    print("\n=== USUARIOS MÁS ACTIVOS ===")

    try:
        with open(ARCHIVO_PRESTAMOS, "r", encoding="utf-8") as f:
            prestamos = json.load(f)

        conteo = {}
        for p in prestamos.values():
            u_id = p["usuario_id"]
            conteo[u_id] = conteo.get(u_id, 0) + p["cantidad"]

        for u_id, total in sorted(conteo.items(), key=lambda x: x[1], reverse=True):
            print(f"Usuario {u_id}: {total} herramientas solicitadas")

    except FileNotFoundError:
        print("No hay préstamos registrados.")

def menu_consultas():
    while True:
        print("\n===== MENÚ CONSULTAS =====")
        print("1. Herramientas con stock bajo")
        print("2. Préstamos activos y vencidos")
        print("3. Historial de préstamos de un usuario")
        print("4. Herramientas más solicitadas")
        print("5. Usuarios más activos")
        print("6. Volver")

        try:
            op = int(input("Seleccione una opción: "))

            if op == 1:
                herramientas_stock_bajo()
            elif op == 2:
                prestamos_activos_y_vencidos()
            elif op == 3:
                historial_usuario()
            elif op == 4:
                herramientas_mas_solicitadas()
            elif op == 5:
                usuarios_mas_activos()
            elif op == 6:
                break
            else:
                print("Opción inválida.")

        except ValueError:
            print("Debe ingresar un número.")
