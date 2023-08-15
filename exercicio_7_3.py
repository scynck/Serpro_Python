idade = int(input("Informe sua idade: "))
peso = float(input("Informe seu peso: "))
dormiu = input("Dormiu pelo menos 6 horas nas últimas 24h? ")
dormiu = True if dormiu in ["Sim", "sim"] else dormiu == False

if idade >= 16 and idade <=69 and peso > 50 and dormiu == True:
    doador = True
    print("Você pode doar sangue")
else:
    doador = False
    print("Você não pode doar sangue")