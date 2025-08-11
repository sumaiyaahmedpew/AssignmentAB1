# problem_01

inventory = {
    101: ("Pen", 10.0, 50),
    102: ("Notebook", 50.0, 20),
    103: ("Pencil", 5.0, 100),
    104: ("Marker", 30.0, 25),
    105: ("Eraser", 8.0, 40)
}

def add_product(pid, name, price, qty):
    if pid in inventory:
        print("Product ID already exists!")
    else:
        inventory[pid] = (name, price, qty)
        print("Product added successfully.")

def update_quantity(pid, change):
    if pid in inventory:
        name, price, qty = inventory[pid]
        inventory[pid] = (name, price, qty + change)
        print("Quantity updated.")
    else:
        print("Product not found.")

def find_products_in_price_range(low, high):
    return [v for v in inventory.values() if low <= v[1] <= high]

# Function to extract price for sorting
def get_price(item):
    # item is (product_id, (name, price, quantity))
    return item[1][1]  # get the price

def sort_by_price():
    return sorted(inventory.items(), key=get_price)

# Example usage
add_product(106, "Glue", 15.0, 10)
update_quantity(103, -10)

print("Products in range 10–30:", find_products_in_price_range(10, 30))
print("Sorted by price:", sort_by_price())
print("Final inventory:", inventory)
