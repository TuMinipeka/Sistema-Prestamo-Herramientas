from logs import registrar_log
import json
import os
from datetime import datetime

ARCHIVO_PRESTAMOS = "prestamos.json"
ARCHIVO_HERRAMIENTAS = "herramientas.json"
ARCHIVO_USUARIOS = "vecino.json"

def crear_prestamo(usuario_actual):
    if usuario_actual["tipo"] != "Administrador":
        print(" Solo el administrador puede registrar préstamos.")
        return

    print("\n=== REGISTRAR PRÉSTAMO ===")

    id_prestamo = input("ID del préstamo: ")
    usuario_id = input("ID del vecino: ")
    herramienta_id = input("ID de la herramienta: ")

    try:
        cantidad = int(input("Cantidad a prestar: "))
        if cantidad <= 0:
            print("Cantidad inválida.")
            return
    except ValueError:
        print("Cantidad debe ser numérica.")
        return

    fecha_inicio = datetime.now().strftime("%Y-%m-%d")
    fecha_devolucion = input("Fecha estimada devolución (YYYY-MM-DD): ")
    observaciones = input("Observaciones: ")
    registrar_log(
    "INFO",
    f"Préstamo {id_prestamo} creado para usuario {usuario_id}"
)

    # Cargar archivos
    prestamos = {}
    if os.path.exists(ARCHIVO_PRESTAMOS):
        with open(ARCHIVO_PRESTAMOS, "r", encoding="utf-8") as f:
            prestamos = json.load(f)

    with open(ARCHIVO_USUARIOS, "r", encoding="utf-8") as f:
        usuarios = json.load(f)

    with open(ARCHIVO_HERRAMIENTAS, "r", encoding="utf-8") as f:
        herramientas = json.load(f)

    # Validaciones
    if usuario_id not in usuarios:
        print("Vecino no existe.")
        return

    if herramienta_id not in herramientas:
        print("Herramienta no existe.")
        return

    herramienta = herramientas[herramienta_id]

    if herramienta["estado"] != "Activa":
        print("La herramienta no está activa.")
        return

    if herramienta["cantidad"] < cantidad:
        print("No hay stock suficiente.")
        return

    # Registrar préstamo
    prestamos[id_prestamo] = {
        "usuario_id": usuario_id,
        "herramienta_id": herramienta_id,
        "cantidad": cantidad,
        "fecha_inicio": fecha_inicio,
        "fecha_devolucion": fecha_devolucion,
        "estado": "Activo",
        "observaciones": observaciones
    }

    herramienta["cantidad"] -= cantidad

    # Guardar cambios
    with open(ARCHIVO_PRESTAMOS, "w", encoding="utf-8") as f:
        json.dump(prestamos, f, indent=4, ensure_ascii=False)

    with open(ARCHIVO_HERRAMIENTAS, "w", encoding="utf-8") as f:
        json.dump(herramientas, f, indent=4, ensure_ascii=False)

    print(" Préstamo registrado correctamente.")

def devolver_prestamo(usuario_actual):
    if usuario_actual["tipo"] != "Administrador":
        print(" Solo el administrador puede registrar devoluciones.")
        return

    id_prestamo = input("ID del préstamo a devolver: ")

    with open(ARCHIVO_PRESTAMOS, "r", encoding="utf-8") as f:
        prestamos = json.load(f)

    if id_prestamo not in prestamos:
        print("Préstamo no encontrado.")
        return

    prestamo = prestamos[id_prestamo]

    if prestamo["estado"] != "Activo":
        print("Este préstamo ya fue cerrado.")
        return

    with open(ARCHIVO_HERRAMIENTAS, "r", encoding="utf-8") as f:
        herramientas = json.load(f)

    herramientas[prestamo["herramienta_id"]]["cantidad"] += prestamo["cantidad"]
    prestamo["estado"] = "Devuelto"

    with open(ARCHIVO_PRESTAMOS, "w", encoding="utf-8") as f:
        json.dump(prestamos, f, indent=4, ensure_ascii=False)

    with open(ARCHIVO_HERRAMIENTAS, "w", encoding="utf-8") as f:
        json.dump(herramientas, f, indent=4, ensure_ascii=False)

    print(" Préstamo devuelto correctamente.")
    registrar_log(
    "INFO",
    f"Préstamo {id_prestamo} devuelto"
    )

def listar_prestamos():
    print("\n=== LISTA DE PRÉSTAMOS ===")

    try:
        with open(ARCHIVO_PRESTAMOS, "r", encoding="utf-8") as f:
            prestamos = json.load(f)

        for id_p, p in prestamos.items():
            print("----------------------------")
            print(f"ID: {id_p}")
            print(f"Usuario: {p['usuario_id']}")
            print(f"Herramienta: {p['herramienta_id']}")
            print(f"Cantidad: {p['cantidad']}")
            print(f"Inicio: {p['fecha_inicio']}")
            print(f"Devolución: {p['fecha_devolucion']}")
            print(f"Estado: {p['estado']}")
            print(f"Obs: {p['observaciones']}")

    except FileNotFoundError:
        print("No hay préstamos registrados.")

def menu_prestamos(usuario_actual):
    while True:
        print("\n===== MENÚ PRÉSTAMOS =====")
        print("1. Crear préstamo")
        print("2. Devolver préstamo")
        print("3. Listar préstamos")
        print("4. Volver")

        try:
            op = int(input("Seleccione: "))

            if op == 1:
                crear_prestamo(usuario_actual)
            elif op == 2:
                devolver_prestamo(usuario_actual)
            elif op == 3:
                listar_prestamos()
            elif op == 4:
                break
            else:
                print("Opción inválida.")

        except ValueError:
            print("Debe ingresar un número.")

