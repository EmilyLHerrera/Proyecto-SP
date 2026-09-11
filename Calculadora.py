#calculadora de préstamos
#Calcular los intereses

def calcular_intereses(cantidad,intereses,plazo):
    """
(uso deoperadores y funciones)
recibe:cantidad valor numérico, intereses valor numérico, plazo valor numérico
calculalos interéses del préstamo
devuelve:los resultados de los intereses
"""
    tasa=intereses/100
    tiempo=plazo/12
    interesesf=cantidad*tasa*tiempo
    return interesesf

#calcular con el seguro

def calcular_total(cantidad, intereses, seguro):
    """
(uso de operadores y funciones)
recibe:cantidad valor numérico, intereses valor numérico, seguro valor numérico
suma la cantidad del préstamo, los intereses y el seguro
devuelve: total a pagar
"""
    total=cantidad+intereses+seguro
    return total

#parte principal del programa
#definimos el valor de las variables

cantidad=float(input("Ingresa la cantidad del préstamo en pesos:"))
intereses=float(input("Ingresa la tasa anual de intereses en porcentaje:"))
plazo=float(input("Ingresa el plazo para pagar en meses:"))

#decir si los datos son posibles
if cantidad<=0:
    print("La cantidad debe ser mayor a cero, tu cálculo no es posible:")
elif intereses<0:
    print("La tasa de intereses no puede ser negativa, tu cálculo no es posible")
elif plazo<=0:
    print("El plazo a pagar no puede ser igual o menor a 0 tu cálculo no es posible")
else:
    #si todo es correcto se comenzará a calcular el total a pagar
    interesesf =calcular_intereses(cantidad,intereses,plazo)
    print(interesesf)
    
