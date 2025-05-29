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
    with open('Cart.csv', 'r', newline='') as f:
        reader = csv.reader(f)
        next(reader, None)  # Skip header
        for row in reader:
            if row:  # Skip empty rows
                items.append(row)
    return items

def write_cart_items(items):
    """Write items to cart file"""
    with open('Cart.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['PID', 'Item Name', 'Price', 'Quantity'])
        for item in items:
            writer.writerow(item)

def shopkeeper():
    """Shopkeeper mode functionality"""
    print("\nYou chose Shopkeeper Mode....\n")
    print("Welcome to your store\nPlease enter your login credentials for authentication!")
    
    loginID = input("Enter loginID: ")
    password = input("Enter password: ")
    
    if (loginID == 'loginID' and password == 'password'):
        while True:
            print('\nMenu:')
            print('[A] See List of Items Available in store')
            print('[B] Add a new Item')
            print('[C] Remove an Item')
            print('[D] Update an Item')
            print('[L] Leave Store')
            
            choice = input("\nEnter your choice [A][B][C][D][L]: ").upper()
            
            if choice == 'A':
                # Display items
                items = read_store_items()
                print("\nItems Available:")
                print(['PID', 'Item Name', 'Price', 'Quantity'])
                for item in items:
                    print(item)
                    
            elif choice == 'B':
                # Add new item
                print("\nAdd a new Item:")
                pid = input("Enter Product ID: ")
                name = input("Enter Item Name: ")
                
                # Validate price input
                while True:
                    try:
                        price = float(input("Enter Price of Item: "))
                        break
                    except ValueError:
                        print("Invalid price! Please enter a number.")
                
                # Validate quantity input
                while True:
                    try:
                        qty = int(input("Enter Quantity: "))
                        if qty < 0:
                            print("Quantity cannot be negative!")
                            continue
                        break
                    except ValueError:
                        print("Invalid quantity! Please enter a whole number.")
                
                # Create item and add to store
                item = Item(pid, name, price, qty)
                
                # Check for duplicate product ID
                items = read_store_items()
                for existing_item in items:
                    if existing_item[0] == pid:
                        print("\nProduct ID already exists! Please use a unique ID.")
                        break
                else:
                    items.append(item.to_list())
                    write_store_items(items)
                    print("\nItem added successfully!")
                    
            elif choice == 'C':
                # Remove item
                pid = input("Enter Product ID to be removed: ")
                items = read_store_items()
                
                for i, item in enumerate(items):
                    if item[0] == pid:
                        del items[i]
                        write_store_items(items)
                        print("\nItem removed successfully!")
                        break
                else:
                    print("\nProduct ID not found!")
                    
            elif choice == 'D':
                # Update item
                pid = input("Enter Product ID to be updated: ")
                items = read_store_items()
                
                for i, item in enumerate(items):
                    if item[0] == pid:
                        print("\nUpdate:")
                        print("[P] Price of Item")
                        print("[Q] Quantity of Items")
                        update_choice = input("Enter Choice [P][Q]: ").upper()
                        
                        if update_choice == 'P':
                            # Update price
                            try:
                                new_price = float(input("Enter New Price: "))
                                items[i][2] = new_price
                                write_store_items(items)
                                print("\nPrice updated successfully!")
                            except ValueError:
                                print("Invalid price! Update canceled.")
                                
                        elif update_choice == 'Q':
                            # Update quantity
                            try:
                                new_qty = int(input("Enter New Quantity: "))
                                if new_qty < 0:
                                    print("Quantity cannot be negative! Update canceled.")
                                else:
                                    items[i][3] = new_qty
                                    write_store_items(items)
                                    print("\nQuantity updated successfully!")
                            except ValueError:
                                print("Invalid quantity! Update canceled.")
                                
                        else:
                            print("Invalid choice!")
                        break
                else:
                    print("\nProduct ID not found!")
                    
            elif choice == 'L':
                # Leave shopkeeper mode
                print("Leaving Store......")
                return
                
            else:
                print("Invalid Choice!")
    else:
        print("Invalid loginID or password!")

def customer():
    """Customer mode functionality"""
    print("\nYou chose Customer Mode.....\n")
    print("Welcome to the Python Super Mart!!!!\n")
    
    # Get customer budget with validation
    while True:
        try:
            budget = float(input("Enter your budget: "))
            if budget < 0:
                print("Budget cannot be negative!")
                continue
            break
        except ValueError:
            print("Invalid budget! Please enter a number.")
    
    # Initialize cart
    initialize_files()
    
    # Show available items
    items = read_store_items()
    print("\nItems Available:")
    print(['PID', 'Item Name', 'Price', 'Quantity'])
    for item in items:
        print(item)
    
    # Shopping cart loop
    while True:
        print("\nYOUR CART:")
        cart_items = read_cart_items()
        if not cart_items:
            print("-Empty-")
        else:
            print(['PID', 'Item Name', 'Price', 'Quantity'])
            for item in cart_items:
                print(item)
        
        print("\nChoices:")
        print("[A] Add Item to Cart")
        print("[R] Remove Item from Cart")
        print("[C] Close Cart and go for Billing")
        print("[S] Show Cart")
        print("[L] Leave Store")
        
        choice = input("\nEnter your choice [A][R][C][S][L]: ").upper()
        
        if choice == 'A':
            # Add item to cart
            pid = input("Enter Product ID to buy: ")
            
            # Validate quantity input
            try:
                qty = int(input("Enter Quantity: "))
                if qty <= 0:
                    print("Quantity must be positive!")
                    continue
            except ValueError:
                print("Invalid quantity! Please enter a whole number.")
                continue
            
            # Find item in store
            store_items = read_store_items()
            cart_items = read_cart_items()
            
            for i, item in enumerate(store_items):
                if item[0] == pid:
                    available_qty = int(item[3])
                    
                    if qty > available_qty:
                        print(f"Insufficient quantity available! Only {available_qty} in stock.")
                    else:
                        # Check if item already in cart
                        for j, cart_item in enumerate(cart_items):
                            if cart_item[0] == pid:
                                # Update quantity in cart
                                cart_items[j][3] = int(cart_items[j][3]) + qty
                                # Reduce store quantity
                                store_items[i][3] = available_qty - qty
                                
                                write_cart_items(cart_items)
                                write_store_items(store_items)
                                print("Item quantity updated in cart!")
                                break
                        else:
                            # Add new item to cart
                            cart_item = item.copy()
                            cart_item[3] = qty
                            cart_items.append(cart_item)
                            
                            # Reduce store quantity
                            store_items[i][3] = available_qty - qty
                            
                            write_cart_items(cart_items)
                            write_store_items(store_items)
                            print("Item added to cart!")
                    break
            else:
                print("Product ID not found!")
                
        elif choice == 'R':
            # Remove item from cart
            print("Option to remove:")
            print("[I] Remove entire Item")
            print("[Q] Reduce Quantity of Item")
            
            remove_choice = input("Enter Choice [I][Q]: ").upper()
            
            if remove_choice == 'I':
                # Remove entire item
                pid = input("Enter Product ID to remove: ")
                
                cart_items = read_cart_items()
                store_items = read_store_items()
                
                for i, cart_item in enumerate(cart_items):
                    if cart_item[0] == pid:
                        # Return items to store
                        qty_to_return = int(cart_item[3])
                        
                        # Find item in store to update quantity
                        for j, store_item in enumerate(store_items):
                            if store_item[0] == pid:
                                store_items[j][3] = int(store_items[j][3]) + qty_to_return
                                break
                        
                        # Remove from cart
                        del cart_items[i]
                        
                        write_cart_items(cart_items)
                        write_store_items(store_items)
                        print("Item removed from cart successfully!")
                        break
                else:
                    print("Product ID not found in cart!")
                    
            elif remove_choice == 'Q':
                # Reduce quantity
                pid = input("Enter Product ID to reduce quantity of: ")
                
                try:
                    qty = int(input("Enter Quantity to be reduced: "))
                    if qty <= 0:
                        print("Quantity must be positive!")
                        continue
                except ValueError:
                    print("Invalid quantity! Please enter a whole number.")
                    continue
                
                cart_items = read_cart_items()
                store_items = read_store_items()
                
                for i, cart_item in enumerate(cart_items):
                    if cart_item[0] == pid:
                        current_qty = int(cart_item[3])
                        
                        if qty > current_qty:
                            print(f"Cannot reduce by {qty}! Only {current_qty} in cart.")
                        else:
                            # Update cart quantity
                            new_qty = current_qty - qty
                            
                            # Return items to store
                            for j, store_item in enumerate(store_items):
                                if store_item[0] == pid:
                                    store_items[j][3] = int(store_items[j][3]) + qty
                                    break
                            
                            if new_qty == 0:
                                # Remove item if quantity becomes zero
                                del cart_items[i]
                            else:
                                # Update quantity
                                cart_items[i][3] = new_qty
                            
                            write_cart_items(cart_items)
                            write_store_items(store_items)
                            print("Quantity reduced successfully!")
                        break
                else:
                    print("Product ID not found in cart!")
            else:
                print("Invalid choice!")
                
        elif choice == 'C':
            # Process billing
            cart_items = read_cart_items()
            
            if not cart_items:
                print("Your cart is empty! Nothing to bill.")
                continue
                
            print("\nYOUR BILL:")
            print(['PID', 'Item Name', 'Price', 'Quantity', 'Total'])
            
            total = 0
            for item in cart_items:
                item_price = float(item[2])
                item_qty = int(item[3])
                item_total = item_price * item_qty
                total += item_total
                print([item[0], item[1], item_price, item_qty, item_total])
            
            tax = total * 0.15
            grand_total = total + tax
            
            print(f"\nSubtotal: ${total:.2f}")
            print(f"Tax (15%): ${tax:.2f}")
            print(f"Grand Total: ${grand_total:.2f}")
            
            if budget >= grand_total:
                print("\nProcessing payment...")
                print(f"Paid: ${grand_total:.2f}")
                print(f"Change: ${(budget - grand_total):.2f}")
                print("\nThank you for shopping with us! Have a nice day!")
                
                # Clear cart after successful purchase
                os.remove('Cart.csv')
                initialize_files()
                return
            else:
                print(f"\nInsufficient balance! You need ${(grand_total - budget):.2f} more.")
                print("Please remove some items or add more funds.")
                
        elif choice == 'S':
            # Show cart - already shown at the beginning of the loop
            pass
            
        elif choice == 'L':
            # Leave customer mode
            print("Returning items to store...")
            
            # Return cart items to store
            cart_items = read_cart_items()
            store_items = read_store_items()
            
            for cart_item in cart_items:
                pid = cart_item[0]
                qty = int(cart_item[3])
                
                for i, store_item in enumerate(store_items):
                    if store_item[0] == pid:
                        store_items[i][3] = int(store_items[i][3]) + qty
                        break
            
            write_store_items(store_items)
            os.remove('Cart.csv')
            
            print("Leaving Store......")
            return
            
        else:
            print("Invalid Choice!")

def main():
    """Main function to run the shop simulator"""
    initialize_files()
    
    while True:
        print("\n===== SHOP SIMULATOR =====")
        print("Choose your role:")
        print("[A] Shopkeeper")
        print("[B] Customer")
        print("[Q] Quit")
        
        choice = input("\nEnter your choice [A][B][Q]: ").upper()
        
        if choice == 'A':
            shopkeeper()
        elif choice == 'B':
            customer()
        elif choice == 'Q':
            print("Exiting Simulator......")
            break
        else:
            print("Invalid choice!")

if __name__ == '__main__':
    main()
