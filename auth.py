from logs import registrar_log

ADMIN_PASSWORD = "0000"


def login():
    print("\n=== INICIO DE SESIÓN ===")
    print("1. Administrador")
    print("2. Residente")

    try:
        opcion = int(input("Ingrese una opción: "))

        if opcion == 1:
            if verificar_admin():
                registrar_log("INFO", "Inicio de sesión como Administrador")
                return {"tipo": "Administrador"}
            else:
                print("Acceso administrador fallido.")
                return None

        elif opcion == 2:
            registrar_log("INFO", "Inicio de sesión como Residente")
            return {"tipo": "Residente"}
    except KeyboardInterrupt:
        print("Interrumpido")
    except ValueError:
        print("Debe ingresar un número")
        return None
    except Exception as e:
        print("Error Inesperado ", e)
        return None


def verificar_admin():
    intentos = 3

    while intentos > 0:
        password = input("Ingrese la contraseña de administrador: ")

        if password == ADMIN_PASSWORD:
            return True

        intentos -= 1
        registrar_log("WARNING", "Contraseña incorrecta de administrador")
        print(f"Contraseña incorrecta. Intentos restantes: {intentos}")

    registrar_log("ERROR", "Acceso administrador bloqueado")
    return False
