import tkinter as tk

from backend import read_store_items

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

hint = "Enter you Budget.."

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
    def __init__(self, entry, hint, on_valid_input=None):
        self.entry = entry
        self.hint = hint
        self.on_valid_input = on_valid_input
        self.entry.insert(0, hint)
        self.entry.config(fg="red")

        self.entry.bind("<FocusIn>", self.on_entry_click)
        self.entry.bind("<FocusOut>", self.on_focus_out)
        self.entry.bind("<Return>", self.on_focus_out)

    def on_entry_click(self, event):
        if self.entry.get() == self.hint:
            self.entry.delete(0, "end")
            self.entry.config(fg="green")

    def on_focus_out(self, event):
        text = self.entry.get()
        if text == "":
            self.entry.insert(0, self.hint)
            self.entry.config(fg="red")
        else:
            if self.on_valid_input:
                self.on_valid_input()


Hint(budget_entry,"Enter your budget..")
budget_entry.grid(row=0, column=0)


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
confirm_button.grid(row=0, column=1)

tk.Label(
	text="--YOUR CART--",
	fg="green",
	bg="black",
    justify="center",
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
    justify="center",
	font=("Times New Roman",20
		)
	).pack()

shelf_frame = tk.Frame(root)
shelf_frame.config(bg="black")
shelf_frame.pack()

shelf_label = tk.Label(
	shelf_frame,
	text="--SHELF--",
	fg="green",
	bg="black",
    justify="center",
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
            justify="center",
			font=("Times New Roman",30)
			)
		self.label.grid(row=1,column=column)


class TableCell:
	def __init__(self,frame,value,row,column):
		self.label=tk.Label(
			frame,
			text=value,
			fg="green",
			bg="black",
            justify="center",
			font=("Times New Roman",20)
			)
		self.label.grid(row=row,column=column)


class ShelfItem:
    def __init__(self, pid, name, price, available_qty, row):
        self.pid = pid
        self.name = name
        self.price = float(price)
        self.available_qty = int(available_qty)
        self.row = row

        TableCell(shelf_frame, self.pid, row, 0)
        TableCell(shelf_frame, self.name, row, 1)
        TableCell(shelf_frame, self.price, row, 2)
        TableCell(shelf_frame, self.available_qty, row, 3)

        self.add_cart_btn = tk.Button(
            shelf_frame,
            text="Add to Cart",
            command=self.add_to_cart,
            fg="black",
            bg="white",
            relief="raised",
            bd=1,
            activebackground="grey",
            font=("Times New Roman", 20)
        )
        self.add_cart_btn.grid(row=self.row, column=4)

    def add_to_cart(self):
        self.add_cart_btn.destroy()

        qty_frame = tk.Frame(shelf_frame)
        qty_frame.grid(row=self.row, column=4)

        self.user_qty = 0

        self.dec_button = tk.Button(
            qty_frame,
            text="-",
            command=self.dec_qty,
            fg="black",
            bg="white",
            relief="raised",
            bd=1,
            activebackground="grey",
            state="disabled",
            font=("Times New Roman", 20)
        )
        self.dec_button.grid(row=0, column=0)

        self.inc_button = tk.Button(
            qty_frame,
            text="+",
            command=self.inc_qty,
            fg="black",
            bg="white",
            relief="raised",
            bd=1,
            activebackground="grey",
            state="disabled",
            font=("Times New Roman", 20)
        )
        self.inc_button.grid(row=0, column=2)

        self.qty_entry = tk.Entry(
            qty_frame,
            bd=1,
            relief="raised",
            bg="black",
            fg="red",
            width=5,
            font=("Times New Roman", 20)
        )
        self.qty_entry.grid(row=0, column=1)
        Hint(self.qty_entry, "Qty", on_valid_input=self.track_qty)

    def track_qty(self):
        value = self.qty_entry.get()
        try:
            qty = int(value)
            if qty <= 0 or qty > self.available_qty:
                raise ValueError
            self.user_qty = qty
            self.qty_entry.config(fg="green")
            self.dec_button.config(state="active")
            self.inc_button.config(state="active")
            self.available_qty -= self.user_qty
            TableCell(shelf_frame, self.available_qty, self.row, 3)
        except ValueError:
            self.user_qty = 0
            self.qty_entry.delete(0, "end")
            self.qty_entry.insert(0, "Qty")
            self.qty_entry.config(fg="red")
            self.dec_button.config(state="disabled")
            self.inc_button.config(state="disabled")

    def dec_qty(self):
        try:
            user_qty = int(self.qty_entry.get())
        except ValueError:
            user_qty = 0
        if user_qty > 1:
            user_qty -= 1
            self.qty_entry.delete(0, 'end')
            self.qty_entry.insert(0, str(user_qty))
            self.user_qty = user_qty
            self.available_qty += 1
            TableCell(shelf_frame, self.available_qty, self.row, 3)

    def inc_qty(self):
        try:
            user_qty = int(self.qty_entry.get())
        except ValueError:
            user_qty = 0
        if user_qty < self.available_qty:
            user_qty += 1
            self.qty_entry.delete(0, 'end')
            self.qty_entry.insert(0, str(user_qty))
            self.user_qty = user_qty
            self.available_qty -= 1
            TableCell(shelf_frame, self.available_qty, self.row, 3)

    

    

  
shelf_headings = ["PID", "Item Name", "Price", "Quantity Left", "Add to Cart"]
for col, title in enumerate(shelf_headings):
    TableHeading(shelf_frame, title, col)

def refresh_ui():
   
    for widget in shelf_frame.winfo_children()[len(shelf_headings):]:
        widget.destroy()

    
    for idx, (pid, name, price, qty) in enumerate(read_store_items(), start=1):
         ShelfItem(pid, name, price, qty, idx+1)

refresh_ui()
root.mainloop()