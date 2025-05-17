# python_projects
1. # 🛒 Shop Simulator

A terminal-based Python application that simulates a shop environment with two modes: **Shopkeeper** and **Customer**. Inventory and cart data are handled using CSV files.

---

## 📌 Features

### 🧑‍💼 Shopkeeper Mode
- Secure login access
- View available inventory
- Add new items to the store
- Update item price or quantity
- Remove items from inventory
- Persistent store data (`Store.csv`)

### 🧑‍🛒 Customer Mode
- Enter a shopping budget
- View all available store items
- Add items to cart with stock validation
- Remove or update cart items
- Generates a bill with 15% tax
- Budget check with change/refund
- Automatic cart-to-store return on exit

---

## 🗂️ File Structure

- `Store.csv` → Contains store inventory (persistent)
- `Cart.csv` → Contains customer cart (temporary)

---

## 🚀 Getting Started

### ✅ Requirements
- Python 3.x
- No external libraries needed (uses `csv` and `os`)

### ▶️ Run the Script

```bash
python shop_simulator.py
