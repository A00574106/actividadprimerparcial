def calculadora(): #hacer mi función
  print("Dame la longitud del rectángulo")  #le pdio al usuario los números
  longitud = input() #input para que el usuario ponga el número
  print("Dame la anchura del rectángulo")
  anchura=input()
  
  operacion = int(longitud) * int(anchura) #hago mi operación, indicando que las variables son números

  print("El área de tu rectángulo es", operacion) #despliego mi operación

calculadora() 
