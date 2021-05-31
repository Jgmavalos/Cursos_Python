
def read():
    numbers = []
    with open ("./files/numbers.txt", "r", encoding="utf-8") as f:
        for line in f:
            numbers.append(int(line))
    print(numbers)
            
def write():
    names = [ 'Jhon', 'Juan', 'Sofía', 'Isabella']
    with open("./files/names.txt", "w", encoding="utf-8") as f:
        for name in names:
            f.write(name)
            f.write("\n")

# con el comando 'a' en vez de 'w'. Puedo agregar datos a mi archivo sin sobreescribir la informacion

def run():
    write()


if __name__=='__main__':
    run()
