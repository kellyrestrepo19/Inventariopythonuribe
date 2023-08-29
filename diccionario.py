productoTerminadoUno={
    'referencia':5087,
    'marca':"americanino",
    'descripcion':"chompa de acampar",
    'color':"naranja",
    'costoUnitario': 100000,
    'desponibleBodega':True,
    'costoVenta': 850000,
    'puntosVenta':['cc mayorca', 'terminal norte', 'puerta del norte', 'centro de la moda']
}



productoTerminadoDos={
    'referencia':5088,
    'marca':"americanino",
    'descripcion':"camiseta polo",
    'color':"oscura",
    'costoUnitario': 30000,
    'desponibleBodega':True,
    'costoVenta': 150000,
    'puntosVenta':['cc mayorca', 'terminal norte', 'puerta del norte', 'centro de la moda']
}
# los arreglos y las listas se escriben en plural 
# CREANDO UNA LISTA DE DICCIONARIO
productos= [productoTerminadoUno,productoTerminadoDos]

#RECORRRIENDO UNA LISTA CON CILO FOR 
#dentro de ,os parentesis se dice de donde a donde se quiere ir, cuando se cuanto necesiro 
'''for contador in range(1,10, 2):
    print(contador)'''
    
    
for producto in productos:
    for puntoVenta in producto["puntosVenta"]:
        print(puntoVenta)
     