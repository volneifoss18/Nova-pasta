total_pessoas_entrevistadas_50=0
total_alturas_pessoas_50=0
idade=1

while idade !=0:
    idade=(int(input('Informe a sua idade:\n')))
    if idade<=0:
        break  
    altura=(int(input('Informe a sua altura em cm:\n')))
                     
    if idade > 50:
        total_pessoas_entrevistadas_50+=1
        total_alturas_pessoas_50+=altura
   
print(f'A média de altura das pessoas maiores de 50 anos é: {total_alturas_pessoas_50/total_pessoas_entrevistadas_50}')