contarMaior50 = 0
tamanho = 2
contarPessoasEntre10E20 = 0
somaAltura = 0
contarPesoMenor = 0
for i in range(tamanho):
    idade = int(input(f"Informe a idade da pessoa {i + 1}"))
    altura = int(input(f"Informe a altura da pessoa {i + 1}"))
    peso = float(input(f" Informe o peso da pessoa {i + 1}"))

    if idade >+ 50:
        contarMaior50 += 1 
    if idade >= 10 and idade <= 20:
        contarPessoasEntre10E20 += 1
        somaAltura += altura
    if peso < 40:
        contarPesoMenor += 1

media_alturas=(somaAltura/contarPessoasEntre10E20)
porcentagem = contarPesoMenor/tamanho*100