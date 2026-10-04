def check_balance():
    global balance
    print(f"Your balance is {balance}")

def deposit_cash(amount):
    global balance
    balance += amount
    print("Your amonut is Successfully deposited..")

def withdraw(amount):
    global balance
    if amount > balance:
        print("Insufficient Balance...")
    else:
        balance -= amount
        print("Withdrawal Successfully...")

def change_pin():
    global PIN
    new_pin = int(input("Enter new PIN: "))
    PIN = new_pin
    print("PIN is change successfully...")

def menu():
    print("=============== What do u want for today? =============\n\t\t(plz select an option)")
    print("1.. Change PIN")
    print("2.. Cash Withdrawal")
    print("3.. Deposit Cash")
    print("4.. Cash Enquiry")
    print("5.. Exit")


print("============== Welcome to ATM ================")
PIN = 12345
balance = 8000
attempts = 0
while attempts < 3:
    pin = int(input("Enter your PIN: "))
    if pin == PIN:
        break
    else:
        print("Wrong PIN.")
        attempts += 1

if attempts == 3:
    print("You exceeded 3 attempts. Account blocked for 24 hours.")
    exit()

while True:
    menu()
    choice = int(input("Select Your Option: "))
    if choice == 1:
        change_pin()
    elif choice == 2:
        drawal_amount = int(input("Enter the amount u wanna withdraw: "))
        withdraw(drawal_amount)
    elif choice == 3:
        deposit = int(input("Enter the amount u wanna Deposit: "))
        deposit_cash(deposit)
    elif choice == 4:
        check_balance()
    elif choice == 5:
        break
    else:
        print("Plz Enter the right choice...")

    again = input(("Do u wanna make another Transcation(Y/N): "))
    if again == "N":
        break

    




