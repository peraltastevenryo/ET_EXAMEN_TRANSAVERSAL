'''
FUNCIONES
'''

marcas = ['HP', 'ACER', 'ASUS', 'DELL']

productos = {'8475HD': {'marca': 'HP', 'pantalla': 15.6, 'ram': '8GB', 'disco': 'DD', 'almacenamiento': '1T', 'procesador': 'Intel Core i7', 'video': 'Nvidia GTX1050'},
            '2175HD': {'marca': 'ACER', 'pantalla': 14, 'ram': '4GB', 'disco': 'SSD', 'almacenamiento': '512GB', 'procesador': 'Intel Core i7', 'video': 'Nvidia GTX1050'},
            'JjfFHD': {'marca': 'ASUS', 'pantalla': 14, 'ram': '16GB', 'disco': 'SSD', 'almacenamiento': '256GB', 'procesador': 'Intel Core i5', 'video': 'Nvidia RTX2080Ti'},
            'fgdxFHD': {'marca': 'HP', 'pantalla': 15.6, 'ram': '12GB', 'disco': 'DD', 'almacenamiento': '1T', 'procesador': 'Intel Core i5', 'video': 'integrada'},
            'GF75HD': {'marca': 'ASUS', 'pantalla': 15.6, 'ram': '12GB', 'disco': 'DD', 'almacenamiento': '1T', 'procesador': 'Intel Core i3', 'video': 'Nvidia GTX1050'},
            '123FHD': {'marca': 'ACER', 'pantalla': 14, 'ram': '6GB', 'disco': 'DD', 'almacenamiento': '1T','procesador':  'AMD Ryzen 7', 'video': 'integrada'},
            '342FHD': {'marca': 'ACER', 'pantalla': 15.6, 'ram': '8GB', 'disco': 'DD','almacenamiento': '1T', 'procesador': 'AMD Ryzen 5', 'video': 'Nvidia GTX1050'},
            'UWU131HD': {'marca': 'DELL', 'pantalla': 15.6, 'ram': '8GB', 'disco': 'DD', 'almacenamiento': '1T', 'procesador': 'AMD Ryzen 5', 'video': 'Nvidia GTX1050'}
}

stock = {'8475HD': {'precio': 387990, 'stock': 10}, '2175HD': {'precio': 327990, 'stock': 4}, 'JjfFHD': {'precio': 424990, 'stock': 1},
        'fgdxFHD': {'precio': 664990, 'stock': 21}, '123FHD': {'precio': 290890, 'stock': 32}, '342FHD': {'precio': 444990, 'stock': 7},
        'GF75HD': {'precio': 749990, 'stock': 2}, 'UWU131HD': {'precio': 349990, 'stock': 1}, 'FS1230HD': {'precio': 249990, 'stock': 0}
}

# Funcion stock por marca

def stock_marca(productos, stock, marcas):
    
    stock_total = 0
    
    print("\n*** MARCAS ***")
    for i in marcas:
        print(i)
        
        
    user_marca = input("Ingrese marca a consultar: ").upper()
    
    if user_marca not in marcas:
        print("La marca ingresada no se encuentra registrada!")
            
    else:
        for modelo in productos:
            
            if modelo in stock and (productos[modelo]['marca'] == user_marca):
                stock_total += stock[modelo]['stock']
                
        print(f"El stock disponible es de {stock_total}")  
    
    
# Busqueda por precio

def busqueda_precio(stock, productos):
    
    try:
        min_precio = int(input("Ingrese precio minimo: "))
        
        max_precio = int(input("Ingrese precio maximo: "))
        
    except ValueError:
        print("Debe ingresar un valor numerico! Volviendo al menu principal....")
        return
    
    print("*** MODELOS DISPONIBLES ***")
    
    for modelo in productos:
        
        if (stock[modelo]['precio'] >= min_precio and
            stock[modelo]['precio'] <= max_precio):
            
            marca = productos[modelo]['marca']
            
            print(f"{marca} -- {modelo}")

    return

# Listado de productos

def ordenar_productos(productos):
    for modelo in productos:
        print(f"{productos[modelo]['marca']} - {modelo} - {productos[modelo]['ram']} - {productos[modelo]['almacenamiento']}")

def main():

    while True:
        
        print("\n----- MENU -----")
        print("1. Stock marca.")    
        print("2. Búsqueda por precio.")
        print("3. Listado de productos.")
        print("4. Salir.")
        
        try:
            user_opc = int(input("\nIngrese una opción: "))
        
        except ValueError:
            print("Debe ingresar un valor numerico!")
        
        if user_opc == 1:
            stock_marca(productos, stock, marcas)
        
        elif user_opc == 2:
            busqueda_precio(stock, productos)
        
        elif user_opc == 3:
            ordenar_productos(productos)
        
        elif user_opc == 4:
            print("Programa finalizado....")
            break
        
        else:
            print("Debe ingresar una opcion válida!")
    

if __name__ == "__main__":
    main()
    