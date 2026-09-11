inventory = 0;
failures = 0;

while True:
    
    stock = input("Enter stock quantity (or type 'quit' to exit): ")
    if stock == 'quit':
        print(f"Final inventory: {inventory}")
        print(f"Total failures: {failures}")
        break
    elif not stock.isdigit():
        print("Invalid input. Please enter a valid number.")
        failures += 1
    elif int(stock) < 0:
        print("Stock quantity cannot be negative.")
        failures += 1

    elif inventory + int(stock) > 500:
        print("Cannot add stock. Inventory limit exceeded.")
        break
    else:
        inventory += int(stock)
        print(f"Stock added. Current inventory: {inventory}")