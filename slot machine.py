import random
def spin_row():
    symbols = ["🍒" ,"🍉", "🔔", "⭐", "🍌"]
    return [random.choice(symbols) for _ in range(3)]
# can also be done using for loop

def print_row(row):
    print(" | ".join(row)) # join each element with a space 

def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == "🍒":
            return bet * 3
        elif row[0] == "🍉":
            return bet * 4
        elif row[0] == "🔔":
            return bet *2
        elif row [0] == "⭐":
            return bet * 10
        elif row[0] == "🍌":
            return bet * 0 
    return 0
    
def main():
    balance = 1000000000000000
    print("************************")
    print("Welcome to Slot machines")
    print("Symbols 🍒 🍉 🔔 ⭐ 🍌")
    print("************************")
    print("Dont give up, you're a dollar away from GAZILLION DOLLARS!!")
    print("************************")
    
    while balance > 0:
        print(f"Current balance: ${balance}")
        bet = input("Place your bet amount: ")
        
        if not bet.isdigit(): # this checks is the input is anything other than a number
            print("Please enter a valid number")
            continue #skips current iteration and starts from beginning
    
        bet = int(bet) # type casting bet to integer because the input area above takes string 
        
        if bet > balance:
            print("You do not have enough balance to place a bet")
            continue
        
        if bet <= 0:
            print("Lost all your money? Dont quit yet :))")
            continue
        
        balance -= bet
        row = spin_row() # spin row will be a list 
        print("Spinning...\n")
        print_row(row)
        
        payout = get_payout(row, bet)
        if payout > 0:
            print(f"You won ${payout}")
        else:
            print("You lost this round")
        balance += payout 
        play_again = input("Do you want to spin again? (y/n)").lower()
        
        if play_again != 'y':
            break
        
    print(f"Game over! Your final balance is ${balance}")
        
if __name__ == '__main__':
    main()
    