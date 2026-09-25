INVENTORY_FILE = "inventory.txt"
inventory = 0
transactions = []
failures = 0


def load_inventory():
    try:
        with open(INVENTORY_FILE, "r") as file:
            lines = file.readlines()

        if not lines:
            return 0, []

        saved_inventory = int(lines[0].strip())
        saved_transactions = []

        for line in lines[1:]:
            order_number, product, quantity = line.strip().split("|")
            saved_transactions.append(
                (int(order_number), product, int(quantity))
            )

        return saved_inventory, saved_transactions

    except (FileNotFoundError, ValueError):
        return 0, []


def save_inventory():
    with open(INVENTORY_FILE, "w") as file:
        file.write(str(inventory) + "\n")

        for order_number, product, quantity in transactions:
            file.write(f"{order_number}|{product}|{quantity}\n")


def get_next_order_number():
    if not transactions:
        return 1001

    return max(order[0] for order in transactions) + 1


def display_current_order():
    print("Current orders:")
    if not transactions:
        print("No orders yet.")
    else:
        for order_number, product, quantity in transactions:
            print(f"{order_number}, {product}, {quantity}")
    print(f"Next order number: {get_next_order_number()}")


def get_valid_input():
    global failures

    while True:
        display_current_order()
        product = input("Enter product name (or type 'quit' to exit): ")
        order_number = 1001
        if product.lower() == "quit":
            save_inventory()
            generate_report()
            break

        quantity_input = input("Enter Quantity: ")

        try:
            quantity = int(quantity_input)

            if product.strip() == "" or quantity < 0:
                raise ValueError

            if inventory + quantity > 500:
                print("Cannot add stock. Inventory limit exceeded.")
                continue
            order_number = get_next_order_number()

            process_delivery(quantity)
            transactions.append((order_number, product, quantity))
            print(
                f"New order added: {order_number}, "
                f"{product}, {quantity}"
            )
            print("Orders successfully saved to inventory.txt")
        except ValueError:
            print("Invalid product name or quantity.")
            failures += 1


def process_delivery(quantity):
    global inventory
    inventory += quantity
    print(f"Stock added. Current inventory: {inventory}")


def generate_report():
    print("Inventory:")
    for order_number, product, quantity in transactions:
        print(f"{order_number}, {product}, {quantity}")


inventory, transactions = load_inventory()
get_valid_input()