x = input("escriba una letra: ")
y = ord(x)

if y == 65 or y == 69 or y == 73 or y == 79 or y == 85 or y == 97 or y == 101 or y == 105 or y == 111 or y == 117:
  print(x, "es una vocal")
  
else:
  print(x, "es una consonante")