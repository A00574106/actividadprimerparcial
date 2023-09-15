def examen2():
  cantidadA = float(input("Ingrese la cantidad de aluminio: "))
  precioA = float(input("Ingrese el precio unitario del aluminio: "))
  aluminio = precioA * cantidadA

  cantidadC = float(input("Ingrese la cantidad de conectores: "))
  precioC = float(input("Ingrese el precio unitario de los conectores: "))
  conectores = precioC * cantidadC

  cantidadCA = float(input("Ingrese la cantidad de cajas: "))
  precioCA = float(input("Ingrese el precio unitario de cada caja: "))
  cajas = precioCA * cantidadCA

  total = float(aluminio) + float(conectores) + float(cajas)

  print("Tu costo total es: ", total)

  descuento = total * 5/100

  final = total - descuento
  
  print("Tu costo final con el descuento del 5% es: ", final)
  
examen2() 
