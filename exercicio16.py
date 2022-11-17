total_pessoas_entrevistadas=0
total_idade_pessoas=0
idade=1

while idade !=0:
    idade=(int(input('Informe a sua idade:\n')))
    if idade<=0:
        break  
                     
    total_pessoas_entrevistadas+=1
    total_idade_pessoas+=idade
   
print(f'A média das idades das pessoas entrevistadas é: {total_idade_pessoas/total_pessoas_entrevistadas}')