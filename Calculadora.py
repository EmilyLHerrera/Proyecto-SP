def calcular_intereses(cantidad, intereses, plazo):
    """
    (uso de operadores y funciones)
    recibe: cantidad valor numérico, intereses valor numérico,
    plazo valor numérico
    calcula los intereses del préstamo usando la tasa anual
    y el plazo expresado en meses
    devuelve: los intereses del préstamo
    """
    tasa = intereses / 100
    tiempo = plazo / 12
    intereses_finales = cantidad * tasa * tiempo
    return intereses_finales


def calcular_total(cantidad, intereses, seguro):
    """
    (uso de operadores y funciones)
    recibe: cantidad valor numérico, intereses valor numérico,
    seguro valor numérico
    suma la cantidad del préstamo, los intereses y el seguro
    devuelve: total a pagar
    """
    total = cantidad + intereses + seguro
    return total


def calcular_pago(total, plazo):
    """
    (uso de operadores y funciones)
    recibe: total valor numérico, plazo valor numérico
    divide el total del préstamo entre el número de meses
    devuelve: pago mensual
    """
    pago = total / plazo
    return pago


def crear_pagos(pago_mensual, plazo):
    """
    (uso de funciones, listas y ciclo for)
    recibe: pago_mensual valor numérico, plazo valor entero
    crea una lista con el número de cada mes y el pago
    correspondiente a ese mes
    devuelve: lista anidada con los meses y sus pagos
    """
    pagos_mensuales = []

    for mes in range(1, plazo + 1):
        pago = round(pago_mensual, 2)
        pagos_mensuales.append([mes, pago])

    return pagos_mensuales


def crear_prestamo(cantidad, intereses, plazo,
                   intereses_finales, seguro, total,
                   pagos_mensuales):
    """
    (uso de funciones y listas anidadas)
    recibe: cantidad, intereses, plazo, intereses_finales,
    seguro, total y pagos_mensuales
    organiza los datos básicos, los datos financieros
    y los pagos mensuales en listas separadas
    devuelve: una lista anidada con toda la información
    del préstamo
    """
    datos_basicos = [cantidad,
                    intereses,
                    plazo]
    datos_financieros = [intereses_finales,
                        seguro,
                        total]
    prestamo = [datos_basicos,
                datos_financieros,
                pagos_mensuales]

    return prestamo


def mostrar_prestamo(prestamo):
    """
    (uso de funciones, listas anidadas y ciclo for)
    recibe: prestamo, una lista anidada con los datos
    muestra la información del préstamo y sus pagos mensuales
    devuelve: no devuelve ningún valor, solamente muestra
    los resultados en pantalla
    """
    print()
    print("Los datos del préstamo: ")
    print("Cantidad:", prestamo[0][0])
    print("Tasa anual de intereses:", prestamo[0][1], "%")
    print("Plazo en meses:", prestamo[0][2])
    print("Total de intereses:", prestamo[1][0])
    print("Monto del seguro:", prestamo[1][1])
    print("Total a pagar:", prestamo[1][2])

    print()
    print("Los pagos mensuales: ")

    for pago in prestamo[2]:
        print("Mes", pago[0], "- Pago:", pago[1])


def mostrar_historial(historial):
    """
    (uso de funciones, listas anidadas y ciclo for)
    recibe: historial, una lista que contiene los préstamos
    muestra el número, la cantidad, el total y el plazo
    de cada préstamo registrado
    devuelve: no devuelve ningún valor, solamente muestra
    los resultados en pantalla
    """
    print()
    print("El historial de los prestamos: ")

    for numero in range(len(historial)):
        print("Préstamo número:", numero + 1)
        print("Cantidad:", historial[numero][0][0])
        print("Total a pagar:", historial[numero][1][2])
        print("Plazo:", historial[numero][0][2], "meses")
        print("")

nombre = input("Porfavor ingresa tu nombre completo: ")
nombre = nombre.strip().title()

print()
print("Bienvenido", nombre)
print("Calculadora de prestamos")

continuar = "si"
historial = []

while continuar == "si":
    cantidad = float(input(
        "Ingresa la cantidad del préstamo en pesos: "))
    intereses = float(input(
        "Ingresa la tasa anual de intereses en porcentaje: "))
    plazo = int(input(
        "Ingresa el plazo para pagar en meses: "))
    if cantidad <= 0:
        print("La cantidad debe ser mayor a cero.")
    elif intereses < 0:
        print("La tasa de intereses no puede ser negativa.")
    elif plazo <= 0:
        print("El plazo debe ser mayor a cero.")
    else:
        intereses_finales = calcular_intereses(
            cantidad, intereses, plazo)

        seguror = ""

        while seguror != "si" and seguror != "no":
            seguror = input(
                "¿El préstamo cuenta con seguro? "
                "si/no: ")
            seguror= seguror.strip().lower()
            
            if seguror != "si" and seguror != "no":
                print("Opción no válida. Intenta nuevamente respondiendo con si/no: ")
        if seguror == "si":
            seguro = float(input(
                "Ingresa el monto del seguro en pesos: "))
            while seguro < 0:
                print("El seguro no puede ser negativo.")
                seguro = float(input(
                    "Ingresa nuevamente el seguro: "))
        else:
            seguro = 0

        total = calcular_total(cantidad, intereses_finales, seguro)
        pago_mensual = calcular_pago(total, plazo)
        pagos_mensuales = crear_pagos(pago_mensual, plazo)
        prestamo = crear_prestamo(cantidad,
                                 intereses,
                                 plazo,
                                 intereses_finales,
                                 seguro,
                                 total,
                                 pagos_mensuales)

        historial.append(prestamo)
        
        print()
        print("Cliente: ", nombre)
        
        mostrar_prestamo(prestamo)

    print()
    continuar = input("¿Deseas calcular otro préstamo? "
        "si/no: ")
    
    continuar= continuar.strip().lower()
    while continuar !="si" and continuar !="no":
        print("Opción no válida, porfavor escribe únicamente si o no")
        continuar = input("¿Deseas calcular otro préstamo? si/no: ")
        continuar = continuar.strip().lower()

mostrar_historial(historial)

print()
print("Gracias",nombre," por utilizar la calculadora")
print("Hasta pronto!!")