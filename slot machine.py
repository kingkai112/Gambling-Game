# banking and slot machine combine

import random

#  Banking Features
def show_balance(balance):
    print(f"\n💰 Your balance is NRS. {balance:.2f}\n")

def deposit(balance):
    amount = float(input("Enter the amount you want to deposit: "))
    if amount <= 0:
        print("⚠️ Invalid deposit amount")
        return balance
    balance += amount
    print(f"✅ Deposited NRS. {amount:.2f}")
    return balance

def withdraw(balance):
    amount = float(input("Enter the amount you want to withdraw: "))
    if amount <= 0:
        print("⚠️ Invalid withdrawal amount")
    elif amount > balance:
        print("⚠️ Not enough balance")
    else:
        balance -= amount
        print(f"✅ Withdrew NRS. {amount:.2f}")
    return balance

# Slot Machine 
def spin_row():
    symbols = ["🍒", "🍉", "🔔", "⭐", "🍌"]
    return [random.choice(symbols) for _ in range(3)]

def print_row(row):
    print(" | ".join(row))

def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == "🍒":
            return bet * 3
        elif row[0] == "🍉":
            return bet * 4
        elif row[0] == "🔔":
            return bet * 2
        elif row[0] == "⭐":
            return bet * 10
        elif row[0] == "🍌":
            return 0
    return 0

def play_slot_machine(balance):
    print("\n************************")
    print("🎰 Welcome to Slot Machine")
    print("Symbols: 🍒 🍉 🔔 ⭐ 🍌")
    print("************************")

    while True:
        print(f"💰 Current balance: NRS. {balance:.2f}")
        bet = input("Place your bet amount (or 'q' to quit): ")

        if bet.lower() == 'q':
            break

        if not bet.isdigit():
            print("⚠️ Please enter a valid number")
            continue

        bet = int(bet)

        if bet <= 0:
            print("⚠️ Bet must be greater than 0")
            continue
        if bet > balance:
            print("⚠️ Not enough balance to place that bet")
            continue

        balance -= bet
        row = spin_row()
        print("\nSpinning...\n")
        print_row(row)

        payout = get_payout(row, bet)
        if payout > 0:
            print(f"🎉 You won NRS. {payout}")
        else:
            print("😢 You lost this round")

        balance += payout

    return balance

# ----------------- Main Program -----------------
def main():
    balance = 0
    running = True

    while running:
        print("\n====================")
        print("🏦 Banking & Gambling Menu")
        print("====================")
        print("1. Show Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Play Slot Machine 🎰")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            show_balance(balance)
        elif choice == '2':
            balance = deposit(balance)
        elif choice == '3':
            balance = withdraw(balance)
        elif choice == '4':
            balance = play_slot_machine(balance)
        elif choice == '5':
            running = False
        else:
            print("⚠️ Not a valid choice")

    print("🙏 Thank you for using our program!")

if __name__ == '__main__':
    main()
