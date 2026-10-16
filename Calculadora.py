def calcular_intereses(cantidad, intereses, plazo):
    """
    (uso de operadores y funciones)
    recibe: cantidad valor numérico, intereses valor numérico, plazo valor numérico
    calcula los interéses del préstamo
    devuelve: los resultados de los intereses
    """
    tasa = intereses / 100
    tiempo = plazo / 12
    intereses_finales = cantidad * tasa * tiempo
    return intereses_finales


def calcular_total(cantidad, intereses, seguro):
    """
    (uso de operadores y funciones)
    recibe: cantidad valor numérico, intereses valor numérico, seguro valor numérico
    suma la cantidad del préstamo, los intereses y el seguro
    devuelve: total a pagar
    """
    total = cantidad + intereses + seguro
    return total


def calcular_pago(total, plazo):
    """
    (uso de operadores y funciones)
    recibe: total valor numérico, plazo valor numérico
    divide el total del prestamo entre el número de meses
    devuelve: pago mensual
    """
    pago = total / plazo
    return pago


continuar = 1

while continuar == 1:
    cantidad = float(input("ingresa la cantidad del préstamo en pesos: "))
    intereses = float(
        input("ingresa la tasa anual de intereses en porcentaje: "))
    plazo = float(input("ingresa el plazo para pagar en meses: "))

    if cantidad <= 0:
        print("la cantidad debe ser mayor a cero, tu cálculo no es posible: ")
    elif intereses < 0:
        print("la tasa de intereses no puede ser negativa, tu cálculo no es posible")
    elif plazo <= 0:
        print("el plazo a pagar no puede ser igual o menor a 0 tu cálculo no es posible")
    else:
        intereses_finales = calcular_intereses(cantidad, intereses, plazo)
        seguror = int(input("¿el préstamo cuenta con seguro? responde 1 para si, 2 para no: "))

        if seguror == 1:
            seguro = float(input("ingresa el monto del seguro en pesos: "))
            if seguro < 0:
                print("el seguro no puede ser negativo")
                seguro = 0
            else:
                print("Seguro registrado correctamente")
        elif seguror == 2:
            seguro = 0
        else:
            print("opción no válida, no se considera valor para el seguro")
            seguro = 0

        total = calcular_total(cantidad, intereses_finales, seguro)
        pago_mensual = calcular_pago(total, plazo)
    #lista de datos del préstamo
        datos_prestamo = [
            cantidad,
            intereses,
            plazo,
            intereses_finales,
            seguro,
            total ]
        pagos_mensuales = []
        for mes in range(1, int(plazo) +1):
            pagos_mensuales.append(round(pago_mensual, 2))

        print("monto del préstamo es:", datos_prestamo[0])
        print("tasa anual de intereses:", datos_prestamo[1], "%")
        print("plazo en meses:", datos_prestamo[2])
        print("total de intereses:", datos_prestamo[3])
        print("monto del seguro:", datos_prestamo[4])
        print("total a pagar :", datos_prestamo[5])
        for mes in range(len(pagos_mensuales)):
            print(
                "Mes", mes + 1,
                "-pago:", pagos_mensuales[mes] )

    print()
    continuar = int(input("¿Deseas calcular otro prestamo? responde 1 para si, 2 para no: "))

print("Gracias por utilizar la calculadora, hasta pronto!!")