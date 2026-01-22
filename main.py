from auth import login
import VecinoRegistro
import GestionDeHerramienta
import prestamos
import consultas
usuario = login()
if not usuario:
    exit()

while True:
    print("\n=== MENÚ ===")
    print("1 Usuarios")
    print("2 Herramientas")
    print("3 Préstamos")
    print("4 Consultas")
    print("5 Salir")

    op = input("> ")

    if op == "1":
        VecinoRegistro.menu_usuario(usuario)

    elif op == "2":
        GestionDeHerramienta.menu_herramienta(usuario)

    elif op == "3":
        prestamos.menu_prestamos(usuario)

    elif op == "4":
        consultas.menu_consultas()

    elif op == "5":
        break

    else:
        print("Opción inválida.")
