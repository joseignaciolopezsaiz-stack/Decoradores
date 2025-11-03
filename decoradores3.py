
def mi_wrapper(func):
    print(func.__name__)
    print("1")
    def wrapper(*args):
        print(args)
        print("2")
        print("Antes de llamar a la función")
        resultado = func(*args)
        print("Después de llamar a la función")
        return resultado
    return wrapper

def suma(*args):
        lista = list(args)
        print(lista)
        a = 0
        for i in lista:
            a = a + i
            #print(i)
        print(a)
mi_wrapper(suma)(2,3,4,5,6,7,8, 9,10)