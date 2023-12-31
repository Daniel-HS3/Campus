def leerValHoraEmpl():
    while True:
        try:
            n = int(input("Ingrese el valor de la hora trabajada del empleado: "))
            if n < 8000 or n > 150000:
                print("Valor de la Hora inválida. Debe estar en el rango de [8000, 150000]")
                continue
            return n
        except ValueError:
            print("Error al ingresar el valor de la hora trabajada.")

def leerHoraTrabEmpl():
    while True:
        try:
            n = int(input("Ingrese la horas trabajadas del empleado: "))
            if n < 1 or n > 160:
                print("Horas inválidas. Debe estar en el rango de [0, 160]")
                continue
            return n
        except ValueError:
            print("Error al ingresar las horas.")

def leerNombreEmpl():
    while True:
        try:
            nom = input("Ingrese el nombre del empleado:")
            nom = nom.strip()
            if len(nom) == 0 or not nom.isalnum():
                print("Nombre inválido")
                continue
            return nom
        except Exception as e:
            print("Error al ingresar el nombre.", e)

def leerIDEmpl():
    while True:
        try:
            n = int(input("Ingrese el ID del empleado: "))
            if n < 1:
                print("ID inválido. Debe ser mayor a cero")
                continue
            return n
        except ValueError:
            print("Error al ingresar el ID.")
            
def buscarEmpleado(lstEmpleado, idEmpl):
    for i in range(len(lstEmpleado)):
        if (lstEmpleado[i][0] == idEmpl):
            return i
    return -1


def modificarEmpleado(lstEmpleado):
    print("\n\n2. Modificar Empleado\n")
    
    idEmpl = leerIDEmpl()
    posEmpl = buscarEmpleado(lstEmpleado, idEmpl)
    if posEmpl == -1:
        print("El código del empleado no existe.")
        input()
        return
    
    print("\n")
    while True:
        op = int(input("\nQue desea modificar?\n1. Nombre\n2. Cantidad de Horas\n3. Valor de la hora\nOpcion? "))
        if op < 1 or op > 3:
            print("Opción inválida")
            input()
            continue
        break
    
    if op == 1:
        nombre = leerNombreEmpl()
        lstEmpleado[posEmpl][1] = nombre
    elif op == 2:
        cantHoras = leerHoraTrabEmpl()
        lstEmpleado[posEmpl][2] = cantHoras
    elif op == 3:
        valHora = leerValHoraEmpl()
        lstEmpleado[posEmpl][3] = valHora

def agregarEmpleado(lstEmpleado):
    print("\n\n*** 1. Agregar empleado\n")
    lstDatos = []
    id = leerIDEmpl()
    if buscarEmpleado(lstEmpleado, id) != -1:
        print("El id ya existe en la lista")
        input()
        return
    
    lstDatos.append(id)
    lstDatos.append(leerNombreEmpl())
    lstDatos.append(leerHoraTrabEmpl())
    lstDatos.append(leerValHoraEmpl())
    
    lstEmpleado.append(lstDatos)

def menu():
    while True:
        try:
            print("*** NOMINA ACME ***".center(40))
            print("MENU".center(40))
            print("1. Agregar empleado\n2. Modificar empleado\n3. Buscar emplado\n4. Eliminar empleado\n5. Listar empleados\n6. Listar nómina de un empleado\n7. Listar nómina de todos los empleados\n8. Salir")
            op = int(input(">>> Opción (1-8)"))
            if op < 1 or op > 8:
                print("Opción no válida. Escoja de 1 a 8.")
                input("Presione cualquier tecla para continuar...")
                continue
            return op
        except ValueError:
            print("Opción no válida. Escoja de 1 a 8.")
            input("Presione cualquier tecla para continuar...")

## PROGRAMA PRINCIPAL
lstEmpleado= []
while True:
    op = menu()
    if op == 1:
        agregarEmpleado(lstEmpleado)
        print(lstEmpleado)
        input()
    elif op == 2:
        modificarEmpleado(lstEmpleado)
    elif op == 3:
        while True:
            try:
                empleado_buscar = int(input("Digite el ID del empleado a buscar:"))
                if empleado_buscar < 0:
                    print("Código inválido, solo enteros positivos; Intente de nuevo.\n")
                    continue
                empleado = buscarEmpleado(lstEmpleado,empleado_buscar)
                if empleado != -1:
                    print(f"ID {lstEmpleado[empleado]}\n ")

            except ValueError:
                print("Valor inválido, intente de nuevo.\n")

        pass
    elif op == 4:
        pass
    elif op == 5:
        pass
    elif op == 6:
        pass
    elif op == 7:
        pass
    elif op == 8:
        print("\n\nGracias por usar el software. Adios")
        break