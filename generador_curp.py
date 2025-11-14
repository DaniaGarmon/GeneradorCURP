"""
Problema : Encontrar CURP de acuerdo a datos ingresados por el Usuario
Autor: Dania Garcia Montiel
email: aspirante02_a26@cic.ipn.mx
"""

#Variables
apellido_p = None
appelido_m = None
nombre = None
fecha_nacimiento = None
sexo = None
lugar_nacimiento = None
datos_usuario= None
continuar = True
contador = 0

#Constantes
Vocales = ['a','e','i','o','u']
Cat_sexo = ['H','M']
Cat_entidades = {
    "AGUASCALIENTES":"AS",
    "BAJA CALIFORNIA":"BC",
    "BAJA CALIFORNIA SUR":"BS",
    "CAMPECHE":"CC",
    "COAHUILA":"CL", 
    "COLIMA": "CM",
    "CHIAPAS": "CS", 
    "CHIHUAHUA": "CH",
    "DISTRITO": "FEDERAL",
    "DF DURANGO": "DG",
    "GUANAJUATO": "GT",
    "GUERRERO": "GR",
    "HIDALGO":"HG",
    "JALISCO":"JC",
    "MÉXICO": "MC",
    "MICHOACÁN": "MN",
    "MORELOS": "MS",
    "NAYARIT" :"NT",
    "NUEVO LEÓN": "NL",
    "OAXACA":"OC",
    "PUEBLA":"PL",
    "QUERÉTARO":"QT",
    "QUINTANA ROO": "QR",
    "SAN LUIS POTOSÍ" :"SP",
    "SINALOA" :"SL",
    "SONORA" :"SR",
    "TABASCO":"TC",
    "TAMAULIPAS":"TS",
    "TLAXCALA":"TL", 
    "VERACRUZ":"VZ",
    "YUCATÁN":"YN",
    "ZACATECAS":"ZS",
    "NACIDO EN EL EXTRANJERO":"NE"
}

def verificar_dia_nacimiento(dia, mes, anio):
  g_30 = [4,6,9,11]
  g_31 = [1,3,5,7,8,10,12]
  if mes in g_30:
    if 1 <= dia <= 30:
      return True
    else:
      return False
  if mes in g_31:
    if 1 <= dia <= 31:
      return True
    else:
      return False
  if mes == 2:
    if anio % 4 == 0 and anio % 100 != 0:
      if 1 <= dia <= 29:
        return True
      else:
        return False
    elif anio % 4 != 0:
      if 1 <= dia <= 28:
        return True
      else:
        return False
    elif anio % 100 == 0 and anio % 400 != 0:
      if 1 <= dia <= 28:
        return True
      else:
        return False
    elif anio % 400 == 0:
      if 1 <= dia <= 29:
        return True
      else:
        return False



