valor_carro= float(input("Informe o valor do carro:\n"))
valor_a_vista = valor_carro*0.8
print(f"O valor a vista do carro é R${valor_a_vista}.")
juros=0.03
parcelas=6
valor_em_parcelamento=valor_carro * 1.03

for i in range(10):
    print(f"O valor em {parcelas} vezes é {valor_em_parcelamento:.2f} - juros = {juros:.2f}")
    parcelas+=6
    juros+=0.03
    valor_em_parcelamento=(valor_em_parcelamento*1.03)