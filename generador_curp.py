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

def verificar_datos(dato,caso):
  match caso:
    case 1:
      if len(dato) >=3:
        return dato
      else:
        dato = input('Nombre no válido, intenta de nuevo:')
        return verificar_datos(dato,1)
    case 2:
        if len(dato) >=3:
          return dato
        else:
          dato = input('Apellido no válido, intenta de nuevo:')
          return verificar_datos(dato,2)
    case 3:
        if len(dato) >=3 or dato == 'x':
            return dato
        else:
            dato = input('Apellido no válido, intenta de nuevo. \nRecuerda en caso de no contar con este ingresa x:')
            return verificar_datos(dato,3)
        
def ingresar_datos():
    datos_usuario = []
    nombre = input('Ingresa tu(s) nombre(s):')
    nombre = verificar_datos(nombre,1)
    datos_usuario.append(nombre) 
    apellido_p = input('Ingresa tu primer apellido:')
    apellido_p = verificar_datos(apellido_p,2)
    datos_usuario.append(apellido_p)
    appelido_m = input('Ingresa tu segundo apellido, en caso de no contar con este ingresa x:')
    appelido_m = verificar_datos(appelido_m,3)
    datos_usuario.append(appelido_m)
    datos_usuario = [nombre,apellido_p,appelido_m]
    return datos_usuario
    
def generar_curp():
  print('¡Bienvenid@ al generador de CURP!')
  datos_usuario= ingresar_datos()
  print(datos_usuario)

generar_curp()