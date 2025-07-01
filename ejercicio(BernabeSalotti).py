
temperaturas = [18,22,25,20,21] 
umbral = 20

def temperatura_media_alta(temperaturas: list, umbral: int)-> bool:
    """"
    funcion que recibe una lista y un valor y calcula si el promedio de la lista es mayor que el valor dado
    parametros formales:
    temperaturas(list): lista que contiene las temperaturas
    umbral(int):valor que se compara con el promedio de la lista
    retorna:
    respuesta(bool): valor booleano que retoran True si el promedio es mayor al valor umbral, False en caso de que no sea mayor
    """
    cantidad = 0 
    suma = 0
    respuesta = False
    for temperatura in temperaturas:
        suma += temperatura
        cantidad += 1
    promedio = suma/cantidad
    
    if promedio > umbral:    
        respuesta = True
    return respuesta



if temperatura_media_alta(temperaturas, umbral): # invocacion de la funcion 
    #parametros actuales: temperaturas,umbral
    print('la temperatura es mayor que el umbral')
else:
    print('la temperatura es menor que el umbral')
