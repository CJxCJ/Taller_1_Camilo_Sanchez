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