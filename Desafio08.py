try:
    valor_compra = float(input("Digite o valor da compra: R$ "))

    if valor_compra > 500:
        desconto = 0.20 
    elif valor_compra >= 200:
        desconto = 0.10  
    else:
        desconto = 0.0  

    valor_desconto = valor_compra * desconto
    preco_final = valor_compra - valor_desconto

    print(f"\nValor original: R$ {valor_compra:.2f}")
    print(f"Desconto aplicado: {desconto*100:.0f}%")
    print(f"Valor do desconto: R$ {valor_desconto:.2f}")
    print(f"Preço final: R$ {preco_final:.2f}")

except ValueError:
    print("Por favor, digite um valor numérico válido.")