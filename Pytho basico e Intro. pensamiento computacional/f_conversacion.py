def conversacion(mensaje):
    print("Hola, ¿Còmo estàs?")
    print(mensaje)
    print("Adios")

opcion = int(input("Elige una opcion (1 2 3) : "))
if opcion== 1:
    conversacion("Elegiste 1")
elif opcion== 2:
    conversacion("Elegiste 2")
elif opcion== 3:
    conversacion("Elegiste 1")
else:
    print("Amigo solo eran 3 opciones, que te pasa?")
    