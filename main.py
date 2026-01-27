from auth import login
import sys
import VecinoRegistro
import GestionDeHerramienta
import prestamos
import consultas
while True:
    usuario = login()
    if usuario is None:
        print("Debe iniciar Sesion Para Continuar ")
        continue
    if usuario["tipo"] not in ("Administrador", "Residente"):
        print("Usuario Invalido")
        continue 

    while True:
        try:
            print("\n======-MENÚ-======")
            print (f" Bienvenido: {usuario['tipo']} ")
            print("1. Gestion De Vecinos")
            print("2. Gestion De Herramientas")
            print("3. Gestion De Préstamos")
            print("4. Consultas Y Reportes")
            print("5. Salir")

            op = input("Ingrese Una Opción: ")

            if op == "1":
                VecinoRegistro.menu_usuario(usuario)

            elif op == "2":
                GestionDeHerramienta.menu_herramienta(usuario)

            elif op == "3":
                prestamos.menu_prestamos(usuario)

            elif op == "4":
                consultas.menu_consultas()

            elif op == "5":
                print("Saliendo Del Programa Forzosamente.....")
                sys.exit()
                break

            else:
                print("Opción inválida.")
        except ValueError:
            print("Solo Numeros ")
        except KeyboardInterrupt:
            print ("Error")
        except Exception as e:
            print("Error Inesperado ",e)