valor=1
maior_valor=-999999
menor_valor=999999


while valor!=0:
    valor=int(input('Digite um número:\n'))
    if valor <0:
        print(f'Esse valor é inválido pois ele é negativo.')
    if valor>maior_valor:
        maior_valor=valor
    if valor<menor_valor and valor>0:
        menor_valor=valor
    
        
print(f'Dos números digitados, o menor valor é {menor_valor}, e o maior valor é {maior_valor}')
        
