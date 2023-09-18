# Taller_1_Camilo_Sanchez

## Explicacion puntos taller 1 

## Punto 1
Resultado del quiz de python:

![quiz_taller_1_resuelto](https://github.com/CJxCJ/Taller_1_Camilo_Sanchez/assets/115903431/3220b327-95d0-47c4-a21e-a515f763c5f8)


## Punto 2

En este codigo se pide que ingresen los 3 numeros reales para empezar el programa, cuando este empieza por medio del condicional if se comparan y dependiendo de cual sea el mayor imprime la repuesta correspondiente al mayor, si no se cumple las condiciones establecida arojara un mensaje de que no hay un valor mayor.

````code

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

````


## Punto 3

En este codigo se pide que ingresen un numero entero, cuando empiece este programa saca el modulo del numero ingresado x entre 2, si este da 0 el programa responde que es par, sino es impar.

````code
x = int(input("ingrese un numero entero: "))

if x % 2 == 0:
  print(x, "es par")

else:
  print(x, "es impar")
````

## Punto 4

En este codigo se piden 2 numeros reales, aca con el condicional if, si el modulo del primer numero x entre el segundo numero y es igual a 0 el programa aroja que x es multiplo de y, de lo contrario arroja que no es multiplo.

````code
x = float(input("ingrese un numero entero: "))
y = float(input("ingrese un numero entero: "))

if x % y == 0:
  print(x, "es multiplo de" ,y)

else:
  print(x, "no es multiplo de" ,y)
````


## Punto 5

En este codigo se ingresan 3 numeros reales, si la suma de los 2 primeros numero es mayor al tercero el programa arroja que z es mayor que la suma de x mas y, sino luego mira si la suma es menor, en este caso arroja que la suma de x mas y es menor a z y en el ultimo caso si no coincide con las anteriores arroja que es igual.

````code
x = float(input("ingrese el primer numero: "))
y = float(input("ingrese el segundo numero: "))
z = float(input("ingrese el tercer numero: "))

if (x + y) > z:
  print(x, "sumado" ,y, "es mayor que" ,z)

elif (x + y) < z:
  print(x, "sumado" ,y, "es menor que" ,z)

else: 
  print("la suma de ",x, "mas" ,y, " es igual a" ,z,)

````

## Punto 6

En este codigo se le pide al usuario una letra, el programa compara entre los valores ASCII asignados a las vocales, si el numero el codigo ASCII coincide con alguno del condicional arroja que es una vocal, sino arroja que es una consonante.

````code
x = input("escriba una letra: ")
y = ord(x)

if y == 65 or y == 69 or y == 73 or y == 79 or y == 85 or y == 97 or y == 101 or y == 105 or y == 111 or y == 117:
  print(x, "es una vocal")
  
else:
  print(x, "es una consonante")

````


## Punto 7

En este codigo se piden 5 numeros reales, estos numeros se operan en unas variables 
establecidas para ahorrar lineas de codigo y simplificar. Las variables son:

- prom: la cual saca el promedio entre los 5 numeros

- orde: es una lista de los numeros en el orden ingresado. que luego se ordena de forma ascedente con el comando .sort

- medi: la mediana, sacando el 3er numero de la lista orde.sort

- geo: es el promedio multiplicativo de todos los numeros, se multiplican los 5 sumeros entre ellos y luego se eleba a la potecia de 1 / la cantidad de numeros multiplicados, es decir 5.

- edro: es otra lista que por medio de .sort invertido nos da una lista descendente

- men: saca el primer valor de orde, es decir el menor de los 5 numeros
- may: saca el primer valor de edro, es decir el mayor de los 5 numeros

- pot: eleva la variable may, el mayor, potencia de men el menor

- cub: saca la raiz cubica de men, el menor, elevandolo a la potencia de 1/3

Despues de plantear todas esas variables se procede a imprimir todas las respuestas solcitadas simplemente llamando las variables

````code
v = float(input("ingrese el primer numero: "))
w = float(input("ingrese el segundo numero: "))
x = float(input("ingrese el tercer numero: "))
y = float(input("ingrese el cuarto numero: "))
z = float(input("ingrese el quinto numero: "))

prom = float(v + w + x + y + z)/5 

orde = [v,w,x,y,z]

orde.sort()

medi = orde[2]

geo = (v * w * x * y *z) ** (1/5)

edro = [v,w,x,y,z]

edro.sort(reverse=True)

men = orde[0]
may = edro[0]

pot = (may**men)

cub = men ** (1/3)


print(prom, "es el promedio")

print(medi, "es la mediana")

print("{0:.5f}".format(geo), "es el promedio multiplicativo")

print(orde, "es el orden ascendete")

print(edro, "es el orden descendente")

print(pot, "es la potencia del mayor elevado por el menor")

print("{0:.5f}".format(cub), "es la raiz cubica del menor")

````


## Punto 8

En este codigo se ingresa un numero real el cual representa la longuitud de una onda en hz con el condicional if se genera unos rangos en los que va las ondas segun su region en el espectro electromagnetico, estos valores van desde 0 siendo las frecuencias de radio hasta casi el infinito siendo los rayos gamma, si despues de compararse por todas las regiones no coincide con ninguna siendo que no pertenece a ninguna region del Espectro electromagnetico.

````code
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

````


## Punto 9

En este codigo se pide que se escriba con minuscula el nombre de un pais, en los condicionales se compara nuestra variable x con cada pais de america, si en algun condicional x coincide con este el programa arroja la capital de el pais ingresado, si despues de compararse con todos los condicionales no coincide con ninguno arroja que el pais no ha sido identificado.

````code
x = input("ingerese un pais de America en minusculas: ")

if x == str("canada"):
  print("OTTAWA es la capital de" ,x)
  
elif x == str("estados unidos"):
  print("WASHINGTON.DC es la capital de" ,x)
  
elif x == str("mexico"):
  print("CIUDAD DE MEXICO es la capital de" ,x)
  
elif x == str("belice"):
  print("BELMOPAN es la capital de" ,x)
 
elif x == str("guatemala"):
  print("CIUDAD DE GUATEMALA es la capital de" ,x)
  
elif x == str("el salvador"):
  print("SAN SALVADOR es la capital de" ,x)
  
elif x == str("honduras"):
  print("TEGUCIGALPA es la capital de" ,x)
  
elif x == str("nicaragua"):
  print("MANAGUA es la capital de" ,x)
  
elif x == str("costa rica"):
  print("SAN JOSE es la capital de" ,x)
  
elif x == str("panama"):
  print("CIUDAD DE PANAMA es la capital de" ,x)
  
elif x == str("cuba"):
  print("LA HABANA es la capital de" ,x)
  
elif x == str("jamaica"):
  print("kingston es la capital de" ,x)
  
elif x == str("haiti"):
  print("PUERTO PRINCIPE es la capital de" ,x)
  
elif x == str("republica dominicana"):
  print("SANTO DOMINGO es la capital de" ,x)
  
elif x == str("bahamas"):
  print("NASSAU es la capital de" ,x)
  
elif x == str("puerto rico"):
  print("SAN JUAN es la capital de" ,x)
  
elif x == str("antigua y barbuda"):
  print("SAINT JOHN´S es la capital de" ,x)
  
elif x == str("dominica"):
  print("ROSEAU es la capital de" ,x)
  
elif x == str("san cristobal y nieves") or x == str("san cristobal"):
  print("BASSETERRE es la capital de" ,x)
  
elif x == str("santa lucia"):
  print("CASTRIES es la capital de" ,x)
  
elif x == str("san vicente y granadinas") or x == str("san vicente") or x == str("granadinas"):
  print("KINGSTOWN es la capital de" ,x)
  
elif x == str("granada"):
  print("SAINT GEORGE´S es la capital de" ,x)
  
elif x == str("barbados"):
  print("BRIDGETOWN es la capital de" ,x)
  
elif x == str("trinidad y tobago") or x == str("trinidad") or x == str("tobago"):
  print("PUERTO ESPAÑA es la capital de" ,x)
  
elif x == str("venezuela"):
  print("CARACAS es la capital de" ,x)
  
elif x == str("colombia"):
  print("BOGOTA es la capital de" ,x)
  
elif x == str("guayana"):
  print("GEORGETOWN es la capital de" ,x)
  
elif x == str("surinam"):
  print("PARAMARIBO es la capital de" ,x)
  
elif x == str("ecuador"):
  print("QUITO es la capital de" ,x)
  
elif x == str("peru"):
  print("LIMA es la capital de" ,x)
  
elif x == str("brasil"):
  print("BRASILIA es la capital de" ,x)
  
elif x == str("bolivia"):
  print("SUCRE es la capital de" ,x)
  
elif x == str("paraguay"):
  print("ASUNCION es la capital de" ,x)
  
elif x == str("chile"):
  print("SANTIAGO es la capital de" ,x)
  
elif x == str("argentina"):
  print("BUENOS AIRES es la capital de" ,x)

else:
  print("Pais no identificado")

````


## Punto 10

En este codigo se pide que se ingrese un numero real de cierta distacia en km, despues si definen las variables de cuanto equivale cada velocidad: 

- luz: velocidad de la luz en km/s

- luz2: velocidad de la luz en km/h

- sonido: velocidad del sonido en el aire en km/h

- vehiculo: velocidad max del vehiculo de produccion mas rapido del mundo, el koenigsegg jesko con una velocidad punta de 499 km/h

- bolt: la velocidad maxima registrada de Usain Bolt de 44.72 km/h

luego se arroja el resultado de la distacia x dividida por cada variable de velocidad establecida, limitada a 5 decimales a ecepcion de la velocidad de la luz en km/h, teniendo un limite de 10 decimales.

````code
x = float(input("Ingrese su distancia en km: "))

luz = float(299708)

luz2 = float(299708*3600)

sonido = float(1235.5)

vehiculo = int(499)

bolt = float(44.72)

print("tomaria" ,"{0:.5f}".format(x/luz), "segundos y" ,"{0:.10f}".format(x/luz2), "horas en recorrer" ,x,"km a la velocidad de la luz")

print("tomaria" ,"{0:.5f}".format(x/sonido), "horas en recorrer" ,x,"km a la velocidad del sonido")

print("tomaria" ,"{0:.5f}".format(x/vehiculo), "horas en recorrer" ,x,"km a la velocidad del vehiculo de produccion mas rapido del mundo")

print("tomaria" ,"{0:.5f}".format(x/bolt), "horas en recorrer" ,x,"km a la velocidad maxima de Usain Bolt")

````
### Su repectivo diagrama de flujo:

![diagrama_punto_10_taller_1](https://github.com/CJxCJ/Taller_1_Camilo_Sanchez/assets/115903431/f2beab74-b7c0-4d78-a363-5a0802ced6ce)




