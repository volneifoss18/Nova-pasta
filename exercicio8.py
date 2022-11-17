tamanho=3
pessoas_50a_menos_60=0
somar_idades=0
contar_alturas=0
cont_olhos=0
cont_ruivos=0
for i in range(tamanho):
#ler idade, altura e peso
    idade=int(input(f"Informe a idade da pessoa {i+1}"))
    altura=int(input(f"Informe a altura da pessoa {i+1}"))
    peso=float(input(f" Informe o peso da pessoa {i+1}"))
    olhos=input("Informe a cor dos olhos (A,P,V e C)")
    cabelos=input("Informe a cor dos cabelos (P,C,L e R)")

    if idade>50 and peso<60:
        pessoas_50a_menos_60+=1
    if altura < 150:
        somar_idades+=idade
        contar_alturas+=1
    if olhos=="a":
        cont_olhos+=1
    if cabelos == "r" and olhos !="a":
        cont_ruivos+=1

media_idades=somar_idades/contar_alturas
porcentagem=(cont_olhos/tamanho)*100

print (F'A quantidade de pessoas com idade superior a 50 anos e peso inferior a 60 é {pessoas_50a_menos_60}.')
print(f'A média das idades das pessoas das pessoas que medem menos que 150m é de {media_idades}')
print(f'A porcentagem de olhos azuis entre todos é{porcentagem:.2f}%.')
print(f'A quantidade de pessoas ruivas que não possuem olhos azuis é {cont_ruivos}')