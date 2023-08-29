# Menu opciones
#1.Ingresar un producto en la bodega 
#2.Verificar un producto en la bodega
#3.Buscar un producto en la bodega
#4.Editar un produco en la bodega 
#5.Retirar un producto bodega
#6.Si el usuario digita 6 salir 

#producto:nombre,codigo,descripcion,foto,precio,cantidadEnBodega,fechaEntradaBodega
opcion=0
print("TIENDA EL GANGAZO")
print("*******************************")
print(" Menu opciones")
print("1.Ingresar un producto en la bodega")
print("2.Verificar un producto en la bodega")
print("3.Buscar un producto en la bodega") # codigo a  buscar con un if para que recorra la lista  y ponerle condicionales 
print("4.Editar un produco en la bodega ")
print("5.Retirar un producto bodega")
print("6.Si el usuario digita 6 salir ")

productos = []


while opcion !=6:
    
    producto ={}
    opcion=int(input("Digita la opcion deseada: "))
    if opcion ==1:
        producto["nombre"]=input("Digita el nombre del producto: ")
        producto["codigo"]=int(input("Digita el codifo del producto : "))
        producto["descripcion"]=input("Digita la descripcion del producto : ")
        producto["foto"]=input("Digita la url del producto: ")
        producto["cantidadEnBodega"]=input("Digita el stock del producto: ")
        producto["fechaEntradaBodega"]=input("Digita  la fecha de entrada del producto: ")
        productos.append(producto)
        
    elif opcion ==2:

        for productoSeleccionado in productos:
            print(f"nombre: {productoSeleccionado['nombre']}")
            print(f"codigo:{productoSeleccionado['codigo']}")
            print(f"descripcion:{productoSeleccionado['descripcion']}")
            print(f"foto:{productoSeleccionado['foto']}")
            print(f"cantidadEntradaBodega:{productoSeleccionado['cantidadEntradaBodega']}")
            print(f"fechaEntrada:{productoSeleccionado['fechaEntrada']}")
    
    elif opcion ==3:
        pass
    elif opcion ==4:
        pass
    elif opcion ==5:
        pass
    elif opcion ==6:
        print("Opcion invalida, digita una opcion correcta: ")
        
# la lista va por fuera para que me guarde y el diccionario va por dentro para que me deje ingresar valores 