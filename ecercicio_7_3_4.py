numero = 38
tentativa = 0

while tentativa != numero:
    tentativa = int(input("Informe um número entre 1 e 50: "))

    if tentativa > 50 or tentativa < 1:
        continue    
    if tentativa == numero:
        print("Voce acertou!")
        break
    if tentativa < numero:
        print ("Chute num número mais alto!")
        continue
    if tentativa > numero:
        print("Chute um número mais baixo")
        continue
