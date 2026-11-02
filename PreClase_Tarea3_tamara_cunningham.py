dictionary = {"apple": 1500, "pollo asado": 4990, "tomato": 2070, "cereal": 3020, "milk": 4745, "salmon": 18065}
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
                print(f"{quantity} {product_name}(s) added to cart.")
            else:
                print("Invalid quantity. Please enter a positive number.")
        else:
            print("Product not found in the menu.")
    elif menu == "3":
        if not cart:
            print("Your cart is empty.")
        else:
            print("Your cart contains:")
            for product, quantity in cart:
                print(f"- {quantity} x {product} = ₡{dictionary[product] * quantity}")
            print(f"Subtotal: ₡{sum(dictionary[product] * quantity for product, quantity in cart)}")
    elif menu == "4":
        tip_percentage = float(input("Enter the tip percentage: "))
        if 0 <= tip_percentage <= 100:
            subtotal = sum(dictionary[product] * quantity for product, quantity in cart)
            tip_amount = subtotal * (tip_percentage / 100)
            total = subtotal + tip_amount
            print(f"Order Summary:")
            for product, quantity in cart:
                print(f"{product}: {quantity} x ₡{dictionary[product]} = ₡{dictionary[product] * quantity}")
            print(f"Subtotal: ₡{subtotal}")
            print(f"Tip ({tip_percentage}%): ₡{tip_amount}")
            print(f"Total to pay: ₡{total}")
            break
        else:
            print("Invalid tip percentage. Please enter a value between 0 and 100.")
    elif menu == "5":
        print(f"Thanks {usuario} for shopping at \x1B[1;34mMenos x Mas\x1B[0m where we got some stuff!\x1B[0m")
        break
    else:
        print("Invalid option, please try again.")