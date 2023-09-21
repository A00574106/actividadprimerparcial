def suma (a,b):
  x = a + b
  return x

def resta (a,b):
  x = a - b
  return x

print ("DAME EL PRIMER NÚMERO: ")
a = float(input())
print("DAME EL SEGUNDO NÚMERO: ")
b = float(input())
print("LA SUMA DA ", suma (a,b), "Y LA RESTA DA ", resta (a,b))

__________________________________________________________________________________________________________________

def multiplicacion():
  x = a * b
  return x

def division():
  x = a/b
  return x

a = float(input("DAME TU PRIMER NÚMERO: "))
b = float(input("DAME TU SEGUNDO NÚMERO: "))

print("EL RESULTADO DE TU MULTIPLICACIÓN ES ", multiplicacion(), "Y DE LA DIVISIÓN ES:", division())

__________________________________________________________________________________________________________________

def conversion():
  x = a *(1000/1.0)
  return x

a = float(input("DAME LOS KM: "))

print("LA CONVERSIÓN DE", a, "A METROS ES : ", conversion())

__________________________________________________________________________________________________________________
def area_triangulo():
  x = (base*altura)/2
  return x

altura = float(input("DAME LA ALTURA DE TU TRIÁNGULO: "))
base = float(input("DAME LA BASE DE TU TRIÁNGULO: "))

print("EL ÁREA DE TU TRIÁNGULO ES: ", area_triangulo())
