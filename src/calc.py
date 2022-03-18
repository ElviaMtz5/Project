def convertir_fracciones(entrada):
  numero = 0
  try:
    if(isinstance(entrada,str)):
      print(entrada)
      if "/" in entrada :
        arr = entrada.split("/")
        numerador = arr[0]
        denominador = arr[1]
        #print(arr)
        numero = float(numerador) / float(denominador)
        #print(arr, numero)
      else:
        numero = float(entrada)
        print(type(numero))
      
    if(isinstance(entrada,int) or  isinstance(entrada,float)):
      numero = entrada
  except:
    print("Error de formato de numero")
    
  return numero

def suma(a,b):
  sumando_a = convertir_fracciones(a)
  sumando_b = convertir_fracciones(b)
  return sumando_a + sumando_b

def resta(a,b):
  minuendo = convertir_fracciones(a)
  sustraendo = convertir_fracciones(b)
  return minuendo - sustraendo

def multiplicacion(a,b):
  mult_a = convertir_fracciones(a)
  mult_b = convertir_fracciones(b)
  return mult_a * mult_b

def division(a,b):
  numerador = convertir_fracciones(a)
  denominador = convertir_fracciones(b)
  if(denominador == 0):
    raise Exception("Error: el denominador no puede ser 0")
  else:
    return numerador / denominador
