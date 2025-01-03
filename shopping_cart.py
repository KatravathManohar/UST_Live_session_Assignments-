


cart=[]
items=['Bread','cheese','Butter','Cookies','Yougurt']
prices=[40,180,120,80,60]
print(items)
while True:
    print("What u want to do?")
    print("Enter 1 to view the items")
    print("enter 2 for adding items in cart")
    print("enter 3 for updating items in cart")
    print("enter 4 for deleting the items in cart")
    print("enter 5 for printing the bill")

    choice=int(input("Enter your choice:"))

    if choice == 1:
        print("Available Items:")
        for i in range(len(items)):
            print(f"Name: {items[i]} Price: {prices[i]}")

    elif choice == 2:
        item_name = input("Enter the item name: ")
        if item_name in items:
            quantity = int(input("Enter the quantity: "))
            index = items.index(item_name)
            price = prices[index]
            cart.append([item_name, quantity, price, price * quantity])
            print(f"{item_name} added to the cart.")
        else:
            print("Invalid item name. Please try again.")

    elif choice == 3:
        item_name = input("Which item to be updated: ")
        item_found = False
        for item in cart:
            if item[0] == item_name:
                quantity = int(input("Enter the quantity to be updated: "))
                item[1] = quantity
                item[3] = quantity * item[2]
                print(f"{item_name} updated in the cart.")
                item_found = True
                break
        if not item_found:
            print("Item not found in the cart.")

    elif choice == 4:
        item_name = input("Which item to be removed: ")
        item_found = False
        for item in cart:
            if item[0] == item_name:
                cart.remove(item)
                print(f"{item_name} removed from the cart.")
                item_found = True
                break
        if not item_found:
            print("Item not found in the cart.")

    elif choice == 5:
        print("\nCart Details:")
        print("Name,Quantity,Price,Total")
        total_amount = 0
        for item in cart:
            print(f"{item[0]},{item[1]},{item[2]},{item[3]}")
            total_amount += item[3]
            print(f"Total Amount of Bill: {total_amount}\n")

    elif choice == 6:
        print("\nCart Details:")
        print("Name,Quantity,Price,Total")
        total_amount = 0
        for item in cart:
            print(f"{item[0]},{item[1]},{item[2]},{item[3]}")
            total_amount += item[3]
        print(f"Total Amount of Bill: {total_amount}")
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")

