
menu = """ 
Este programa calcula el área para dos cuadriláteros

1 - Rectangulo
2 - Cuadrado

Elige una opcion: """

opcion= int(input(menu))

class Rectangulo:

    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base*self.altura

class Cuadrado(Rectangulo):

    def __init__(self, lado):
        super().__init__(lado, lado)


if __name__=='__main__':

    if opcion == 1:
        b = float(input("Ingresa el tamaño de la base: "))
        a = float(input("Ingresa el tamaño de la altura: "))
        rectagulo = Rectangulo(base= b, altura= a)
        print(rectagulo.area())

    else :
        l = float(input("Ingresa el tamaño del lado: "))
        cuadrado =Cuadrado(lado=l)
        print(f' El área de la figura geometrica es de: {cuadrado.area()} unidades cuadradas')


