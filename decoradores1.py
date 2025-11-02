def decorador1(*a):
    a1,*b= a
    print("hola" ,a1)
    def decorador2(*b):
        b1,c= b
        print("hola",b1)
        def decorador3(c):
            print("hola",c)
            return
        return decorador3(c)
    return decorador2(*b)
decorador1("Maria","Juan"," Pablo")
        
    