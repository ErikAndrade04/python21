Notas = [10.0, 6.0, 9.9, 6.8, 3.0, 5.2]

Notas_acima_sete = 0
for nota in Notas:
    if nota > 7:
        Notas_acima_sete += 1
        print(f"Quantidade de notas acima de 7: {Notas_acima_sete}")