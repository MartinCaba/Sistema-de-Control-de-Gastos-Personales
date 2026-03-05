# Sistema de Control de Gastos Personales

gastos = []  # [monto, categoria]

def cargar_gastos():
    continuar = "SI"

    while continuar == "SI":

        monto = 0
        while monto == 0:
            monto = float(input("Ingrese el monto: "))
            if monto == 0:
                print("Error: el monto no puede ser 0")

        categoria = input("Ingrese la categoría o producto: ")

        gastos.append([monto, categoria])

        continuar = input("¿Desea agregar otro gasto? (SI/NO): ")


def mostrar_total_general():
    total = 0
    for gasto in gastos:
        total += gasto[0]

    print("\nTotal gastado:", "$",total)


def mostrar_por_categoria():
    categorias_mostradas = []

    print("\nGasto por categoría o producto:")

    for gasto in gastos:
        categoria = gasto[1]

        if categoria not in categorias_mostradas:
            total_categoria = 0

            for g in gastos:
                if g[1] == categoria:
                    total_categoria += g[0]

            print(categoria,":","$", total_categoria)
            categorias_mostradas.append(categoria)


def mostrar_mayor_menor():
    if len(gastos) == 0:
        print("No hay gastos cargados")
        return

    if len(gastos) == 1:
        print("\nSolo hay un gasto registrado.")
        print("Gasto más alto:", "$",gastos[0][0], "| Categoría:", gastos[0][1])
        return

    mayor = gastos[0]
    menor = gastos[0]

    for gasto in gastos:
        if gasto[0] > mayor[0]:
            mayor = gasto
        if gasto[0] < menor[0]:
            menor = gasto

    print("\nGasto más alto:", "$",mayor[0], "| Categoría:", mayor[1])
    print("Gasto más bajo:", "$",menor[0], "| Categoría:", menor[1])


# Programa principal
cargar_gastos()
mostrar_total_general()
mostrar_por_categoria()
mostrar_mayor_menor()




























