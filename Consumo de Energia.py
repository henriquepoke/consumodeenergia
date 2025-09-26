print("""
Fórmula da Energia:
E = P × Δt
Onde P é o valor em kWh -> W dividido por 1000
Δt -> Tempo em horas""")
print()
kWh = int(input("Digite o valor de P (em W ou kWh): "))

Question = str(input("Esse valor é em kWh?: "))
if 'sim' in str(Question).lower():
    print()
else:
    kWh = kWh / 1000
    print(f"Fiz a conversão automaticamente! Resultado: {kWh}kWh!")

H = input("Digite o tempo (Δt) em horas: ")
E = kWh * float(H[0])
print(f"O resultado é de {E}kWh!")
print()
ContinueVR = str(input("Continuar para calcular o consumo em R$? "))
if 'sim' in str(ContinueVR).lower():
    print("""
    Fórmula do Consumo:
    C = E × R$""")
    VReal = float(input("Digite o valor em R$: "))
    CE = E * VReal
    print(f"Resultado: R${CE}!")
    continueM = input("Quer calcular o consumo mensal? ")
    if 'sim' in str(continueM).lower():
        resul = CE * 30
        print(f"Resultado mensal: R${resul:.2f}")
else:
    print("Programa finalizado!")