def mi_decorador(funcion1, funcion2):
    def nueva(*arg):
        print("Llamada a la funcion",funcion2.__name__)
        funcion2(*arg)
        arg1,arg10 = arg
        print(arg1)
        print(arg10)
        print(f"me llamo {arg1} y {arg10}")
        
        def otra_func(arg1, arg2 = "yo"):
            print(arg1)
            print(arg2)
            print(f"Me llamo {arg1} y {arg2}")
            print("Llamada a la funcion",funcion1.__name__)
            funcion1(arg1,arg2)
            print("Llamada a la funcion" ,funcion2.__name__)
            funcion2(arg1,arg2)
            
            def otra_func2(arg3):
                print(arg3)
                print(f"Me llamo {arg3}")              
                def otra_func3(*arg4):
                    arg41,arg42= arg4
                    
                    print(arg41)
                    print(arg42)
                    print("Llamada a la funcion",funcion1.__name__)
                    funcion1(*arg4)
                    print("Llamada a la funcion",funcion2.__name__)
                    
                    funcion2(*arg)
                    funcion2(*arg4)
                    return
                print("otra_func3 =", otra_func3.__name__)
                return otra_func3
            print("otra_func2 =", otra_func2.__name__)
            return otra_func2
        print("otra_func=",otra_func.__name__)
            
        return otra_func
    print("nueva =", nueva.__name__)
    return nueva
#dos parametros
def imprimir(*hola):
    hola1, hola2= hola
    print(f"hola {hola1} y {hola2}")
#dos parametros
def comprar(*nombre):
    nombre1,nombre2 = nombre
    print(f"compra {nombre1} y {nombre2}")
# 2 func, 2 param, 1 o 2 param, 1 param, 2 param
mi_decorador(imprimir,
 comprar)("jose","Pablo")("Luis")("Julian")("Andres","Parla")