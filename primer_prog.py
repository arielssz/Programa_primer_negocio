#Nombre:Erick Chancusig
#Curso: 1ro "A"

def sumar_factura(*valores):
    return sum(valores)

def agregar_a_factura(lista_productos, **producto):
     return lista_productos + f"- {producto['orden']} (${producto['valor']})"
factura = 0
lista_productos = ""
salir = 0

while salir == 0:
    print("--- Bienvenido, seleccione su pedido ---")
    print("1. Crepas")
    print("2. Bebidas")
    print("3. Postres")
    print("4. Salir de LaCrepería")
    print("--------------------------------------")
    menu = int(input("Seleccione una opción: "))
    orden = ""
    valor = 0
    if menu == 1:
        print("--- Menú de Crepas ------------------")
        print("1. Crepa de nutella con fresas 3$")
        print("2. Crepa de chocolate 3.50$")
        print("3. Crepa de nutella con plátano 3.25$")
        print("4. Crepa de dulce de leche 3.75$")
        print("5. Crepa de crema batida con frutas 4$")
        print("6. Salir al menú principal")
        opcion = int(input("Seleccione una opción: "))
        if opcion == 1:
            orden = "Crepa de nutella con fresas"
            valor = 3
        elif opcion == 2:
            orden = "Crepa de chocolate"
            valor = 3.50
        elif opcion == 3:
            orden = "Crepa de nutella con plátano"
            valor = 3.25
        elif opcion == 4:
            orden = "Crepa de dulce de leche"
            valor = 3.75
        elif opcion == 5:
            orden = "Crepa de crema batida con frutas"
            valor = 4
        elif opcion == 6:
            print("Regresando al menú principal")
        else:
            print("Error: opción no válida")
    elif menu == 2:
        print("--- Menú de Bebidas ------------------")
        print("1. Café 1.25$")
        print("2. Smoothies 2$")
        print("3. Frappes 3$")
        print("4. Salir al menú principal")
        opcion = int(input("Seleccione una opción: "))
        if opcion == 1:
            orden = "Café"
            valor = 1.25
        elif opcion == 2:
            orden = "Smoothies"
            valor = 2
        elif opcion == 3:
            orden = "Frappes"
            valor = 3
        elif opcion == 4:
            print("Regresando al menú principal")
        else:
            print("Error: opción no válida")
    elif menu == 3:
        print("--- Menú de Postres ------------------")
        print("1. Cupcakes 1$")
        print("2. Pastel 1.50$")
        print("3. Helados 0.75$")
        print("4. Pastel de tres leches 1.25$")
        print("5. Mousse de maracuyá 3.50$")
        print("6. Salir al menú principal")
        opcion = int(input("Seleccione una opción: "))
        if opcion == 1:
            orden = "Cupcakes"
            valor = 1
        elif opcion == 2:
            orden = "Pastel"
            valor = 1.50
        elif opcion == 3:
            orden = "Helados"
            valor = 0.75
        elif opcion == 4:
            orden = "Pastel de tres leches"
            valor = 1.25
        elif opcion == 5:
            orden = "Mousse de maracuyá"
            valor = 3.50
        elif opcion == 6:
            print("Regresando al menú principal")
        else:
            print("Error: opción no válida")
    elif menu == 4:
        salir = 1
        print("Saliendo del programa, ¡Gracias por preferir LaCrepería!")
    else:
        print("Error: opción no válida")
    if orden != "":
        factura = sumar_factura(factura, valor)
        lista_productos = agregar_a_factura(lista_productos, orden=orden, valor=valor)
        print("------------------------------------------------------")
        print("Has seleccionado:", orden)
        print("Por un valor de:", valor, "$")
        print("Su factura es:", factura, "$")
        print("¿Desea agregar más productos a su carrito?")
        print("1. Agregar más productos")
        print("2. Finalizar compra")
        agregacion = int(input("Seleccione una opción: "))
        if agregacion == 1:
            print("Producto agregado correctamente.")
            print("Detalle actual:")
            print(lista_productos)
            print("Factura actual:", factura, "$")
        elif agregacion == 2:
            salir = 1
            print("Finalizando compra!")
            print("Detalle:")
            print(lista_productos)
            print("El valor a pagar es de", factura, "$")
            print("Gracias por su compra")
        else:
            print("Opción no válida, regresando al menú principal.")