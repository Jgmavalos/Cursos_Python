import random

def ordenamiento_mezcla(lista):
    if len(lista) > 1:
        medio = len(lista)//2
        izq = lista[:medio]
        der = lista[medio:]
        print(izq, '*'* 5, der)

        #Llamada recursiva cada mitad
        ordenamiento_mezcla(izq)
        ordenamiento_mezcla(der)


        #Iteradores para recorrer las dos sublistas
        i = 0
        j = 0
        #Iterador lista principal
        k = 0

        while i < len(izq) and j < len(der):
            if izq[i] < der[j]:
                lista[k] = izq[i]
                i += 1
            else:
                lista[k]= der[j]
                j += 1
            
            k += 1
            
        
        while i < len(izq):
            lista[k] = izq[i]
            i += 1
            k += 1


        while j < len(der):
            lista[k] = der[j]
            j += 1
            k += 1


        print(f'izquierda {izq}, derecha {der}')
        print(lista)
        print('-'* 50)

    return lista

if __name__=='__main__':
    tamano_lista = int(input('De que tamaño sera la lista?: '))

    lista = [random.randint(0,100) for i in range(tamano_lista)]
    print(lista)
    print('-' * 20)

    lista_ordenada = ordenamiento_mezcla(lista)
    print(lista_ordenada)

