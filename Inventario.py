# Vamos a diseñar un programa donde nos ayude a inventariar los productos en una tienda
#comenzamos declarando las variables

# Inicializamos variables
precio = 0
cantidad = 0
costo_total = 0

# Pedimos el nombre del producto, asegurándonos que no quede vacío
while True:
    nombre_de_producto = input("Ingrese el nombre del producto: ").strip()
    if nombre_de_producto:
        break
    else:
        print("El nombre del producto no puede estar vacío. Intente de nuevo.")

# Pedimos la cantidad del producto, asegurándonos que sea un entero positivo
while True:
    try:
        cantidad = int(input("Ingrese la cantidad del producto: "))
        if cantidad > 0:
            break
        else:
            print("La cantidad debe ser mayor a 0.")
    except ValueError:
        print("La cantidad ingresada es inválida. Debe ser un número entero.")

# Pedimos el precio del producto, asegurándonos que sea un número positivo
while True:
    try:
        precio = float(input("Ingrese el precio del producto: "))
        if precio > 0:
            break
        else:
            print("El precio debe ser mayor a 0.")
    except ValueError:
        print("El precio ingresado es inválido. Debe ser un número.")

# Calculamos el costo total
costo_total = cantidad * precio

# Mostramos resumen
print("\n======= Resumen del inventario =======")
print("Producto:       ", nombre_de_producto)
print("Cantidad:       ", cantidad)
print("Precio unitario:", precio)
print("Total a pagar:  ", costo_total)