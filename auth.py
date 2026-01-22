from logs import registrar_log
ADMIN_PASSWORD = "0000"

def login():
    print("\n=== INICIO DE SESIÓN ===")
    print("1. Administrador")
    print("2. Residente")

    try:
        opcion = int(input("Seleccione una opción: "))
        if opcion == 1:
            if verificar_admin():
                return {"tipo": "Administrador"}
            else:
                return None
        elif opcion == 2:
            return {"tipo": "Residente"}
        else:
            print("Opción inválida")
            return None
    except ValueError:
        print("Debe ingresar un número.")
        return None


def verificar_admin():
    intentos = 3
    while intentos > 0:
        password = input("Ingrese la contraseña: ")
        if password == ADMIN_PASSWORD:
            registrar_log("INFO", "Inicio de sesión como Administrador")
            return True
        intentos -= 1
        registrar_log("WARNING", "Contraseña incorrecta de administrador")
    registrar_log("ERROR", "Acceso administrador bloqueado")
    return False
