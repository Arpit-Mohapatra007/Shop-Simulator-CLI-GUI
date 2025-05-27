import tkinter as tk

def buget_record():
	user_budget = budget_entry.get()
	budget_entry.destroy()
	confirm_button.destroy()
	budget = tk.Label(
		budgetFrame,
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


headFrame = tk.Frame(root)
headFrame.pack()
tk.Label(
	headFrame,
	text="Shop Simulator",
	fg="green",
	bg="black",
	font=("Times New Roman",100
		)
	).pack()
	


budgetFrame = tk.Frame(root)
budgetFrame.pack()

hint = "Enter you Budget.."

budget_entry = tk.Entry(
	budgetFrame,
	bd=1,
	relief="raised",
	bg="black",
	fg="red",
	width=30,
	font=("Times New Roman",30)
	)

budget_entry.insert(0,hint)

def on_entry_click(event):
	if budget_entry.get() == hint:
		budget_entry.delete(0,"end")
		budget_entry.config(fg="green")

def on_focusout(event):
	if budget_entry.get() == "":
		budget_entry.insert(0,hint)
		budget_entry.config(fg="red")

budget_entry.bind("<FocusIn>", on_entry_click)
budget_entry.bind("<FocusOut>", on_focusout)

budget_entry.grid(row=0, column=0, padx=5)


confirm_button = tk.Button(
	budgetFrame,
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



root.mainloop()
