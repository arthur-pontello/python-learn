palavra = input("Digite sua palavra: ")
numero_letras = len(palavra)
numero_tentativas = int(input("Digite a quantidade de tentativas"))
palpites = ["-"] * numero_letras

while("-" in palpites):
    i = 0
    print("".join(palpites))
    palpite = input("palpite: ")
    for letra in palavra:
        if palpite == letra:
            palpites[i] = letra
        i += 1

            

print(f"Parabens a palavra era {palavra}")
            
