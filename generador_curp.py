"""
Problema : Encontrar CURP de acuerdo a datos ingresados por el Usuario
Autor: Dania Garcia Montiel
email: aspirante02_a26@cic.ipn.mx
"""

#Variables
contador = 0
continuar = True

#Constantes
Cat_entidades = {
    "AGUASCALIENTES":"AS",
    "BAJA CALIFORNIA":"BC",
    "BAJA CALIFORNIA SUR":"BS",
    "CAMPECHE":"CC",
    "COAHUILA":"CL", 
    "COLIMA": "CM",
    "CHIAPAS": "CS", 
    "CHIHUAHUA": "CH",
    "CIUDAD DE MÉXICO": "DF",
    "DURANGO": "DG",
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
Cat_sexo = ['H','M','X']
Vocales = ['A','E','I','O','U']

def seleccionar_estado_nacimiento():
  global Cat_entidades
  print('Cátalogo de entidades:')
  for estado, clave in Cat_entidades.items():
    print(f'{estado} - {clave}')
  print('---------------------------------')
  estado = input('Ingresa el código del estado donde naciste. Por ejemplo, si naciste en Tlaxcala, ingresa "TL": ').upper()
  if estado in Cat_entidades.values():
    return estado
  else:
    print('Estado no válido, intenta de nuevo.')
    print('---------------------------------')
    return seleccionar_estado_nacimiento()

def verificar_dia_nacimiento(dia, mes, anio):
  """
  Función para verificar que el día de nacimiento sea válido.
  """
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
  """
  Función para verificar que los datos ingresados sean correctos.
  """
  global contador
  match caso:
    case 1:
      if len(dato) >=3:
        contador = 0
        dato = dato.upper()
        dato = [d for d in dato]
        return dato
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
          dato = dato.upper()
          dato = [d for d in dato]
          return dato
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
            dato = dato.upper()
            dato = [d for d in dato]
            return dato
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
          return None
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
  """
  Función para ingresar la fecha de nacimiento del usuario.
  """
  fecha_nacimiento = []
  anio = int(input('Ingresa el año de tu nacimiento: '))
  anio = verificar_datos(anio,4)
  mes = int(input('Ingresa el mes de tu nacimiento en número, ejemplo: \nSi naciste en el mes de Noviembre ingresa el número 11: '))
  mes = verificar_datos(mes,5,None,anio)
  if mes is None:
    return None
  dia = int(input('Ingresa el día de tu nacimiento: '))
  dia = verificar_datos(dia,6,mes,anio)
  anio_digitos = [int(d) for d in str(anio)]
  anio_digitos = anio_digitos[2:5]
  anio_digitos = ''.join(map(str,anio_digitos))
  mes = str(mes).zfill(2)
  dia = str(dia).zfill(2)
  fecha_nacimiento.append(anio_digitos)
  fecha_nacimiento.append(mes)
  fecha_nacimiento.append(dia)
  return fecha_nacimiento

def seleccionar_sexo():
  global Cat_sexo
  sexo = int(input('Selecciona tu sexo: \nSi eres Mujer ingresa 1 \nSi eres Hombre ingresa 2 \nSi eres No Binario ingresa 3: '))
  if sexo == 1:
    return Cat_sexo[1]
  elif sexo == 2:
    return Cat_sexo[0]
  elif sexo == 3:
    return Cat_sexo[2]
  else:
    print('Opción no válida, intenta de nuevo.')
    return seleccionar_sexo()
      
def ingresar_datos():
    """
    Función para que el usuario ingrese sus datos, y validar que sean correctos.
    """
    nombre = input('Ingresa tu(s) nombre(s):')
    nombre = verificar_datos(nombre,1)
    if nombre is None:
      return None
    apellido_p = input('Ingresa tu primer apellido:')
    apellido_p = verificar_datos(apellido_p,2)
    if apellido_p is None:
      return None
    appelido_m = input('Ingresa tu segundo apellido, en caso de no contar con este ingresa x:')
    appelido_m = verificar_datos(appelido_m,3)
    if appelido_m is None:
      return None
    fecha_nacimiento = ingresar_fecha()
    if fecha_nacimiento is None:
      return None
    sexo = seleccionar_sexo()
    edo_nacimiento = seleccionar_estado_nacimiento()
    datos_usuario = {
      'nombre':nombre,
      'apellido_p':apellido_p,
      'apellido_m':appelido_m,
      'fecha_nacimiento':fecha_nacimiento,
      'sexo':sexo,
      'edo_nacimiento':edo_nacimiento
    }
    return datos_usuario
  
def seleccionar_letras_apellido_p(apellido_p):
  """
  Función para selecionar las letras del apellido paterno que se van a usar en la CURP.
  """
  global Vocales
  primer_letra = apellido_p[0]
  apellido_p = apellido_p[1:]
  primera_vocal = None
  for letra in apellido_p:
    if letra in Vocales:
      primera_vocal = letra
      break
  primera_consonante = None
  for letra in apellido_p:
    if letra not in Vocales:
      primera_consonante = letra
      break
  letras_apellido_p = [primer_letra,primera_vocal,primera_consonante]
  return letras_apellido_p

def seleccionar_letras_apellido_m(apellido_m):
  """
  Función para selecionar las letras del apellido materno que se van a usar en la CURP.
  """
  global Vocales
  if 'X' in apellido_m:
    return ['X','X']
  primera_letra = apellido_m[0]
  apellido_m = apellido_m[1:]
  primera_consonante = None
  for letra in apellido_m:
    if letra not in Vocales:
      primera_consonante = letra
      break
  return [primera_letra,primera_consonante]

def checar_nombres_compuestos(nombre):
  """
  Función para evaluar si el nombre es compuesto.
  En la CURP si el nombre es compuesto con María o José, se va a evaluar el otro nombre.
  """
  nombres_compuestos_validar = ['MARÍA','MARIA','JOSE','JOSÉ']
  if ' ' in nombre:
    indice= nombre.index(' ')
    nombre_compuesto = nombre[:indice]
    nombre_compuesto = ''.join(nombre_compuesto)
    if nombre_compuesto in nombres_compuestos_validar:
      return nombre[indice+1:]
    else:
      return nombre
  else:
    return nombre

def seleccionar_letras_nombre(nombre):
  """
  Función para selecionar las letras del nombre que se van a usar en la CURP.
  """
  global Vocales
  nombre = checar_nombres_compuestos(nombre)
  primera_letra = nombre[0]
  nombre = nombre[1:]
  consonante_interna = None
  for letra in nombre:
    if letra not in Vocales:
      consonante_interna = letra
      break
  return [primera_letra,consonante_interna]

def verificar_palabra_altisonante(palabra):
  """
  Función para verificar que no se generar palabras curiosas/altisonantes al juntar los datos ingresados.
  """
  palabras_reservadas = ['VACA','COLA','PENE','PUTO','MULA','JOTO','CACA','RATA']
  if palabra in palabras_reservadas:
    return True
  else:
    return False
 
def generar_curp():
  """
  Función para generar CURP a partir de los datos ingresados del usuario.
  """
  print('¡Bienvenid@ al generador de CURP!')
  while continuar:
    datos_usuario= ingresar_datos()
    if datos_usuario is None:
      print('Nos vemos a la próxima!!')
      break
    letras_apellido_p= seleccionar_letras_apellido_p(datos_usuario['apellido_p'])
    letras_apellido_m = seleccionar_letras_apellido_m(datos_usuario['apellido_m'])
    letras_nombre = seleccionar_letras_nombre(datos_usuario['nombre'])
    curp = [letras_apellido_p[0],
            letras_apellido_p[1],
            letras_apellido_m[0],
            letras_nombre[0],
            datos_usuario['fecha_nacimiento'][0],
            datos_usuario['fecha_nacimiento'][1],
            datos_usuario['fecha_nacimiento'][2],
            datos_usuario['sexo'],
            datos_usuario['edo_nacimiento'],
            letras_apellido_p[2],
            letras_apellido_m[1],
            letras_nombre[1],
            'XX']
    palabra_verificar = curp[0:4]
    palabra_verificar = ''.join(palabra_verificar)
    palabra_altisonante = verificar_palabra_altisonante(palabra_verificar)
    if palabra_altisonante:
      curp[1] = 'X'
    curp = ''.join(curp)
    print('\n')
    print(f'Clave Única de Registro de Población (CURP): {curp}')
    break

def main():
    generar_curp()

if __name__ == '__main__':
    main()