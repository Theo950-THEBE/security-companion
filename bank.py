import tkinter as tk
from tkinter import messagebox
from datetime import datetime

# ============================================================
# BANKING SIMULATOR
# Educational/local demo — fictional bank and money only.
# ============================================================

root = tk.Tk()
root.title("NOVA BANK // DIGITAL BANKING")
root.geometry("950x600")
root.configure(bg="#07100d")
root.resizable(False, False)

# -----------------------------
# Fake account
# -----------------------------

ACCOUNT = {
    "name": "Alex Morgan",
    "account": "NOVA-482913",
    "balance": 12850.75,
    "pin": "2468",
}

transactions = [
    ("Opening balance", "+R12,850.75"),
]

# -----------------------------
# Colors
# -----------------------------

BG = "#07100d"
PANEL = "#0d1b16"
GREEN = "#00e58a"
WHITE = "#e8fff5"
GRAY = "#78958a"
RED = "#ff5555"

# -----------------------------
# Login screen
# -----------------------------

def login_screen():

    for widget in root.winfo_children():
        widget.destroy()

    frame = tk.Frame(root, bg=BG)
    frame.pack(expand=True)

    tk.Label(
        frame,
        text="NOVA BANK",
        fg=GREEN,
        bg=BG,
        font=("Arial", 32, "bold")
    ).pack(pady=20)

    tk.Label(
        frame,
        text="SECURE DIGITAL BANKING",
        fg=GRAY,
        bg=BG,
        font=("Consolas", 12)
    ).pack(pady=5)

    tk.Label(
        frame,
        text="Enter your PIN",
        fg=WHITE,
        bg=BG,
        font=("Arial", 14)
    ).pack(pady=(40, 10))

    pin_entry = tk.Entry(
        frame,
        show="●",
        width=18,
        justify="center",
        font=("Arial", 18)
    )

    pin_entry.pack()

    def login():

        if pin_entry.get() == ACCOUNT["pin"]:
            dashboard()

        else:
            messagebox.showerror(
                "Access denied",
                "Incorrect PIN."
            )

    tk.Button(
        frame,
        text="LOGIN",
        command=login,
        bg=GREEN,
        fg="black",
        font=("Arial", 12, "bold"),
        width=18,
        relief="flat"
    ).pack(pady=25)

    tk.Label(
        frame,
        text="DEMO ACCOUNT — NO REAL BANKING CONNECTION",
        fg="#53665e",
        bg=BG,
        font=("Consolas", 9)
    ).pack(pady=20)


# -----------------------------
# Dashboard
# -----------------------------

def dashboard():

    for widget in root.winfo_children():
        widget.destroy()

    # Header
    header = tk.Frame(root, bg=PANEL, height=70)
    header.pack(fill="x")

    tk.Label(
        header,
        text="NOVA BANK",
        fg=GREEN,
        bg=PANEL,
        font=("Arial", 22, "bold")
    ).pack(side="left", padx=25, pady=18)

    tk.Label(
        header,
        text=f"Welcome, {ACCOUNT['name']}",
        fg=WHITE,
        bg=PANEL,
        font=("Arial", 12)
    ).pack(side="right", padx=25)

    # Main
    main = tk.Frame(root, bg=BG)
    main.pack(fill="both", expand=True, padx=25, pady=25)

    # Balance card
    balance = tk.Frame(
        main,
        bg=PANEL,
        padx=30,
        pady=25
    )

    balance.pack(fill="x")

    tk.Label(
        balance,
        text="AVAILABLE BALANCE",
        fg=GRAY,
        bg=PANEL,
        font=("Consolas", 11)
    ).pack(anchor="w")

    balance_label = tk.Label(
        balance,
        text=f"R {ACCOUNT['balance']:,.2f}",
        fg=GREEN,
        bg=PANEL,
        font=("Arial", 32, "bold")
    )

    balance_label.pack(anchor="w", pady=5)

    tk.Label(
        balance,
        text=f"Account: {ACCOUNT['account']}",
        fg=GRAY,
        bg=PANEL,
        font=("Consolas", 10)
    ).pack(anchor="w")

    # Buttons
    buttons = tk.Frame(main, bg=BG)
    buttons.pack(fill="x", pady=20)

    def deposit():

        amount = amount_entry.get()

        try:
            amount = float(amount)

            if amount <= 0:
                raise ValueError

            ACCOUNT["balance"] += amount

            transactions.append(
                (
                    "Cash deposit",
                    f"+R{amount:,.2f}"
                )
            )

            balance_label.config(
                text=f"R {ACCOUNT['balance']:,.2f}"
            )

            refresh_transactions()

            amount_entry.delete(0, "end")

        except ValueError:
            messagebox.showerror(
                "Invalid amount",
                "Enter a valid positive amount."
            )

    def withdraw():

        amount = amount_entry.get()

        try:
            amount = float(amount)

            if amount <= 0:
                raise ValueError

            if amount > ACCOUNT["balance"]:
                messagebox.showerror(
                    "Transaction declined",
                    "Insufficient funds."
                )
                return

            ACCOUNT["balance"] -= amount

            transactions.append(
                (
                    "Cash withdrawal",
                    f"-R{amount:,.2f}"
                )
            )

            balance_label.config(
                text=f"R {ACCOUNT['balance']:,.2f}"
            )

            refresh_transactions()

            amount_entry.delete(0, "end")

        except ValueError:
            messagebox.showerror(
                "Invalid amount",
                "Enter a valid amount."
            )

    tk.Label(
        buttons,
        text="Amount:",
        fg=WHITE,
        bg=BG,
        font=("Arial", 11)
    ).pack(side="left")

    amount_entry = tk.Entry(
        buttons,
        width=15,
        font=("Arial", 12)
    )

    amount_entry.pack(side="left", padx=10)

    tk.Button(
        buttons,
        text="DEPOSIT",
        command=deposit,
        bg=GREEN,
        fg="black",
        relief="flat",
        font=("Arial", 10, "bold")
    ).pack(side="left", padx=5)

    tk.Button(
        buttons,
        text="WITHDRAW",
        command=withdraw,
        bg="#20352d",
        fg=WHITE,
        relief="flat",
        font=("Arial", 10, "bold")
    ).pack(side="left", padx=5)

    # Transactions
    history = tk.LabelFrame(
        main,
        text="  RECENT TRANSACTIONS  ",
        fg=GREEN,
        bg=BG,
        font=("Consolas", 11, "bold")
    )

    history.pack(fill="both", expand=True)

    transaction_box = tk.Text(
        history,
        bg="#030806",
        fg=WHITE,
        font=("Consolas", 11),
        bd=0
    )

    transaction_box.pack(
        fill="both",
        expand=True,
        padx=10,
        pady=10
    )

    def refresh_transactions():

        transaction_box.delete("1.0", "end")

        for description, amount in reversed(
            transactions[-10:]
        ):

            timestamp = datetime.now().strftime("%H:%M")

            transaction_box.insert(
                "end",
                f"{timestamp}   {description:<25} {amount}\n"
            )

    refresh_transactions()


# -----------------------------
# Start application
# -----------------------------

login_screen()

root.mainloop()