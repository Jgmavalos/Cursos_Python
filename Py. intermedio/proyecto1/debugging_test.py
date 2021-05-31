def divisors(num):
    divisors = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)
    return divisors

def run():
    try:
        num = int(input('Ingresa un número entero: '))
        if num < 0:
            raise Exception('Número negativo invalido')
        print(divisors(num))
        print('Terminó mi programa')

    except ValueError:
        print('Debes ingresar un número entero')

    except Exception:
        print('Debes ingresar un número entero positivo')

if __name__=='__main__':
    run()