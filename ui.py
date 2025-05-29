import tkinter as tk
from backend import *  # We'll define logic in backend.py

class ShopSimulator:
    def __init__(self, root):
        self.root = root
        self.root.title("Shop Simulator GUI")
        self.root.geometry("1080x2400")
        self.root.config(bg="black")

        initialize_files()

        self.budget = 0
        self.cart_items = []
        self.store_items = read_store_items()

        self.setup_ui()

    def setup_ui(self):
        self.head_frame = tk.Frame(self.root)
        self.head_frame.pack()
        tk.Label(
            self.head_frame,
            text="SHOP SIMULATOR",
            fg="green",
            bg="black",
            font=("Times New Roman", 90)
        ).pack()

        self.budget_frame = tk.Frame(self.root)
        self.budget_frame.pack()

        self.budget_entry = tk.Entry(
            self.budget_frame,
            bd=1,
            relief="raised",
            bg="black",
            fg="red",
            width=30,
            font=("Times New Roman", 30)
        )
        Hint(self.budget_entry, "Enter your budget..")
        self.budget_entry.grid(row=0, column=0, padx=5)

        self.confirm_button = tk.Button(
            self.budget_frame,
            text="Confirm",
            command=self.set_budget,
            fg="black",
            bg="white",
            relief="raised",
            bd=1,
            activebackground="grey",
            font=("Times New Roman", 30)
        )
        self.confirm_button.grid(row=0, column=1, padx=5)

        tk.Label(
            text="--YOUR CART--",
            fg="green",
            bg="black",
            font=("Times New Roman", 30)
        ).pack()

        self.cart_frame = tk.Frame(self.root)
        self.cart_frame.pack()

        self.cart_label = tk.Label(
            self.cart_frame,
            text="(empty)",
            fg="red",
            bg="black",
            font=("Times New Roman", 20)
        )
        self.cart_label.pack()

        self.shelf_frame = tk.Frame(self.root)
        self.shelf_frame.pack()

        tk.Label(
            self.shelf_frame,
            text="--SHELF--",
            fg="green",
            bg="black",
            font=("Times New Roman", 40)
        ).grid(row=0, column=2)

        TableHeading(self.shelf_frame, "Item Name", column=0)
        TableHeading(self.shelf_frame, "Price", column=1)
        TableHeading(self.shelf_frame, "Quantity Left", column=2)
        TableHeading(self.shelf_frame, "Add to Cart", column=3)

        self.render_shelf()

    def set_budget(self):
        self.budget = float(self.budget_entry.get())
        self.budget_entry.destroy()
        self.confirm_button.destroy()
        tk.Label(
            self.budget_frame,
            text=f"Budget: ${self.budget}",
            fg="green",
            bg="black",
            font=("Times New Roman", 30)
        ).pack()

    def render_shelf(self):
        for idx, item in enumerate(self.store_items, start=2):
            ShelfItem(self.shelf_frame, item[1], item[2], item[3], idx, self)

class Hint:
    def __init__(self, entry, hint):
        self.entry = entry
        self.entry.insert(0, hint)

        def on_entry_click(event):
            if self.entry.get() == hint:
                self.entry.delete(0, "end")
                self.entry.config(fg="green")

        def on_focusout(event):
            if self.entry.get() == "":
                self.entry.insert(0, hint)
                self.entry.config(fg="red")

        self.entry.bind("<FocusIn>", on_entry_click)
        self.entry.bind("<FocusOut>", on_focusout)

class TableHeading:
    def __init__(self, frame, title, column):
        self.label = tk.Label(
            frame,
            text=title,
            fg="green",
            bg="black",
            font=("Times New Roman", 30)
        )
        self.label.grid(row=1, column=column, padx=5, pady=5)

class TableCell:
    def __init__(self, frame, value, row, column):
        self.var = tk.StringVar()
        self.var.set(str(value))
        self.label = tk.Label(
            frame,
            textvariable=self.var,
            fg="green",
            bg="black",
            font=("Times New Roman", 20)
        )
        self.label.grid(row=row, column=column, padx=5, pady=5)

    def update(self, new_value):
        self.var.set(str(new_value))

class ShelfItem:
    def __init__(self, frame, name, price, quantity, row, app):
        self.app = app
        self.name = name
        self.price = float(price)
        self.available_qty = int(quantity)
        self.row = row
        self.frame = frame

        TableCell(frame, name, row, 0)
        TableCell(frame, price, row, 1)
        self.qty_cell = TableCell(frame, self.available_qty, row, 2)

        self.add_btn = tk.Button(
            frame,
            text="Add to Cart",
            command=self.add_to_cart,
            fg="black",
            bg="white",
            relief="raised",
            bd=1,
            activebackground="grey",
            font=("Times New Roman", 20)
        )
        self.add_btn.grid(row=row, column=3, padx=5, pady=5)

    def add_to_cart(self):
        self.add_btn.destroy()

        self.qty_frame = tk.Frame(self.frame)
        self.qty_frame.grid(row=self.row, column=3, padx=5, pady=5)

        self.dec_button = tk.Button(
            self.qty_frame,
            text="-",
            command=self.dec_qty,
            fg="black",
            bg="white",
            relief="raised",
            bd=1,
            activebackground="grey",
            font=("Times New Roman", 20)
        )
        self.dec_button.grid(row=0, column=0, padx=1, pady=1)

        self.qty_entry = tk.Entry(
            self.qty_frame,
            bd=1,
            relief="raised",
            bg="black",
            fg="red",
            font=("Times New Roman", 20),
            width=5
        )
        self.qty_entry.insert(0, "1")
        self.qty_entry.grid(row=0, column=1)
        self.available_qty -= 1

        self.inc_button = tk.Button(
            self.qty_frame,
            text="+",
            command=self.inc_qty,
            fg="black",
            bg="white",
            relief="raised",
            bd=1,
            activebackground="grey",
            font=("Times New Roman", 20)
        )
        self.inc_button.grid(row=0, column=2, padx=1, pady=1)

        update_cart_item(self.name, self.price, 1)
        self.refresh_cart_label()
        self.qty_cell.update(self.available_qty)

    def dec_qty(self):
        qty = int(self.qty_entry.get())
        if qty > 1:
            qty -= 1
            self.qty_entry.delete(0, tk.END)
            self.qty_entry.insert(0, str(qty))
            self.available_qty += 1
            update_cart_item(self.name, self.price, -1)
            self.qty_cell.update(self.available_qty)
            self.refresh_cart_label()

    def inc_qty(self):
        qty = int(self.qty_entry.get())
        if self.available_qty > 0:
            qty += 1
            self.qty_entry.delete(0, tk.END)
            self.qty_entry.insert(0, str(qty))
            self.available_qty -= 1
            update_cart_item(self.name, self.price, 1)
            self.qty_cell.update(self.available_qty)
            self.refresh_cart_label()

    def refresh_cart_label(self):
        self.app.cart_label.config(text=f"Updated cart: {self.name}")

if __name__ == '__main__':
    root = tk.Tk()
    app = ShopSimulator(root)
    root.mainloop()
