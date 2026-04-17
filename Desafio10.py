Frase = input("Digite uma frase para analisar; ")

vogais = "aeiouAEIOUáàâãéêíóôõúÁÀÂÃÉÊÍÓÔÕÚ"
contador = 0

for caractere in Frase:
 if caractere in vogais:
  contador + 1

print(f"A frase digitada tem {contador} vogais.")