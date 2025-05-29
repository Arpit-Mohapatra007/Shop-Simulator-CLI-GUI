import tkinter as tk
import os 
import csv
class Item:
    def __init__(self, pid, name, price, qty):
        self.pid = pid
        self.name = name
        self.price = float(price)  # Convert price to float
        self.qty = int(qty)        # Convert quantity to integer

    def to_dict(self):
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

def buget_record():
	user_budget = budget_entry.get()
	budget_entry.destroy()
	confirm_button.destroy()
	budget = tk.Label(
		budget_frame,
		text=f"Budget:${user_budget}",
		fg="green",
		bg="black",
		font=("Times New Roman",30)
		)
	budget.pack()

def render_cart():
	TableHeading(cart_frame,"Item Name",0)
	TableHeading(cart_frame,"Price",1)
	TableHeading(cart_frame,"Quantity",2)
	TableHeading(cart_frame,"Total Price",3)

def update_cart():
	# if name exists then only update quantity
	# if new item is added i.e. name doesnt exists create all the columns 

root = tk.Tk()
root.title("Shop Simulator GUI")
root.geometry("1080x2400")	
root.config(bg="black")	


head_frame = tk.Frame(root)
head_frame.pack()
tk.Label(
	head_frame,
	text="SHOP SIMULATOR",
	fg="green",
	bg="black",
	font=("Times New Roman",90
		)
	).pack()
	


budget_frame = tk.Frame(root)
budget_frame.pack()

budget_entry = tk.Entry(
	budget_frame,
	bd=1,
	relief="raised",
	bg="black",
	fg="red",
	width=30,
	font=("Times New Roman",30)
	)

class Hint:
	def __init__ (self,entry,hint):
		self.entry=entry
		self.entry.insert(0,hint)
		def on_entry_click(event):
			if self.entry.get() == hint:
				self.entry.delete(0,"end")
				self.entry.config(fg="green")

		def on_focusout(event):
			if self.entry.get() == "":
				self.entry.insert(0,hint)
				self.entry.config(fg="red")

		self.entry.bind("<FocusIn>", on_entry_click)
		self.entry.bind("<FocusOut>", on_focusout)

Hint(budget_entry,"Enter your budget..")
budget_entry.grid(row=0, column=0, padx=5)


confirm_button = tk.Button(
	budget_frame,
	text="Confirm",
	command=buget_record,
	fg="black",
	bg="white",
	relief="raised",
	bd=1,
	activebackground="grey",
	font=("Times New Roman",30)
	)
confirm_button.grid(row=0, column=1, padx=5)

tk.Label(
	text="--YOUR CART--",
	fg="green",
	bg="black",
	font=("Times New Roman",30
		)
	).pack()

cart_frame = tk.Frame(root)
cart_frame.pack()

cart_label = tk.Label(
	cart_frame,
	text="(empty)",
	fg="red",
	bg="black",
	font=("Times New Roman",20
		)
	).pack()

shelf_frame = tk.Frame(root)
shelf_frame.pack()

shelf_label = tk.Label(
	shelf_frame,
	text="--SHELF--",
	fg="green",
	bg="black",
	font=("Times New Roman",40
		)
	).grid(row=0,column=2)

class TableHeading:
	def __init__(self, frame, title, column):
		self.label = tk.Label(
			frame,
			text=title,
			fg="green",
			bg="black",
			font=("Times New Roman",30)
			)
		self.label.grid(row=1,column=column,padx=5,pady=5)


class TableCell:
	def __init__(self,frame,value,row,column):
		self.label=tk.Label(
			frame,
			text=value,
			fg="green",
			bg="black",
			font=("Times New Roman",20)
			)
		self.label.grid(row=row,column=column,padx=5,pady=5)


class ShelfItem:
	def __init__(self,name,price,available_qty,row):
		self.name_str=name
		self.price_val=price
		self.available_qty=available_qty

		TableCell(shelf_frame,name,row,0)
		TableCell(shelf_frame,price,row,1)
		TableCell(shelf_frame,available_qty,row,2)

		self.add_cart=tk.Button(
			shelf_frame,
			text="Add to Cart",
			command=lambda: self.add_to_cart(),
			fg="black",
			bg="white",
			relief="raised",
			bd=1,
			activebackground="grey",
			font=("Times New Roman",20)
			)

		self.add_to_cart.grid(row=row,column=3,padx=5,pady=5)

	def add_to_cart(self):

		self.add_cart.destroy()

		qty_frame=tk.Frame(shelf_frame)
		qty_frame.grid(row=row,column=3,padx=5,pady=5)

		self.dec_button=tk.Button(
			qty_frame,
			text="-",
			command=lambda: self.dec_qty(),
			fg="black",
			bg="white",
			relief="raised",
			bd=1,
			activebackground="grey",
			font=("Times New Roman",20)
			).grid(row=0,column=0,padx=1,pady=1)

		self.qty_entry=tk.Entry(
			qty_frame,
			bd=1,
			relief="raised",
			bg="black",
			fg="red",
			font=("Times New Roman",20)
			)
		Hint(self.qty_entry,"Qty")
		self.qty_entry.grid(row=0,column=1)
		self.available_qty-=int(self.qty_entry.get())

		self.inc_button=tk.Button(
			qty_frame,
			text="+",
			command=lambda: self.inc_qty(),
			fg="black",
			bg="white",
			relief="raised",
			bd=1,
			activebackground="grey",
			font=("Times New Roman",20)
			).grid(row=0,column=2,padx=1,pady=1)

	def dec_qty(self):
		user_qty=int(self.qty_entry.get())
		user_qty-=1
		self.qty_entry.insert(0,user_qty)
		self.available_qty+=1

	def inc_qty(self):
		user_qty=int(self.qty_entry.get())
		user_qty+=1
		self.qty_entry.insert(0,user_qty)
		self.available_qty-=1

		TableCell(self.frame,self.available_qty,self.row,2)

		global cart_label
		if(cart_label):
			cart_label.destroy()

		global render_cart
		if not render_cart:
			render_cart()

		update_cart()


TableHeading(shelf_frame,"Item Name",column=0)
TableHeading(shelf_frame,"Price",column=1)
TableHeading(shelf_frame,"Quantity Left",column=2)
TableHeading(shelf_frame,"Add to Cart",column=3)

root.mainloop()
