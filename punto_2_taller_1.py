x = float(input("ingrese el primer numero: "))
y = float(input("ingrese el segundo numero: "))
z = float(input("ingrese el tercer numero: "))

if x > y and x > z:
  print(x, "es mayor que",y, "y" ,z)

elif y > x and y > z:
  print(y, "es mayor que",x, "y" ,z)
 
elif z > x and z > y:
  print(z, "es mayor que",x, "y" ,y)
  
else: 
  print("no hay un solo valor mayor ")