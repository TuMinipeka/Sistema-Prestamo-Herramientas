from logs import registrar_log
import json
import os
def crear_herramienta():
    print("\n===-Registrar Herramienta-===")
    id_herramienta = input("ID De La Herramienta: ")
    nombre = input("Nombre: ").capitalize()
    categoria = input("Categoría: ")
    try:
        cantidad = int(input("Cantidad disponible: "))
        if cantidad < 0:
            print("La cantidad no puede ser negativa.")
            return

        valor = float(input("Valor estimado: "))
        if valor < 0:
            print("El valor no puede ser negativo.")
            return
    except ValueError:
        print("Cantidad y valor deben ser numéricos.")
        return
    
    print("Estado:")
    print("1. Activa")
    print("2. En reparación")
    print("3. Fuera de servicio")

    estado_op = input("Seleccione estado: ")
    try:
        if estado_op == "1":
            estado = "Activa"
        elif estado_op == "2":
            estado = "En reparación"
        elif estado_op == "3":
            estado = "Fuera de servicio"
        else:
            print("Estado inválido.")
            return
    except KeyboardInterrupt:
        print("Error")
    except ValueError:
        print("Ingrese Solo Numeros")
    except Exception as e:
        print("Error Inesperado, ",e)
    try:
        datos = {}
        if os.path.exists("herramientas.json"):
            with open("herramientas.json", "r", encoding="utf-8") as f:
                datos = json.load(f)

        if id_herramienta in datos:
            print(" Esta herramienta ya existe.")
            return

        datos[id_herramienta] = {
            "nombre": nombre,
            "categoria": categoria,
            "cantidad": cantidad,
            "estado": estado,
            "valor": valor
        }

        with open("herramientas.json", "w", encoding="utf-8") as ark:
            json.dump(datos, ark, indent=4, ensure_ascii=False)

        print(" Herramienta registrada correctamente.")

    except Exception as e:
        print(f"Error al registrar herramienta: {e}")

    registrar_log("INFO", f"Herramienta {id_herramienta} creada")

def listar_herramienta():
    print("=====/Listas De Herramientas---------")
    try:
        with open("herramientas.json", "r", encoding="utf-8") as ark:
            datos=json.load(ark)

        for id_h , h in datos.items():
            print ("---------------------------------")
            print(f"ID: {id_h}")
            print(f"Nombre: {h['nombre']}")
            print(f"Categoria: {h['categoria']}")
            print(f"Cantidad: {h['cantidad']}")
            print(f"Estado: {h['estado']}")
            print(f"Valor: {h['valor']}")
    except FileNotFoundError:
        print("No Existen Herramientas Registradas")

def buscar_herramienta():
    print("=====/Buscar Herramientas Por ID---------")
    id_h = input("Ingrese El ID De La Herramienta")
    try:
        with open("herramientas.json","r",encoding="utf-8") as ark:
            datos= json.load(ark)
        if id_h in datos:
            h = datos[id_h]
            print("///--HERRAMIENTA ENCONTRADA--///")
            print(f"ID: {id_h}")
            print(f"Nombre: {h['nombre']}")
            print(f"Categoria: {h['categoria']}")
            print(f"Cantidad: {h['cantidad']}")
            print(f"Estado: {h['estado']}")
            print(f"Valor: {h['valor']}")
        else:
            print("No Existe Herramienta con ese ID")
    except FileNotFoundError:
        print("No Existen Herramientas Registradas")

def actualizar():
    print("\n ===Actualizar Informacion Herramientas===")
    id_h = input("Ingrese El ID De La Herramienta")
    try:
        with open("herramientas.json", "r", encoding="utf-8") as ark:
            datos=json.load(ark)
        
        if id_h not in datos:
            print("No Existe Herramienta Registrada")
            return
        herramientas = datos[id_h]
        print("\n (Enter Para Mantener El Dato Actual)")
        print(f"ID: {id_h}")
        nombre_actualizado = input(f"nombre: [{herramientas['nombre']}]") or herramientas["nombre"]
        categoria_actualizada = input(f"categoria: [{herramientas['categoria']}]") or herramientas["categoria"]
        cantidad_actualizada= input(f"cantidad: [{herramientas['cantidad']}]") or herramientas["cantidad"]
        valor_actualizado= input (f"valor: [{herramientas['valor']}]") or herramientas["Valor"]
        estado_op = input(f"Opción actual [{herramientas['estado']}]: ")


        if estado_op == "1":
            estado = "Activa"
        elif estado_op == "2":
            estado = "En reparación"
        elif estado_op == "3":
            estado = "Fuera de servicio"
        else:
            print("Estado inválido.")
            return

        datos[id_h] = {
            "nombre": nombre_actualizado,
            "categoria": categoria_actualizada,
            "cantidad": cantidad_actualizada,
            "estado": estado,
            "valor": valor_actualizado
        }
        with open("herramientas.json", "w", encoding="utf-8") as ark:
            json.dump(datos,ark, indent=4, ensure_ascii=False)
            print("-----Archivo actualizado correctamente-----")
    except FileNotFoundError:
        print("No Existen Herramienta Registrada")
    except Exception as e:
        print("Ocurrio un error inesperado",e)

def eliminar_herramientas():
    print("======= ELIMINAR HERRAMIENTA ========")
    id_h = input("Ingrese El ID De La Herramienta Que Desea Eliminar: ")
    try:
        with open ("herramientas.json", "r", encoding="utf-8") as f:
            datos=json.load(f)
        if id_h not in datos:
            print("No Hay Herramienta Registrado Con Ese ID")
            return
        herramienta= datos[id_h]
        print(f"nombre: {herramienta['nombre']} {herramienta['categoria']}")

        confirmar = input ("Seguro Que Desea Eliminar Esa Herramienta (si/no): ").lower()
        if confirmar !="si":
            print ("Cancelando Eliminacion")
            return
        del datos[id_h]
        with open("herramientas.json", "w", encoding="utf-8") as arc:
            json.dump(datos, arc, indent=4, ensure_ascii=False)

        print("------/HERRAMIENTA ELIMINADA EXITOSAMENTE ------")
    except FileNotFoundError:
        print("No Hay Herramienta Registrado")
    except Exception as e:
        print(f"Error inesperado al elimiar: {e}")
    registrar_log(
    "WARNING",
    f"Herramienta {id_h} inactivada"
    )

def menu_herramienta(usuario_actual):
    while True:
        print ("\n ====== Menu Herramientas =====")
        print ("1. Crear Herramienta")
        print ("2. Lista De Herramientas")
        print ("3. Buscar Herramienta Por ID")
        print ("4. Actualizar Herramienta")
        print ("5. Eliminar Herramienta")
        print ("6. Volver")
        try:
            opcion = int(input("Ingrese Una Opción: "))
            if opcion == 1:
                if usuario_actual["tipo"] == "Administrador":
                    crear_herramienta()
                else:
                    print("Solo Administrador")
            elif opcion == 2:
                listar_herramienta()
            elif opcion == 3:
                buscar_herramienta()
            elif opcion == 4:
                if usuario_actual["tipo"]=="Administrador":
                    actualizar()
                else:
                    print("Solo Administrador")
            elif opcion == 5:
                if usuario_actual["tipo"]=="Administrador":
                    eliminar_herramientas()
                else:
                    print("Solo administrador")
            elif opcion == 6:
                print("Saliendo Del Programa.....")
                break
            else:
                print("Opcion No Valida")
        except ValueError:
            print("Solo Valores Numericos")
        except Exception as e:
            print("Ocurrio Un Error Inesperando ",e)
            break



