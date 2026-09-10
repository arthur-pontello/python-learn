print('lista de compras')
print('1- mostrar lista')
print('2- encerrar')
itens= []

while(True):
    item = input()
    try: 
        if int(item) == 1:
            for item in itens:
                print(item)

        if int(item) == 2:
            sair = input('tem certeza que quer sair?')
            if sair[0] == 's':
                with open("lista_compras.txt", "w") as notas:
                    notas.write("----lista de compras----" + '\n')
                    for i in itens:
                        notas.write(i + "\n")
                break
            else:
                continue
    except:
        itens.append(item)

