import csv
import os

class Item:
    def __init__(self, pid, name, price, qty):
        self.pid = pid
        self.name = name
        self.price = float(price)  # Convert price to float
        self.qty = int(qty)        # Convert quantity to integer

    def to_list(self):
        return [self.pid, self.name, self.price, self.qty]

def initialize_files():
    """Initialize store and cart files if they don't exist"""
    if not os.path.exists('Store.csv'):
        with open('Store.csv', 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['PID', 'Item Name', 'Price', 'Quantity'])
    
    # Always create a fresh cart file
    with open('Cart.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['PID', 'Item Name', 'Price', 'Quantity'])

def read_store_items():
    """Read all items from store file"""
    items = []
    if os.path.exists('Store.csv'):
        with open('Store.csv', 'r', newline='') as f:
            reader = csv.reader(f)
            next(reader, None)  # Skip header
            for row in reader:
                if row:  # Skip empty rows
                    items.append(row)
    return items

def write_store_items(items):
    """Write items to store file"""
    with open('Store.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['PID', 'Item Name', 'Price', 'Quantity'])
        for item in items:
            writer.writerow(item)

def read_cart_items():
    """Read all items from cart file"""
    items = []
    if os.path.exists('Cart.csv'):
        with open('Cart.csv', 'r', newline='') as f:
            reader = csv.reader(f)
            next(reader, None)  # Skip header
            for row in reader:
                if row:  # Skip empty rows
                    items.append(row)
    return items

def write_cart_items_list(items):
    """Write items list to cart file"""
    with open('Cart.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['PID', 'Item Name', 'Price', 'Quantity'])
        for item in items:
            writer.writerow(item)

def update_store_item(pid, qty):
    """Update the quantity of an item in the store file"""
    items = read_store_items()
    for i, item in enumerate(items):
        if item[0] == pid:
            items[i][3] = str(qty)
            break
    write_store_items(items)
    
def get_quantity_of_store_item(pid):
    """Get an item quantity from the store file"""
    items = read_store_items()
    for item in items:
        if item[0] == pid:
            return int(item[3])
    return 0
        
def get_store_item(pid):
    """Get complete item details from store"""
    items = read_store_items()
    for item in items:
        if item[0] == pid:
            return item
    return None

def add_to_cart(pid, qty):
    """Add item to cart or update quantity if already exists"""
    store_item = get_store_item(pid)
    if not store_item:
        return False, "Item not found in store"
    
    available_qty = int(store_item[3])
    if qty > available_qty:
        return False, f"Insufficient quantity. Only {available_qty} available"
    
    cart_items = read_cart_items()
    
    # Check if item already in cart
    for i, cart_item in enumerate(cart_items):
        if cart_item[0] == pid:
            # Update existing cart item
            new_qty = int(cart_item[3]) + qty
            cart_items[i][3] = str(new_qty)
            write_cart_items_list(cart_items)
            
            # Update store quantity
            update_store_item(pid, available_qty - qty)
            return True, "Item quantity updated in cart"
    
    # Add new item to cart
    cart_item = store_item.copy()
    cart_item[3] = str(qty)
    cart_items.append(cart_item)
    write_cart_items_list(cart_items)
    
    # Update store quantity
    update_store_item(pid, available_qty - qty)
    return True, "Item added to cart"

def remove_from_cart(pid, qty=None):
    """Remove item from cart completely or reduce quantity"""
    cart_items = read_cart_items()
    
    for i, cart_item in enumerate(cart_items):
        if cart_item[0] == pid:
            current_qty = int(cart_item[3])
            
            if qty is None or qty >= current_qty:
                # Remove entire item
                qty_to_return = current_qty
                del cart_items[i]
            else:
                # Reduce quantity
                qty_to_return = qty
                cart_items[i][3] = str(current_qty - qty)
            
            # Return items to store
            current_store_qty = get_quantity_of_store_item(pid)
            update_store_item(pid, current_store_qty + qty_to_return)
            
            write_cart_items_list(cart_items)
            return True, f"Removed {qty_to_return} items from cart"
    
    return False, "Item not found in cart"

def get_cart_quantity(pid):
    """Get item quantity in cart"""
    cart_items = read_cart_items()
    for cart_item in cart_items:
        if cart_item[0] == pid:
            return int(cart_item[3])
    return 0

def get_store_item_quantity(pid):
    """Get item quantity in store"""
    store_item = get_store_item(pid)
    if store_item:
        return int(store_item[3])
    return 0

def update_cart_quantity(pid, new_qty):
    """Update item quantity in cart"""
    # Get current quantity in cart (assume this function exists)
    current_qty = get_cart_quantity(pid)
    
    # Calculate the difference
    diff = int(new_qty) - current_qty
    
    if diff > 0:
        # Increasing quantity: check store inventory and add to cart
        store_qty = get_store_item_quantity(pid)  # Assume this function exists
        if store_qty < diff:
            return False, "Insufficient inventory"
        add_to_cart(pid, qty=diff)
        update_store_item_quantity(pid, store_qty - diff)
    elif diff < 0:
        # Decreasing quantity: remove from cart and return to store
        remove_from_cart(pid, qty=-diff)
        store_qty = get_store_item_quantity(pid)
        update_store_item_quantity(pid, store_qty + (-diff))
    else:
        # No change needed
        return True, "Quantity unchanged"
    
    return True, "Quantity updated in cart"

def calculate_bill():
    """Calculate total bill with tax"""
    cart_items = read_cart_items()
    if not cart_items:
        return 0, 0, 0, []
    
    bill_items = []
    subtotal = 0
    
    for item in cart_items:
        price = float(item[2])
        qty = int(item[3])
        total = price * qty
        subtotal += total
        bill_items.append([item[0], item[1], price, qty, total])
    
    tax = subtotal * 0.15
    grand_total = subtotal + tax
    
    return subtotal, tax, grand_total, bill_items

def process_payment(budget):
    """Process payment and clear cart if successful"""
    subtotal, tax, grand_total, bill_items = calculate_bill()
    
    if budget >= grand_total:
        # Clear cart after successful payment
        initialize_files()
        return True, grand_total, budget - grand_total
    else:
        return False, grand_total, grand_total - budget

def clear_cart():
    """Clear cart and return all items to store"""
    cart_items = read_cart_items()
    
    for cart_item in cart_items:
        pid = cart_item[0]
        qty = int(cart_item[3])
        current_store_qty = get_quantity_of_store_item(pid)
        update_store_item(pid, current_store_qty + qty)
    
    initialize_files()

def validate_price(price_str):
    """Validate price input"""
    try:
        price = float(price_str)
        if price < 0:
            return False, "Price cannot be negative"
        return True, price
    except ValueError:
        return False, "Invalid price format"

def validate_quantity(qty_str):
    """Validate quantity input"""
    try:
        qty = int(qty_str)
        if qty < 0:
            return False, "Quantity cannot be negative"
        return True, qty
    except ValueError:
        return False, "Invalid quantity format"

def validate_budget(budget_str):
    """Validate budget input"""
    try:
        budget = float(budget_str)
        if budget < 0:
            return False, "Budget cannot be negative"
        return True, budget
    except ValueError:
        return False, "Invalid budget format"

# Shopkeeper functions
def add_store_item(pid, name, price, qty):
    """Add new item to store"""
    # Check for duplicate PID
    if get_store_item(pid):
        return False, "Product ID already exists"
    
    # Validate inputs
    is_valid, validated_price = validate_price(str(price))
    if not is_valid:
        return False, validated_price
    
    is_valid, validated_qty = validate_quantity(str(qty))
    if not is_valid:
        return False, validated_qty
    
    # Add item
    items = read_store_items()
    item = Item(pid, name, validated_price, validated_qty)
    items.append(item.to_list())
    write_store_items(items)
    
    return True, "Item added successfully"

def remove_store_item(pid):
    """Remove item from store"""
    items = read_store_items()
    
    for i, item in enumerate(items):
        if item[0] == pid:
            del items[i]
            write_store_items(items)
            return True, "Item removed successfully"
    
    return False, "Product ID not found"

def update_store_item_price(pid, new_price):
    """Update item price"""
    is_valid, validated_price = validate_price(str(new_price))
    if not is_valid:
        return False, validated_price
    
    items = read_store_items()
    for i, item in enumerate(items):
        if item[0] == pid:
            items[i][2] = str(validated_price)
            write_store_items(items)
            return True, "Price updated successfully"
    
    return False, "Product ID not found"

def update_store_item_quantity(pid, new_qty):
    """Update item quantity"""
    is_valid, validated_qty = validate_quantity(str(new_qty))
    if not is_valid:
        return False, validated_qty
    
    items = read_store_items()
    for i, item in enumerate(items):
        if item[0] == pid:
            items[i][3] = str(validated_qty)
            write_store_items(items)
            return True, "Quantity updated successfully"
    
    return False, "Product ID not found"

def authenticate_shopkeeper(login_id, password):
    """Authenticate shopkeeper credentials"""
    return login_id == 'loginID' and password == 'password'