# 🛒 **Shop Simulator**

A **Python-based interactive shopping simulation** offering both **CLI** and **Tkinter GUI** modes. Designed for **Shopkeepers** to manage inventory and **Customers** to shop with budgets, carts, and billing — all powered by CSV-based storage!

---

## 📦 **Project Features**

| Feature    | CLI Version 🖥️                   | GUI Version 🖼️                   |
| ---------- | --------------------------------- | --------------------------------- |
| Interface  | Terminal-based                    | Graphical (Tkinter)               |
| User Modes | Shopkeeper & Customer             | Shopkeeper & Customer             |
| Inventory  | Managed via `Store.csv`           | Managed via `Store.csv`           |
| Cart       | Managed via `Cart.csv`            | Managed via `Cart.csv`            |
| Billing    | Subtotal + 15% Tax + Budget Check | Subtotal + 15% Tax + Budget Check |

---

## ▶️ **How to Run**

### 🧾 Command-Line Interface (CLI)

```bash
python3 ShopSimCLI.py
```

### 🖼️ Graphical User Interface (GUI)

```bash
python3 ShopSim_GUI.py
```

---

## 📁 **File Structure**

```
ShopSimulator/
│
├── ShopSimCLI.py        # CLI interface with embedded logic
├── ShopSim_GUI.py       # GUI interface using Tkinter
├── ShopSim_backend.py   # Backend logic & CSV data handling
├── Store.csv            # Persistent inventory database
└── Cart.csv             # Temporary shopping cart data
```

---

## 🔧 **Modules & Libraries Used**

* **`tkinter`** – GUI development (built-in)
* **`csv`** – CSV file manipulation (built-in)
* **`os`** – File existence & operations (built-in)

---

## 🧪 **Functional Overview**

### 🖥️ CLI Mode (`ShopSimCLI.py`)

* **Main Menu**: Select role – Shopkeeper or Customer.
* **Shopkeeper Workflow**:

  * Login with hardcoded credentials.
  * Perform inventory operations: add, update, delete, view.
* **Customer Workflow**:

  * Input shopping budget.
  * Browse items, manage cart.
  * Checkout with tax and budget validation.

🔁 *All logic is handled within this file.*

---

### 🖼️ GUI Mode (`ShopSim_GUI.py`)

* **Built with Tkinter**: User-friendly graphical flow.
* **Screens Include**:

  * Role selection
  * Shopkeeper login
  * Inventory management
  * Customer shopping & billing
* **Widgets**: Buttons, entry fields, tables, dialogs.
* **Dynamic Navigation**: Screen transitions by frame resets.
* **Event Handlers**: Use backend logic from `ShopSim_backend.py`.

---

### 🧠 Backend Logic (`ShopSim_backend.py`)

Handles **core functionalities and CSV data processing**:

#### 🛍️ Store Operations:

* `add_store_item()`
* `remove_store_item()`
* `update_store_item()`
* `get_store_items()`

#### 🛒 Cart Operations:

* `add_to_cart()`
* `remove_from_cart()`
* `update_cart_item()`
* `clear_cart()`

#### 💵 Billing & Validation:

* `calculate_bill()` — returns subtotal, tax, total.
* `process_payment()` — checks customer budget.
* Input checks for valid name, price, quantity.

#### 🔐 Authentication:

* `authenticate_shopkeeper(loginID, password)`

---

## 🤝 **Contributing**

Contributions are welcome! If you'd like to add features or fix bugs, feel free to fork this repo and submit a pull request.

---

## 📬 **Feedback**

If you find bugs or want new features, open an issue or drop a comment!

---
