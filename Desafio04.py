def categorizar_imc_academia():
   
    try:
        peso = float(input("Digite o seu peso (kg): ").replace(',', '.'))
        altura = float(input("Digite a sua altura (M): ").replace(',', '.'))

        if peso <= 0 or altura <= 0:
            print("Peso e altura devem ser valores positivos. Digite um número valido.")
            return
        
        imc = peso / (altura ** 2)
        print(f"\n Seu IMC é: {imc:.2f}")

        if imc < 18.5:
            print("Categoria: Abaixo do peso (Magro). Recomendado: Ganho de massa muscular.")
        elif 18.5 <= imc <= 24.9:
            print("Categoria: Peso normal. Objetivo: Manutenção ou definição.")
        else:

            print("Categoria: Acima de 24.9. Recomendado: Foco em perda de gordura/recomposição.")

    except ValueError:
        print("Erro: Por favor, insira apenas números. Use ponto ou vírgula para decimais.")
    except ZeroDivisionError:
        print("Erro: Altura não pode ser zero.")
