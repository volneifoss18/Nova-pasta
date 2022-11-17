i=0
faixa1 = 0
faixa5 = 0


for i in range (3):
    idade = int(input('Informe a sua idade: '))
    if idade <= 15:
        faixa1+= 1
    if idade > 60:
        faixa5+= 1
print(f'A porcentagem de pessoas na primeira faixa etária é: {(faixa1 * 100) / 3}% ')
print(f'A porcentagem de pessoas na última faixa etária é: {(faixa5*100) / 3}%')