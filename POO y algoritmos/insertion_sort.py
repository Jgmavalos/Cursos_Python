import random

def insertion_sort(lista):
    n = len(lista)
    for i in range(1, n):
        j = i - 1
        valor = lista[i]
        while valor < lista[j] and j >= 0 :
            lista[j + 1] = lista[j]
            j -= 1
        lista[j + 1] = valor


if __name__=='__main__':
    tamano_lista = int(input('De que tamaño sera la lista?:'))
    lista = [random.randint(0,100) for i in range(tamano_lista)]
    print(lista)
    insertion_sort(lista)
    print(lista)


    