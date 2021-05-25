

def morral(tamano_morral, peso, valores, n):
    
    if n == 0 or tamano_morral == 0:
        return 0

    if peso[n - 1] > tamano_morral:
        return morral[tamano_morral, peso, valores, n - 1]

    return max(valores[n - 1] + morral(tamano_morral - peso[n - 1], peso, valores, n - 1), morral(tamano_morral, peso, valores, n - 1))



if __name__=='__main__':
    valores = [60, 100, 120]
    peso = [10, 20, 30]
    tamano_morral = 50
    n = len(valores)

    resultado = morral(tamano_morral, peso, valores, n)
    print(resultado)