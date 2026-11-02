"""1. El programa deberá contar con un menú de productos almacenado en un diccionario,
donde cada producto tenga asociado su precio. El menú deberá contener al menos seis productos.
2. Al iniciar, el programa deberá solicitar el nombre del cliente y mostrar un saludo personalizado.
3. El programa deberá presentar al usuario un menú de opciones que se repita hasta que el usuario decida salir. 
Las opciones mínimas serán:
a. Ver el menú de productos con sus precios, en forma de listado numerado.
b. Agregar un producto al pedido.
c. Ver el pedido actual.
d. Finalizar el pedido y salir.
4. Si el usuario ingresa una opción inexistente, el programa deberá mostrar un mensaje de error y 
volver a presentar las opciones.
5. Al agregar un producto, el programa deberá solicitar el nombre del producto y la cantidad deseada. 
Si el producto no existe en el menú, deberá informarse al usuario. La cantidad deberá ser un número entero 
mayor que cero.
6. Al ver el pedido actual, deberá mostrarse cada producto solicitado con su cantidad y subtotal. 
Si el pedido está vacío, deberá indicarse al usuario.
7. Al finalizar el pedido, el programa deberá solicitar el porcentaje de propina deseado, 
validando que se encuentre en el rango de 0 a 100.
8. Finalmente, deberá mostrarse un resumen que incluya el nombre del cliente, el detalle del pedido, 
el subtotal, el monto de la propina y el total a pagar."""


dictionary = {"Apple": 1500, "Pollo Asado": 4990, "Tomato": 2070, "Cereal": 3020, "Milk": 4745, "Salmon": 18065}
cart = []
usuario = input("Username: ")
print(f"{usuario}, welcome to \x1B[1;34mMenos x Mas\x1B[0m where we got some stuff!\x1B[0m")

while True:
    print("\n\x1B[1;34mMenu Options:\x1B[0m")
    print("1. View product menu")
    print("2. Add product to cart")
    print("3. View cart")
    print("4. Finish order")
    print("5. Exit")
    
    menu = input("Select an option: ")
    
    if menu == "1":
        print("Product Menu: ")
        for i, (product, price) in enumerate(dictionary.items(), start=1):
            print(f"{i}. {product}: ₡{price}")
    elif menu == "2":
        product_name = input("Enter the product name: ").casefold()
        if product_name in dictionary:
            quantity = int(input("Enter the quantity: "))
            if quantity > 0:
                cart.append((product_name, quantity))
                print(f"{quantity} {product_name}(s) added to the cart.")
            else:
                print("Invalid quantity. Please enter a positive integer.")
        else:
            print("Product not found in the menu.")
    elif menu == "3":
        if not cart:
            print("Your cart is empty.")
        else:
            print("Your cart contains:")
            for product, quantity in cart:
                print(f"- {quantity} x {product}")
            print(f"Subtotal: ₡{sum(dictionary[product] * quantity for product, quantity in cart)}")
    elif menu == "4":
        tip_percentage = float(input("Enter the tip percentage: "))
        if 0 <= tip_percentage <= 100:
            subtotal = sum(dictionary[product] * quantity for product, quantity in cart)
            tip_amount = subtotal * (tip_percentage / 100)
            total = subtotal + tip_amount
            print(f"Order Summary:")
            for item in cart:
                print(f"{item}: {cart[item]} x ₡{dictionary[item]} = ₡{dictionary[item] * cart[item]}")
            print(f"Subtotal: ₡{subtotal}")
            print(f"Tip ({tip_percentage}%): ₡{tip_amount}")
            print(f"Total to pay: ₡{total}")
            break
        else:
            print("Invalid tip percentage. Please enter a value between 0 and 100.")
    elif menu == "5":
        break
    else:
        print("Invalid option, please try again.")