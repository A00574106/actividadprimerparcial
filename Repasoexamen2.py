def conversor_de_temperatura():
  print("Ingresa la temperatura en C°")
  celsius = input()

  fahrenheit = int(celsius) * 9/5 +32
  kelvin = int(celsius) + 273
  print("De grados C° a fahrenheit es", fahrenheit,"y en kelvin es", kelvin)

conversor_de_temperatura()
