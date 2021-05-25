menu = """ 
Bienvenido al conversor de monedas a dolar 💱 💲

1 - Pesos colombianos (COP)
2 - Pesos mexicanos (MXN)
3 - Pesos argentinos (ARS)

Elige una opcion: """

def conversor(tipo_peso,dolar):
    pesos = input("¿Cuántos pesos"+ tipo_peso + "tienes?")
    pesos = float(pesos)
    endolar = pesos/dolar
    endolar = round(endolar,2)
    endolar = str(endolar)
    print("Tienes $" + endolar + "dolares")
opcion= int(input(menu))

if opcion == 1:
    conversor("colombianos (COP)", 3875)
elif opcion == 2:
    conversor("mexicanos (MXN)", 24)
elif opcion == 3:
    conversor("argentinos (ARS)", 65)
else:
    print("Intenta nuevamente")

