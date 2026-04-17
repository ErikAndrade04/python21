vendas = [ 100, 50, 78, 13, 80]

soma_pares = 0

for venda in vendas:
     if venda % 2 == 0:
        soma_pares += venda

        print(f"A soma das vendas pares é: {soma_pares}")