#Ley de la suma
#1
def f(n):
    for i in range (n):
        print(i)

    for i in range(n):
        print(i)

# O(n) + O(n) = O(n+n) = O(2n) = O(n)

# Esta función tiene un crecimiento lineal 
# con respecto a n (crece en O(n))

#2
def f(n):
    for i in range (n):
        print(i)

    for i in range(n * n):
        print(i)

# O(n) + O(n * n) = O(n + n^2) = O(n^2)

# Por tanto, crece en 0(n^2)
#Funcion cuadratica

#Ley multiplicacion
#3
def f(n):
    for i in range(n):

        for j in range(n):
            print(i, j)

#loop dentro de otro loop
# O(n) * O(n) = O(n * n) = O(n^2)
#Funcion cuadratipa


#Recursividad multiple
#4
def fibonacci(n):

    if n == 0 or n ==1:
        return 1
    
    return fibonacci(n - 1) + fibonacci(n - 2)

# O(2**n)
#Crecimiento exponencial