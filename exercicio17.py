qtd_pessoas_total=0
canal=0
canal_4=0
soma_pessoas_4=0
soma_pessoas_5=0
soma_pessoas_7=0
soma_pessoas_12=0
canal_5=0
canal_7=0
canal_12=0
total=0
while canal!='0':
    canal=str(input(f'Informe o número do canal (4, 5, 7, 12):'))
    if canal == "0":
        break
    qtd_pessoas_total=int(input('Informe quantas pessoas estão assistindo o canal:'))
    if canal=="4":
        canal_4+=1
        soma_pessoas_4+=qtd_pessoas_total
        total+=qtd_pessoas_total
    if canal=="5":
        canal_5+=1
        canal_5+=1
        soma_pessoas_5+=qtd_pessoas_total
        total+=qtd_pessoas_total
    if canal=="7":
        canal_7+=1
        canal_7+=1
        soma_pessoas_7+=qtd_pessoas_total
        total+=qtd_pessoas_total
    if canal=="12":
        canal_12+=1
        canal_12+=1
        soma_pessoas_12+=qtd_pessoas_total
        total+=qtd_pessoas_total

porcentagem_4= (soma_pessoas_4*100)/total
porcentagem_5= (soma_pessoas_5*100)/total
porcentagem_7= (soma_pessoas_7*100)/total
porcentagem_12= (soma_pessoas_12*100)/total

print(f"A quantidade de pessoas assistindo o canal 4 são {soma_pessoas_4} e representam {porcentagem_4}%")
print(f"A quantidade de pessoas assistindo o canal 5 são {soma_pessoas_5} e representam {porcentagem_5}%")
print(f"A quantidade de pessoas assistindo o canal 7 são {soma_pessoas_7} e representam {porcentagem_7}%")
print(f"A quantidade de pessoas assistindo o canal 12 são {soma_pessoas_12} e representam {porcentagem_12}%")