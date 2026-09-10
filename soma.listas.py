def decoradora(func):
    def verificadora(x, y):
        try: 
            for i, d in zip(x, y):
                int(i), int(d)
            return func(x, y)
        except ValueError: 
            return'devem conter apenas números'
    return verificadora

@decoradora
def soma_listas(lista1, lista2):
    return [int(i) + int(d) for i, d in zip(lista1, lista2)]

l1 = [1,2,3,4,5,6,7]
l2 = [1,2,3,4]

def decoradora(func):
    def verificadora(x, y):
        try: 
            for i, d in zip(x, y):
                int(i), int(d)
            return func(x, y)
        except ValueError: 
            return'devem conter apenas números'
    return verificadora

@decoradora
def soma_listas(lista1, lista2):
    return [int(i) + int(d) for i, d in zip(lista1, lista2)]

l1 = [1,2,3,4,5,6,7]
l2 = [1,2,3,4]

print(soma_listas(l1,l2))