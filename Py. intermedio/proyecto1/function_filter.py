
def run():

    my_list = [1,2,3,5,7,8,13,15,16,18,25,28]

    # Determinar cuales son impares en mi lista
    print(my_list)

    # Método 1 con filter
    odd = list(filter(lambda x: x%2 != 0, my_list))
    print(odd)

    # Método 2 sin filter
    odd = [i for i in my_list if i % 2 != 0]
    print(odd)

if __name__ == '__main__' :
    run()




