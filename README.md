# consumodeenergia
Um código em python que calcula o consumo de energia. Neste código, calculamos a energia (potência em kWh pelo tempo em horas), e a energia pelo custo de R$ por kWh e, por fim, quanto isso gasta em um mês (30 dias, mês comercial).

# Fórmulas Utilizadas

Fórmula da Energia:
E = P × Δt
Onde P é o valor em kWh -> se for em W, é dividido por 1000
Δt -> Tempo em horas

Fórmula do Consumo:
C = E × R$
Onde E é a energia que calculamos anteriormente e o R$ é o preço por kWh que varia de acordo com a distribuidora de energia e região.

Fórmula Mensal:
C × 30
C = o valor que calculamos anteriormente
30 = mês comercial
