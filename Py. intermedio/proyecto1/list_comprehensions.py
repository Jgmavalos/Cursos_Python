

def run():
    
    #values = [i for i in range(1,1001) if i % 4 == 0 and i % 6 == 0 and i % 9 == 0]
    #print(values)

    print([i**2 for i in range(1,1001) if i % 36 == 0])

    #squares =[]
    #for i in range(1,101):
    #    if i % 5 != 0: # se introduce condicion de eleccion
    #        squares.append(i**2)
    #print(squares)




if __name__=='__main__':
    run()

