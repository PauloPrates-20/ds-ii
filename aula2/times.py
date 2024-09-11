time1 = input("Digite o nome do primeiro time: ")
placar1 = int(input(f"Digite o placar do {time1}: "))
time2 = input("Digite o nome do segundo time: ")
placar2 = int(input(f"digite o placar do {time2}: "))

if placar1 > placar2:
    print(f"Vitória do {time1}!")
elif placar2 > placar1:
    print(f"Vitória do {time2}!")
else:
    print("Empate!")