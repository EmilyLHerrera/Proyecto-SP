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

        print("\nel monto del préstamo es:", cantidad)
        print("el total de intereses es igual a:", intereses_finales)
        print("el seguro es:", seguro)
        print("el total a pagar es igual a:", total)
        print("El total a pagar mensualmente es:", pago_mensual)

        # Convertimos plazo a int para que la función range() funcione correctamente
        for mes in range(1, int(plazo) + 1):
            print("Mes", mes, "-pago", round(pago_mensual, 2))

    print()
    continuar = int(input("¿Deseas calcular otro prestamo? responde 1 para si, 2 para no: "))

print("Gracias por utilizar la calculadora, hasta pronto!!")