def verificar_datos(dato,caso, mes=None, anio=None):
  global contador
  match caso:
    case 1:
      if len(dato) >=3:
        contador = 0
        return dato.upper()
      else:
        contador += 1
        if contador == 1 or contador == 2:
          dato = input('Nombre no válido, intenta de nuevo:')
          return verificar_datos(dato,1)
        else:
          intentar = input('Nombre no válido. ¿Quieres volver a intentarlo? Escribe y/Y para continuar, de lo contrario escribe cualquier otra letra: ')
          if intentar == 'Y' or intentar == 'y':
            contador = 0
            dato = input('Ingresa tu(s) nombre(s):')
            return verificar_datos(dato,1)
          else:
            return None        
    case 2:
        if len(dato) >=3:
          contador = 0
          return dato.upper()
        else:
          contador += 1
          if contador == 1 or contador == 2:
            dato = input('Apellido no válido, intenta de nuevo:')
            return verificar_datos(dato,2)
          else:
            intentar = input('Apellido no válido. ¿Quieres volver a intentarlo? Escribe y/Y para continuar, de lo contrario escribe cualquier otra letra: ')
            if intentar == 'Y' or intentar == 'y':
              contador = 0
              dato = input('Ingresa tu apellido paterno : ')
              return verificar_datos(dato,2)
            else:
              return None 
    case 3:
        if len(dato) >=3 or dato == 'x' or dato == 'X':
            contador = 0
            return dato.upper()
        else:
            contador += 1
            if contador == 1 or contador == 2:
              dato = input('Apellido no válido, intenta de nuevo. \nRecuerda en caso de no contar con este ingresa x: ')
              return verificar_datos(dato,3)
            else:
              intentar = input('Apellido no válido. ¿Quieres volver a intentarlo? Escribe y/Y para continuar, de lo contrario escribe cualquier otra letra: ')
              if intentar == 'Y' or intentar == 'y':
                contador = 0
                dato = input('Ingresa tu apellido materno. \nRecuerda en caso de no contar con este ingresa x: ')
                return verificar_datos(dato,3)
              else:
                return None 
    case 4:
      if 1900 <= dato <= 2025:
        contador = 0
        return dato
      else:
        contador += 1
        if contador == 1 or contador == 2:
          print('Año no válido, intenta de nuevo:')
          dato = int(input())
          return verificar_datos(dato,4)
        else:
          intentar = input('Año de nacimiento no válido. ¿Quieres volver a intentarlo? Escribe y/Y para continuar, de lo contrario escribe cualquier otra letra: ')
          if intentar == 'Y' or intentar == 'y':
            contador = 0
            dato = int(input('Ingresa tu año de nacimiento: '))
            return verificar_datos(dato,4)
          else:
            return None   
    case 5:
      if 1 <= dato <= 12:
        if anio == 2025 and dato !=11 and dato !=12:
          return dato
        elif anio == 2025 and (dato ==11 or dato ==12):
          print('El sistema solo admite fechas hasta el 31 de Octubre de 2025')
          return dato
        else:
          return dato
      else:
        dato = int(input('Mes no válido, intenta de nuevo:'))
        return verificar_datos(dato,5)
    case 6:
      checar_dia =verificar_dia_nacimiento(dato,mes,anio)
      if checar_dia:
        return dato
      else:
        dato = int(input('Día no válido, intenta de nuevo:'))
        return verificar_datos(dato,6,mes,anio)


        

def ingresar_fecha():
  fecha_nacimiento = []
  anio = int(input('Ingresa el año de tu nacimiento: '))
  anio = verificar_datos(anio,4)
  mes = int(input('Ingresa el mes de tu nacimiento en número, ejemplo: \nSi naciste en el mes de Noviembre ingresa el número 11: '))
  mes = verificar_datos(mes,5,None,anio)
  dia = int(input('Ingresa el día de tu nacimiento: '))
  dia = verificar_datos(dia,6,mes,anio)
  fecha_nacimiento.append(anio)
  fecha_nacimiento.append(mes)
  fecha_nacimiento.append(dia)
  return fecha_nacimiento
        
def ingresar_datos():
    datos_usuario = []
    nombre = input('Ingresa tu(s) nombre(s):')
    nombre = verificar_datos(nombre,1)
    if nombre != None:
      datos_usuario.append(nombre) 
    else: 
      return None
    apellido_p = input('Ingresa tu primer apellido:')
    apellido_p = verificar_datos(apellido_p,2)
    datos_usuario.append(apellido_p)
    appelido_m = input('Ingresa tu segundo apellido, en caso de no contar con este ingresa x:')
    appelido_m = verificar_datos(appelido_m,3)
    datos_usuario.append(appelido_m)
    fecha_nacimiento = ingresar_fecha()
    datos_usuario = [nombre,apellido_p,appelido_m, fecha_nacimiento]
    return datos_usuario
    
def generar_curp():
  print('¡Bienvenid@ al generador de CURP!')
  while continuar:
    datos_usuario= ingresar_datos()
    if datos_usuario is None:
      print('Nos vemos a la próxima!!')
      break
    print(datos_usuario)
    break

generar_curp()