import tkinter as tk
from tkinter import messagebox, simpledialog
from backend import *

class ShopSimulatorGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Shop Simulator GUI")
        self.root.geometry("1200x800")
        self.root.config(bg="black")
        
        self.user_budget = 0
        self.current_mode = None
        
        initialize_files()
        self.create_main_menu()

    class Hint: 
        def __init__(self,entry,hint):
            self.hint = hint
            self.entry = entry
            self.entry.insert(0, hint)  
            self.entry.config(fg="red")
            def on_click_entry(event):
                if self.entry.get() == self.hint:
                    self.entry.delete(0, tk.END)
                    self.entry.insert(0,"")
                    self.entry.config(fg="green")
            

            def on_focusout_entry(event):
                if self.entry.get() == "":
                    self.entry.insert(0, self.hint)
                    self.entry.config(fg="red")

            entry.bind("<FocusIn>", on_click_entry)
            entry.bind("<FocusOut>", on_focusout_entry)



    def clear_screen(self):
        """Clear all widgets from the screen"""
        for widget in self.root.winfo_children():
            widget.destroy()
    
    def create_main_menu(self):
        """Create the main menu for role selection"""
        self.clear_screen()
        
        # Title
        title_frame = tk.Frame(self.root, bg="black")
        title_frame.pack(pady=20)
        
        tk.Label(
            title_frame,
            text="SHOP SIMULATOR",
            fg="green",
            bg="black",
            font=("Times New Roman", 60)
        ).pack()
        
        # Role selection
        role_frame = tk.Frame(self.root, bg="black")
        role_frame.pack(pady=50)
        
        tk.Label(
            role_frame,
            text="Choose your role:",
            fg="white",
            bg="black",
            font=("Times New Roman", 30)
        ).pack(pady=20)
        
        button_frame = tk.Frame(role_frame, bg="black")
        button_frame.pack()
        
        tk.Button(
            button_frame,
            text="Shopkeeper",
            command=self.shopkeeper_login,
            fg="black",
            bg="white",
            font=("Times New Roman", 20),
            width=15,
            height=2
        ).pack(side=tk.LEFT, padx=10)
        
        tk.Button(
            button_frame,
            text="Customer",
            command=self.customer_setup,
            fg="black",
            bg="white",
            font=("Times New Roman", 20),
            width=15,
            height=2
        ).pack(side=tk.LEFT, padx=10)
        
        tk.Button(
            button_frame,
            text="Quit",
            command=self.root.quit,
            fg="white",
            bg="red",
            font=("Times New Roman", 20),
            width=15,
            height=2
        ).pack(side=tk.LEFT, padx=10)
    
    def shopkeeper_login(self):
        """Handle shopkeeper login"""
        self.clear_screen()
        
        # Title
        tk.Label(
            self.root,
            text="SHOPKEEPER LOGIN",
            fg="green",
            bg="black",
            font=("Times New Roman", 40)
        ).pack(pady=20)
        
        # Login form
        login_frame = tk.Frame(self.root, bg="black")
        login_frame.pack(pady=50)
        
        tk.Label(
            login_frame,
            text="Login ID:",
            fg="white",
            bg="black",
            font=("Times New Roman", 20)
        ).grid(row=0, column=0, padx=10, pady=10, sticky="e")
        
        self.login_entry = tk.Entry(
            login_frame,
            font=("Times New Roman", 20),
            width=20
        )
        self.login_entry.grid(row=0, column=1, padx=10, pady=10)
        
        tk.Label(
            login_frame,
            text="Password:",
            fg="white",
            bg="black",
            font=("Times New Roman", 20)
        ).grid(row=1, column=0, padx=10, pady=10, sticky="e")
        
        self.password_entry = tk.Entry(
            login_frame,
            font=("Times New Roman", 20),
            width=20,
            show="*"
        )
        self.password_entry.grid(row=1, column=1, padx=10, pady=10)
        
        button_frame = tk.Frame(login_frame, bg="black")
        button_frame.grid(row=2, column=0, columnspan=2, pady=20)
        
        tk.Button(
            button_frame,
            text="Login",
            command=self.authenticate_shopkeeper,
            fg="black",
            bg="white",
            font=("Times New Roman", 15),
            width=10
        ).pack(side=tk.LEFT, padx=5)
        
        tk.Button(
            button_frame,
            text="Back",
            command=self.create_main_menu,
            fg="white",
            bg="red",
            font=("Times New Roman", 15),
            width=10
        ).pack(side=tk.LEFT, padx=5)
    
    def authenticate_shopkeeper(self):
        """Authenticate shopkeeper credentials"""
        login_id = self.login_entry.get()
        password = self.password_entry.get()
        
        if authenticate_shopkeeper(login_id, password):
            self.shopkeeper_menu()
        else:
            messagebox.showerror("Error", "Invalid login ID or password!")
    
    def shopkeeper_menu(self):
        """Create shopkeeper management interface"""
        self.clear_screen()
        self.current_mode = "shopkeeper"
        
        # Title
        tk.Label(
            self.root,
            text="SHOPKEEPER PANEL",
            fg="green",
            bg="black",
            font=("Times New Roman", 40)
        ).pack(pady=20)
        
        # Menu buttons
        menu_frame = tk.Frame(self.root, bg="black")
        menu_frame.pack(pady=30)
        
        buttons = [
            ("View Items", self.view_store_items),
            ("Add Item", self.add_item_dialog),
            ("Remove Item", self.remove_item_dialog),
            ("Update Item", self.update_item_dialog),
            ("Back to Main", self.create_main_menu)
        ]
        
        for i, (text, command) in enumerate(buttons):
            row = i // 4
            col = i % 4
            
            tk.Button(
                menu_frame,
                text=text,
                command=command,
                fg="black",
                bg="white",
                font=("Times New Roman", 18),
                width=15,
                height=2
            ).grid(row=row, column=col, padx=10, pady=10)
        
        # Items display area
        self.items_display_frame = tk.Frame(self.root, bg="black")
        self.items_display_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
    
    def view_store_items(self):
        """Display store items in shopkeeper view"""
        for widget in self.items_display_frame.winfo_children():
            widget.destroy()
        
        tk.Label(
            self.items_display_frame,
            text="STORE INVENTORY",
            fg="green",
            bg="black",
            font=("Times New Roman", 25)
        ).pack(pady=10)
        
        items = read_store_items()
        if not items:
            tk.Label(
                self.items_display_frame,
                text="No items in store",
                fg="red",
                bg="black",
                font=("Times New Roman", 20)
            ).pack()
        else:
            # Create table
            table_frame = tk.Frame(self.items_display_frame, bg="black")
            table_frame.pack()
            
            headers = ["PID", "Item Name", "Price", "Quantity"]
            for col, header in enumerate(headers):
                tk.Label(
                    table_frame,
                    text=header,
                    fg="green",
                    bg="black",
                    font=("Times New Roman", 18),
                    relief="solid",
                    borderwidth=1,
                    width=15
                ).grid(row=0, column=col, padx=1, pady=1)
            
            for row, item in enumerate(items, 1):
                for col, value in enumerate(item):
                    tk.Label(
                        table_frame,
                        text=value,
                        fg="white",
                        bg="black",
                        font=("Times New Roman", 14),
                        relief="solid",
                        borderwidth=1,
                        width=15
                    ).grid(row=row, column=col, padx=1, pady=1)
    
    def add_item_dialog(self):
        """Dialog to add new item"""
        dialog = tk.Toplevel(self.root)
        dialog.title("Add New Item")
        dialog.geometry("400x300")
        dialog.config(bg="black")
        dialog.grab_set()
        
        tk.Label(
            dialog,
            text="ADD NEW ITEM",
            fg="green",
            bg="black",
            font=("Times New Roman", 20)
        ).pack(pady=10)
        
        # Form fields
        form_frame = tk.Frame(dialog, bg="black")
        form_frame.pack(pady=20)
        
        fields = ["Product ID:", "Item Name:", "Price:", "Quantity:"]
        entries = {}
        
        for i, field in enumerate(fields):
            tk.Label(
                form_frame,
                text=field,
                fg="white",
                bg="black",
                font=("Times New Roman", 14)
            ).grid(row=i, column=0, padx=10, pady=5, sticky="e")
            
            entry = tk.Entry(
                form_frame,
                font=("Times New Roman", 14),
                width=20
            )
            entry.grid(row=i, column=1, padx=10, pady=5)
            entries[field.replace(":", "")] = entry
        
        def add_item():
            pid = entries["Product ID"].get().strip()
            name = entries["Item Name"].get().strip()
            price = entries["Price"].get().strip()
            qty = entries["Quantity"].get().strip()
            
            if not all([pid, name, price, qty]):
                messagebox.showerror("Error", "All fields are required!")
                return
            
            success, message = add_store_item(pid, name, price, qty)
            if success:
                messagebox.showinfo("Success", message)
                dialog.destroy()
                self.view_store_items()
            else:
                messagebox.showerror("Error", message)
        
        button_frame = tk.Frame(dialog, bg="black")
        button_frame.pack(pady=20)
        
        tk.Button(
            button_frame,
            text="Add Item",
            command=add_item,
            fg="black",
            bg="white",
            font=("Times New Roman", 12)
        ).pack(side=tk.LEFT, padx=5)
        
        tk.Button(
            button_frame,
            text="Cancel",
            command=dialog.destroy,
            fg="white",
            bg="red",
            font=("Times New Roman", 12)
        ).pack(side=tk.LEFT, padx=5)
    
    def remove_item_dialog(self):
        """Dialog to remove item"""
        pid = simpledialog.askstring("Remove Item", "Enter Product ID to remove:")
        if pid:
            success, message = remove_store_item(pid)
            if success:
                messagebox.showinfo("Success", message)
                self.view_store_items()
            else:
                messagebox.showerror("Error", message)
    
    def update_item_dialog(self):
        """Dialog to update item"""
        pid = simpledialog.askstring("Update Item", "Enter Product ID to update:")
        if not pid:
            return
        
        item = get_store_item(pid)
        if not item:
            messagebox.showerror("Error", "Product ID not found!")
            return
        
        dialog = tk.Toplevel(self.root)
        dialog.title("Update Item")
        dialog.geometry("300x200")
        dialog.config(bg="black")
        dialog.grab_set()
        
        tk.Label(
            dialog,
            text=f"UPDATE ITEM: {pid}",
            fg="green",
            bg="black",
            font=("Times New Roman", 16)
        ).pack(pady=10)
        
        tk.Label(
            dialog,
            text=f"Current: {item[1]} - ${item[2]} - Qty: {item[3]}",
            fg="white",
            bg="black",
            font=("Times New Roman", 12)
        ).pack(pady=5)
        
        button_frame = tk.Frame(dialog, bg="black")
        button_frame.pack(pady=20)
        
        def update_price():
            new_price = simpledialog.askfloat("Update Price", "Enter new price:")
            if new_price is not None:
                success, message = update_store_item_price(pid, new_price)
                messagebox.showinfo("Result", message)
                if success:
                    dialog.destroy()
                    self.view_store_items()
        
        def update_quantity():
            new_qty = simpledialog.askinteger("Update Quantity", "Enter new quantity:")
            if new_qty is not None:
                success, message = update_store_item_quantity(pid, new_qty)
                messagebox.showinfo("Result", message)
                if success:
                    dialog.destroy()
                    self.view_store_items()
        
        tk.Button(
            button_frame,
            text="Update Price",
            command=update_price,
            fg="black",
            bg="white",
            font=("Times New Roman", 12)
        ).pack(pady=5)
        
        tk.Button(
            button_frame,
            text="Update Quantity",
            command=update_quantity,
            fg="black",
            bg="white",
            font=("Times New Roman", 12)
        ).pack(pady=5)
        
        tk.Button(
            button_frame,
            text="Cancel",
            command=dialog.destroy,
            fg="white",
            bg="red",
            font=("Times New Roman", 12)
        ).pack(pady=5)
    
    def customer_setup(self):
        """Setup customer interface with budget input"""
        self.clear_screen()
        
        # Title
        tk.Label(
            self.root,
            text="WELCOME TO PYTHON SUPER MART!",
            fg="green",
            bg="black",
            font=("Times New Roman", 40)
        ).pack(pady=20)
        
        # Budget input
        budget_frame = tk.Frame(self.root, bg="black")
        budget_frame.pack(pady=30)
        
        tk.Label(
            budget_frame,
            text="Enter your budget:",
            fg="white",
            bg="black",
            font=("Times New Roman", 25)
        ).pack(pady=10)
        
        self.budget_entry = tk.Entry(
            budget_frame,
            font=("Times New Roman", 20),
            width=15,
            justify='center'
        )
        self.Hint(self.budget_entry,"in USD")
        self.budget_entry.pack(pady=10)
        
        tk.Button(
            budget_frame,
            text="Confirm Budget",
            command=self.confirm_budget,
            fg="black",
            bg="white",
            font=("Times New Roman", 18),
            width=15
        ).pack(pady=10)
        
        tk.Button(
            budget_frame,
            text="Back",
            command=self.create_main_menu,
            fg="white",
            bg="red",
            font=("Times New Roman", 15),
            width=10
        ).pack(pady=5)
    
    def confirm_budget(self):
        """Confirm and validate budget"""
        budget_str = self.budget_entry.get().strip()
        if not budget_str:
            messagebox.showerror("Error", "Please enter a budget!")
            return
        
        is_valid, budget = validate_budget(budget_str)
        if not is_valid:
            messagebox.showerror("Error", budget)
            return
        
        self.user_budget = budget
        self.customer_interface()
    
    def subtract_from_budget(self, amount):
        self.user_budget -= (amount+0.15*amount)
        self.budget_label.config(text=f"Budget: ${self.user_budget:.2f}")


    def add_to_budget(self, amount):
        self.user_budget += (amount+0.15*amount)
        self.budget_label.config(text=f"Budget: ${self.user_budget:.2f}")

    def customer_interface(self):
        """Main customer shopping interface"""
        self.clear_screen()
        self.current_mode = "customer"
        
        # Top frame with budget and cart info
        top_frame = tk.Frame(self.root, bg="black")
        top_frame.pack(fill=tk.X, padx=10, pady=5)
        
        self.budget_label = tk.Label(
            top_frame,
            text=f"Budget: ${self.user_budget:.2f}",
            fg="green" if self.user_budget >0 else "red",
            bg="black",
            font=("Times New Roman", 20)
        )
        self.budget_label.pack(side=tk.LEFT)
        
        # Control buttons
        button_frame = tk.Frame(top_frame, bg="black")
        button_frame.pack(side=tk.RIGHT)
        
        tk.Button(
            button_frame,
            text="Remove Item(s)",
            command=self.remove_from_cart,
            fg="black",
            bg="lightblue",
            font=("Times New Roman", 12)
        ).pack(side=tk.LEFT, padx=2)
        
        tk.Button(
            button_frame,
            text="Checkout",
            command=self.checkout,
            fg="black",
            bg="lightgreen",
            font=("Times New Roman", 12)
        ).pack(side=tk.LEFT, padx=2)
        
        tk.Button(
            button_frame,
            text="Clear Cart",
            command=self.clear_cart_gui,
            fg="black",
            bg="orange",
            font=("Times New Roman", 12)
        ).pack(side=tk.LEFT, padx=2)
        
        tk.Button(
            button_frame,
            text="Leave Store",
            command=self.leave_store,
            fg="white",
            bg="red",
            font=("Times New Roman", 12)
        ).pack(side=tk.LEFT, padx=2)
        
        # Main content area
        content_frame = tk.Frame(self.root, bg="black")
        content_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)
        
        # Store items section
        store_frame = tk.LabelFrame(
            content_frame,
            text="STORE ITEMS",
            fg="green",
            bg="black",
            font=("Times New Roman", 16)
        )
        store_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 5))
        
        self.create_store_display(store_frame)
        
        # Cart section
        cart_frame = tk.LabelFrame(
            content_frame,
            text="YOUR CART",
            fg="green",
            bg="black",
            font=("Times New Roman", 16)
        )
        cart_frame.pack(side=tk.RIGHT, fill=tk.Y, padx=(5, 0))
        
        self.cart_display_frame = cart_frame
        self.update_cart_display()
    
    def create_store_display(self, parent):
        """Create scrollable store items display"""
        # Create canvas and scrollbar for scrolling
        canvas = tk.Canvas(parent, bg="black")
        scrollbar = tk.Scrollbar(parent, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas, bg="black")
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Headers
        headers = ["PID", "Name", "Price", "Available", "Action"]
        for col, header in enumerate(headers):
            tk.Label(
                scrollable_frame,
                text=header,
                fg="green",
                bg="black",
                font=("Times New Roman", 12),
                relief="solid",
                borderwidth=1,
                width=15
            ).grid(row=0, column=col, padx=1, pady=1)
        
        # Populate store items
        items = read_store_items()
        for row, item in enumerate(items, 1):
            for col, value in enumerate(item):
                tk.Label(
                    scrollable_frame,
                    text=value,
                    fg="white",
                    bg="black",
                    font=("Times New Roman", 12),
                    relief="solid",
                    borderwidth=1,
                    width=15
                ).grid(row=row, column=col, padx=1, pady=1)
            
            # Check if item is in cart
            cart_item = self.get_cart_item(item[0])
            if cart_item:
                qty = cart_item[3]  # Cart quantity
                self.create_quantity_controls(scrollable_frame, row, item[0], qty)
            else:
                tk.Button(
                    scrollable_frame,
                    text="Add",
                    command=lambda pid=item[0]: self.add_to_cart_dialog(pid),
                    fg="black",
                    bg="lightgreen",
                    font=("Times New Roman", 12),
                    width=15
                ).grid(row=row, column=4, padx=1, pady=1)

    def add_to_cart_dialog(self, pid):
        """Dialog to add item to cart"""
        item = get_store_item(pid)
        if not item:
            messagebox.showerror("Error", "Product ID not found!")
            return
        
        qty = simpledialog.askinteger("Add to Cart", f"Enter quantity for {item[1]} (Available: {item[3]}):", minvalue=1)
        if qty is not None:
            self.subtract_from_budget(float(get_store_item(pid)[2])*qty)
            success, message = add_to_cart(pid, qty)
            if success:
                messagebox.showinfo("Success", message)
                self.customer_interface()  # Refresh interface
            else:
                messagebox.showerror("Error", message)

    def create_quantity_controls(self, parent, row, pid, qty):
        """Create quantity adjustment controls at the specified row"""
        quantity_frame = tk.Frame(parent, bg="black")
        quantity_frame.grid(row=row, column=4, padx=1, pady=1)

        tk.Button(
            quantity_frame,
            text="-",
            command=lambda: self.decrease_quantity(pid),
            fg="black",
            bg="white",
            font=("Times New Roman", 12),
            width=3
        ).grid(row=0, column=0, padx=1, pady=1)

        qty_entry = tk.Entry(
            quantity_frame,
            font=("Times New Roman", 12),
            fg="green",
            bg="black",
            width=5,
            justify='center',
        )
        qty_entry.insert(0, str(qty))
        qty_entry.grid(row=0, column=1, padx=1, pady=1)
        

        tk.Button(
            quantity_frame,
            text="+",
            command=lambda: self.increase_quantity(pid),
            fg="black",
            bg="white",
            font=("Times New Roman", 12),
            width=3
        ).grid(row=0, column=2, padx=1, pady=1)

    def increase_quantity(self, pid):
        """Increase the quantity of an item in the cart"""
        success, message = add_to_cart(pid, 1)
        if success:
            self.subtract_from_budget(float(get_store_item(pid)[2]))
            self.customer_interface()  # Refresh interface
        else:
            messagebox.showerror("Error", message)

    def decrease_quantity(self, pid):
        """Decrease the quantity of an item in the cart"""
        cart_item = self.get_cart_item(pid)
        if cart_item:
            success, message = remove_from_cart(pid, 1)
            if success:
                self.add_to_budget(float(get_store_item(pid)[2]))
                self.customer_interface()  # Refresh interface
            else:
                messagebox.showerror("Error", message)

    def get_cart_item(self, pid):
        """Retrieve an item from the cart by PID"""
        cart_items = read_cart_items()
        for item in cart_items:
            if item[0] == pid:
                return item
        return None
            
    def remove_from_cart(self):
        """Display detailed cart view in a new window"""
        dialog = tk.Toplevel(self.root)
        dialog.title("Your Cart")
        dialog.geometry("600x400")
        dialog.config(bg="black")
        dialog.grab_set()
        
        tk.Label(
            dialog,
            text="YOUR CART",
            fg="green",
            bg="black",
            font=("Times New Roman", 20)
        ).pack(pady=10)
        
        # Cart items display
        cart_frame = tk.Frame(dialog, bg="black")
        cart_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        cart_items = read_cart_items()
        if not cart_items:
            tk.Label(
                cart_frame,
                text="Your cart is empty",
                fg="red",
                bg="black",
                font=("Times New Roman", 16)
            ).pack()
        else:
            # Headers
            headers = ["PID", "Name", "Price", "Quantity", "Remove"]
            for col, header in enumerate(headers):
                tk.Label(
                    cart_frame,
                    text=header,
                    fg="green",
                    bg="black",
                    font=("Times New Roman", 12),
                    relief="solid",
                    borderwidth=1,
                    width=15
                ).grid(row=0, column=col, padx=1, pady=1)
            
            # Cart items
            for row, item in enumerate(cart_items, 1):
                for col, value in enumerate(item):
                    tk.Label(
                        cart_frame,
                        text=value,
                        fg="white",
                        bg="black",
                        font=("Times New Roman", 12),
                        relief="solid",
                        borderwidth=1,
                        width=15
                    ).grid(row=row, column=col, padx=1, pady=1)
                
                # Remove button
                tk.Button(
                    cart_frame,
                    text="Remove",
                    command=lambda pid=item[0]: self.remove_from_cart_dialog(pid, dialog),
                    fg="white",
                    bg="red",
                    font=("Times New Roman", 12),
                    width=15
                ).grid(row=row, column=4, padx=1, pady=1)
        
        # Close button
        tk.Button(
            dialog,
            text="Close",
            command=dialog.destroy,
            fg="white",
            bg="red",
            font=("Times New Roman", 12)
        ).pack(pady=10)
    
    def remove_from_cart_dialog(self, pid, dialog):
        """Dialog to remove item from cart"""
        dialog_option = tk.Toplevel(self.root)
        dialog_option.title("Remove Item")
        dialog_option.geometry("300x200")
        dialog_option.config(bg="black")
        dialog_option.grab_set()
        
        tk.Label(
            dialog_option,
            text="Remove Options",
            fg="green",
            bg="black",
            font=("Times New Roman", 16)
        ).pack(pady=10)
        
        def remove_entire():
            success, message = remove_from_cart(pid)
            messagebox.showinfo("Result", message)
            if success:
                dialog_option.destroy()
                dialog.destroy()
                self.customer_interface()
        
        def reduce_quantity():
            qty = simpledialog.askinteger("Reduce Quantity", "Enter quantity to remove:", minvalue=1)
            if qty is not None:
                success, message = remove_from_cart(pid, qty)
                messagebox.showinfo("Result", message)
                if success:
                    dialog_option.destroy()
                    dialog.destroy()
                    self.customer_interface()
        
        tk.Button(
            dialog_option,
            text="Remove Entire Item",
            command=remove_entire,
            fg="black",
            bg="white",
            font=("Times New Roman", 12)
        ).pack(pady=5)
        
        tk.Button(
            dialog_option,
            text="Reduce Quantity",
            command=reduce_quantity,
            fg="black",
            bg="white",
            font=("Times New Roman", 12)
        ).pack(pady=5)
        
        tk.Button(
            dialog_option,
            text="Cancel",
            command=dialog_option.destroy,
            fg="white",
            bg="red",
            font=("Times New Roman", 12)
        ).pack(pady=5)
    
    def checkout(self):
        """Process checkout and display bill"""
        cart_items = read_cart_items()
        if not cart_items:
            messagebox.showinfo("Info", "Your cart is empty! Nothing to bill.")
            return
        
        subtotal, tax, grand_total, bill_items = calculate_bill()
        
        dialog = tk.Toplevel(self.root)
        dialog.title("Checkout")
        dialog.geometry("600x400")
        dialog.config(bg="black")
        dialog.grab_set()
        
        tk.Label(
            dialog,
            text="YOUR BILL",
            fg="green",
            bg="black",
            font=("Times New Roman", 20)
        ).pack(pady=10)
        
        # Bill items
        bill_frame = tk.Frame(dialog, bg="black")
        bill_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        headers = ["PID", "Name", "Price", "Qty", "Total"]
        for col, header in enumerate(headers):
            tk.Label(
                bill_frame,
                text=header,
                fg="green",
                bg="black",
                font=("Times New Roman", 12),
                relief="solid",
                borderwidth=1,
                width=15
            ).grid(row=0, column=col, padx=1, pady=1)
        
        for row, item in enumerate(bill_items, 1):
            for col, value in enumerate(item):
                tk.Label(
                    bill_frame,
                    text=f"{value:.2f}" if isinstance(value, float) else value,
                    fg="white",
                    bg="black",
                    font=("Times New Roman", 12),
                    relief="solid",
                    borderwidth=1,
                    width=15
                ).grid(row=row, column=col, padx=1, pady=1)
        
        # Bill totals
        totals_frame = tk.Frame(dialog, bg="black")
        totals_frame.pack(pady=10)
        
        tk.Label(
            totals_frame,
            text=f"Subtotal: ${subtotal:.2f}",
            fg="white",
            bg="black",
            font=("Times New Roman", 14)
        ).pack()
        
        tk.Label(
            totals_frame,
            text=f"Tax (15%): ${tax:.2f}",
            fg="white",
            bg="black",
            font=("Times New Roman", 14)
        ).pack()
        
        tk.Label(
            totals_frame,
            text=f"Grand Total: ${grand_total:.2f}",
            fg="white",
            bg="black",
            font=("Times New Roman", 14)
        ).pack()
        
        # Payment processing
        success, total, change = process_payment(self.user_budget)
        if success:
            tk.Label(
                totals_frame,
                text=f"Paid: ${total:.2f}",
                fg="green",
                bg="black",
                font=("Times New Roman", 14)
            ).pack()
            
            tk.Label(
                totals_frame,
                text=f"Change: ${change:.2f}",
                fg="green",
                bg="black",
                font=("Times New Roman", 14)
            ).pack()
            
            tk.Label(
                totals_frame,
                text="Thank you for shopping with us!",
                fg="green",
                bg="black",
                font=("Times New Roman", 14)
            ).pack()
            
            tk.Button(
                dialog,
                text="Return to Main Menu",
                command=lambda: [dialog.destroy(), self.create_main_menu()],
                fg="black",
                bg="white",
                font=("Times New Roman", 12)
            ).pack(pady=10)
            
            self.user_budget = change
        else:
            tk.Label(
                totals_frame,
                text=f"Insufficient balance! Need ${change:.2f} more.",
                fg="red",
                bg="black",
                font=("Times New Roman", 14)
            ).pack()
            
            tk.Button(
                dialog,
                text="Close",
                command=dialog.destroy,
                fg="white",
                bg="red",
                font=("Times New Roman", 12)
            ).pack(pady=10)
    
    def clear_cart_gui(self):
        """Clear cart and return items to store"""
        clear_cart()
        messagebox.showinfo("Success", "Cart cleared successfully!")
        self.customer_interface()
    
    def leave_store(self):
        """Return items to store and go back to main menu"""
        clear_cart()
        messagebox.showinfo("Info", "Returning items to store. Leaving store...")
        self.create_main_menu()
    
    def update_cart_display(self):
        """Update cart display in the customer interface"""
        for widget in self.cart_display_frame.winfo_children():
            if widget != self.cart_display_frame:  # Avoid destroying the frame itself
                widget.destroy()
        
        cart_items = read_cart_items()
        if not cart_items:
            tk.Label(
                self.cart_display_frame,
                text="Your cart is empty",
                fg="red",
                bg="black",
                font=("Times New Roman", 14)
            ).pack(pady=10)
        else:
            headers = ["PID", "Name", "Price", "Qty"]
            for col, header in enumerate(headers):
                tk.Label(
                    self.cart_display_frame,
                    text=header,
                    fg="green",
                    bg="black",
                    font=("Times New Roman", 12),
                    relief="solid",
                    borderwidth=1,
                    width=10
                ).grid(row=0, column=col, padx=1, pady=1)
            
            for row, item in enumerate(cart_items, 1):
                for col, value in enumerate(item):
                    tk.Label(
                        self.cart_display_frame,
                        text=value,
                        fg="white",
                        bg="black",
                        font=("Times New Roman", 12),
                        relief="solid",
                        borderwidth=1,
                        width=10
                    ).grid(row=row, column=col, padx=1, pady=1)

if __name__ == "__main__":
    gui = ShopSimulatorGUI()
    gui.root.mainloop()