def calculadora_inutil(): #creé la función
  print("Dime un número que será la base") #le pido al usuario el número base
  base = input() 

  print("Dame otro número y será tu exponencial") #le pido al usuario el exponencial
  exponente = input()

  operacion = int(base) ** (1/int(exponente)) #desplegué mi resultado / hice la operación

  print("El resultado incorrecto de tu operación es", operacion) #ejecuté la función

calculadora_inutil()
