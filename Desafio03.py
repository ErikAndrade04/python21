total = 0.0

while True:
    try:
        valor = float (input("Digite seu valor para finalizar a compra"))

        if valor == 0: 
            break

        total += valor 

    except ValueError:
        print ("Por favor digite um número valido")

        print("O total da compra é R$ {Total:.2F}")