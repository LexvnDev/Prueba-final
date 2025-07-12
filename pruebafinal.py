productos ={"8475HD":["HP",15.6,"8GB","DD","IT","Intel Core i5","Nvidia GTX1050"],
"2175HD":["Lenovo", 14,"4GB","SSD","512GB","Intel Core i5","Nvidia GTX1050"],
"JjfFHD":["Asus",14,"16GB","SSD","256","Intel Core i7","Nvidia RTX2080Ti"],
}

stock = {"8475HD":[387990,10],"2175HD":[327990,4],"JjfFHD":[424990,1]
}

def stock_marca(marca):
    
    while True:
        for modelo, indice in productos.items():
            if indice[0].lower() == marca and modelo in stock:
                print(f"el stock es: {stock[modelo][1]}")
        break
    
def busqueda_precio(p_min, p_max):
    resultados = []
    for modelo, (precio, cantidad) in stock.items():
        if p_min <= precio <= p_max and cantidad > 0:
            marca = productos[modelo][0]
            resultados.append(f"{marca}-{modelo}")
        if resultados:
            resultados.sort()
            for i in resultados:
                print(i)
            else:
                print("No hay notebooks en ese rango de precios")

def actualizar_precio(modelo, p):
    if modelo in stock:
        stock[modelo][0] = p
        print("precio actualizado")
    else:
        print("El modelo no existe!!")
    
    respuesta = input("Desea actualizar otro precio (s/n)?: ")
    if respuesta.lower() == si:
        nuevo_modelo = input("ingrese el modelo a")

def menu():

    while True:
        print("\n"
            "\n 1: StocK Marca"
            "\n 2: Busqueda por precio"
            "\n 3: Actualizar Precio"
            "\n 4: Salir")
    
        try:
            op = int(input("Ingrese una Opcion: "))
        except ValueError:
            print("Ingrese un numero valido")
        
        else:
    
            if op == 1: 
                 marca = input("Ingrese marca a consultar: ").lower().strip()
                 stock_marca(marca)
            elif op == 2:
                p_min = int(input("Ingrese precio minimo: "))
                p_max = int(input("Ingrese precio maximo: "))
                busqueda_precio(p_min, p_max)

            elif op == 3:
                print("opcion 3")
                modelo = input("ingrese modelo a actualizar: ")
                p = int(input("Ingrese Precio nuevo: "))
            elif op == 4:
                print("Programa finalizado")
                break
            else:
                print("Debe seleccionar una Opcion valida")

print("***Menu Principal***")
menu()