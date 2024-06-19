with open(nombre_archivo, mode='w', newline='') as archivo_csv:
    writer = csv.writer(archivo_csv)
    writer.writerow(['Bitácora del Auto'])
    for evento in bitacora:
        writer.writerow([evento])
        print(f"Registro guardado en '{nombre_archivo}' con éxito.")
    except Exception as e:
        print(f"Error al guardar el archivo: {e}, coloque un nombre y extensión al archivo")
def menu():
    while True:
            print("\nMenú de registro histórico de acciones en el Auto:")
            print("1. Agregar acción")
            print("2. Verificar histórico")
            print("3. Guardar en archivo CSV")
            print("4. Salir")
            try:
            opcion = int(input("Ingrese la opción deseada: "))
            if opcion == 1:
               print("Escriba la acción (EJ: encender auto, viaje de Puerto Montt a Santiago")
               print("apagado auto, colocar alarma)")
               evento = input("Escriba la acción: ")
               agregar_evento(evento)
            elif opcion == 2:
                historico()
            elif opcion == 3:
               nombre_archivo = input("Ingrese el nombre del archivo CSV para guardar el registro:")
ejemplo:'bitacoraAuto.csv':")
            guardar_registro_csv(nombre_archivo)
        elif opcion == 4:
            print("saliendo de la bitácora")
            break
        else:
        print("Opción no válida. Por favor, ingrese una opción válida.")
    except ValueError as e:
    print(f"Error: {e}. Por favor, ingrese un valor numérico válido.")
if __name__ == "__main__":
menu()