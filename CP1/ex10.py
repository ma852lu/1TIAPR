temp = float(input("Digite a temperatura em °C: "))
if temp < 0:
    print("Congelante")
elif temp <= 30:
    print("Agradável")
else:
    print("Quente")