Temperaturas = [21.0, 22.0, 23.0, 24.0, 25.0, 26.0]
somar_Temperaturas = 0.0 
contador = 0
for temp in Temperaturas:
 somar_Temperaturas += temp
 contador +1

 média = somar_Temperaturas / contador

 print ("Temperaturas da semana: ", Temperaturas )
 print (f"A temperatura média da semana é {média:.2f}ºC")