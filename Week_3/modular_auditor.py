inventory = 0;
failures = 0;
def get_valid_input():
    while True:
        stock = input("Enter stock quantity (or type 'quit' to exit): ")
        if stock == 'quit':
            generate_report()
            break
        elif not stock.isdigit():
            print("Invalid input. Please enter a valid number.")
            failures += 1
        elif int(stock) < 0:  
            print("Stock quantity cannot be negative.")
            failures += 1
        elif inventory + int(stock) > 500:
            print("Cannot add stock. Inventory limit exceeded.")
            generate_report()
            break
        else:
            process_delivery(inventory, int(stock))
            calculate_tax(int(stock))
           

def process_delivery(current_total, new_value):
    global inventory
    inventory += new_value
    print(f"Stock added. Current inventory: {inventory}")


def calculate_tax(amount):
    tax = amount * 0.10
    print(f"Tax collected for this delivery: {tax}")

def generate_report():
    print(f"Final inventory: {inventory}")
    print(f"Total failures: {failures}")
    print(f"Total tax collected: {calculate_tax(inventory)}")


get_valid_input()