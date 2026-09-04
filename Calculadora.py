# Calculadora de préstamos.

print("Bienvenido a tu calculadora de préstamos")

#Datos del préstamo

cantidad=float(input("Ingresa la cantidad total del préstamo solicitado:"))
intereses=float(input("Ingresa la tasa anual de intereses en porcentaje (%)"))
plazo=int(input("Ingresa el plazo para pagar en meses"))

#Operaciones para el cálculo de los intereses

interesesf=(intereses/100)
tasa=(plazo/12)
interesesfinal=(interesesf*tasa*cantidad)

#Preguntar al usuario sobre su seguro

seguror=int(input("El préstamo cuenta con un seguro de pago, Responde 1 si la respuesta es sí o 2 sí la respuesta es no:"))
if seguror==1:
    segurom=float(input("Ingresa el monto del seguro"))
else:
    segurom=0
    
#Total a pagar
    
total=(interesesfinal+cantidad+segurom)

#cantidad de pagos mensuales

pagos=total/plazo

#verificar las entradas

print("Verifica tus datos")
print("Cantidad del préstamo:",cantidad)
print("Tasa anual de intereses:",intereses)
print("Plazo para pagar:",plazo)
print("Seguro del préstamo",segurom)

#imprimir los resultados

print("Los totales a pagar son:")
print("La cantidad total a pagar es de:",total)
print("La cantidad a pagar mensualmente es de:",pagos)
