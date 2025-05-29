**Shop Simulator**

A Python-based Shop Simulator application featuring both a command-line interface (CLI) and a graphical user interface (GUI) built with Tkinter for customers and shopkeepers to manage store inventory and shopping carts. The backend logic handles CSV file storage, item management, cart operations, and billing for the GUI but CLI have integrated backend and frontend.

*Project Overview*
This Shop Simulator supports two interfaces:
CLI Version: A terminal-based simulation for Shopkeeper and Customer modes.
GUI Version: A Tkinter-based graphical application for the same workflows.
Inventory and cart data are persisted in CSV files (Store.csv, Cart.csv).

*Running the Application*

CLI:
`python3 ShopSimCLI.py`

GUI:
`python3 ShopSim_GUI.py`

File Structure
`|── ShopSimCLI.py       # CLI interface script
├── ShopSim_GUI.py      # GUI interface script using Tkinter
├── ShopSim_backend.py  # Core logic and CSV file operations
├── Store.csv           # Persistent store inventory
└── Cart.csv            # Temporary shopping cart data`

*Modules & Libraries*
1. tkinter: Built-in library for creating GUIs.
2. csv: Built-in library for reading and writing CSV files.
3. os: Built-in library for file operations.

*Detailed Code Explanation*

*CLI (`ShopSimCLI.py`)
  Implements a command-line workflow:
  Main Menu: Choose Shopkeeper or Customer mode.
  Shopkeeper:
  Authenticate via hardcoded credentials.
  View, add, update, or remove items in Store.csv.
  Customer:
  Enter a shopping budget.
  Browse items, add/remove/update quantities in cart.
  Checkout calculates subtotal, 15% tax, grand total, and budget check.
  All CSV reads/writes call functions within the same file.

*GUI (`ShopSim_GUI.py`)
  Defines ShopSimulatorGUI class using Tkinter:
  Screens: Main role selection, shopkeeper login, inventory management, customer shopping interface.
  Widgets: Buttons, entries, tables, and scrollable frames.
  Navigation: Clears and rebuilds frames per screen.
  Dialog windows: For adding/removing/updating items and managing cart quantities.
  Event handlers invoke backend functions in `ShopSim_backend.py`.

*Backend (`ShopSim_backend.py`)
  Encapsulates data operations and business logic:
  Item class: Represents store items and serializes to CSV rows.
  Initialization: initialize_files() creates or resets Store.csv and Cart.csv.
  Store functions: CRUD operations on inventory (add_store_item, remove_store_item, etc.).
  Cart functions: add_to_cart, remove_from_cart, clear_cart with inventory adjustments.
  Validation: Input checks for price, quantity, and budget.
  Billing: calculate_bill() (subtotal, tax, total) and process_payment() (budget vs. total).
  Authentication: authenticate_shopkeeper(loginID, password).

