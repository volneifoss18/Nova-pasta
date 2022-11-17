total_cand_1=0
total_cand_2=0
total_cand_3=0
total_cand_4=0
nulo=0
branco=0
total_votantes=0
voto=1

while voto !=0:
    voto=int(input('[1]Canditado 1\n[2]Canditado 2\n[3]Canditado 3\n[4]Canditado 4\n[5]Branco\n[6]Nulo\n'))
    if voto == 1:
        total_cand_1+=1
        total_votantes+=1
    if voto == 2:
        total_cand_2+=1
        total_votantes+=1
    if voto == 3:
        total_cand_3+=1
        total_votantes+=1
    if voto == 4:
        total_cand_4+=1
        total_votantes+=1
    if voto == 5:
        branco+=1
        total_votantes+=1
    if voto == 6:
        nulo+=1
        total_votantes+=1
    if voto == 0:
        break
    else:
        print(f'Código de candidato inválido!')

print(f'A quantidade de votos do candidato 1 é {total_cand_1}')
print(f'A quantidade de votos do candidato 2 é {total_cand_2}')
print(f'A quantidade de votos do candidato 3 é {total_cand_3}')
print(f'A quantidade de votos do candidato 4 é {total_cand_4}')
print(f"A porcentagem de votos nulos é {(nulo*100)/total_votantes:.2f}")
print(f"A porcentagem de votos brancos é {(branco*100)/total_votantes:.2f}")