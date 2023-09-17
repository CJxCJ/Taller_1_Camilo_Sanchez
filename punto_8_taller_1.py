x = float(input("ingresar frecuencia en hz: "))


if 0 < x < 30 * (10**3):
  print("es una onda de muy Baja Frecuencia - Radio")

    
elif 30 * (10**3) < x < 650 * (10**3):
  print("es una onda de Onda Larga - Radio")
  

elif 650 * (10**3) < x < 1.7 * (10**6):
  print("es una onda de Onda Media - Radio")
  

elif 1.7 * (10**6) < x < 30 * (10**6):
  print("es una onda de Onda Corta - Radio")
 
  
elif 30 * (10**6) < x < 300 * (10**6):
  print("es una onda de Muy Alta Frecuencia-Radio")
  
  
elif 300 * (10**6) < x < 3 * (10**8):
  print("es una onda de Ultra Alta Frecuencia-Radio")
  
  
elif 3 * (10**8) < x < 300 * (10**9):
  print("es una onda de Microondas")
  
  
elif 300 * (10**9) < x < 6 * (10**12):
  print("es una onda de Infrarrojo lejano/submilimétrico")
   
  
elif 6 * (10**12) < x < 120 * (10**12):
  print("es una onda de Infrarrojo medio")
  
  
elif 10 * (10**12) < x < 384 * (10**12):
  print("es una onda de Infrarrojo cercano")
  
  
elif 384 * (10**12) < x < 7.89 * (10**14):
  print("es una onda de Espectro Visible")
    
  
elif 7.89 * (10**14) < x < 1.5 * (10**15):
  print("es una onda de Ultravioleta cercano")
  
  
elif 1.5 * (10**15) < x < 30 * (10**15):
  print("es una onda de Ultravioleta extremo")
  
  
elif 30 * (10**15) < x < 30 * (10**18):
  print("es una onda de Rayos X")  


elif 30 * (10**18) < x < 300 * (10**99):
  print("es una onda de Rayos Gamma")  


else:
  print("No pertenece a ninguna region del espectro electromagnetico")