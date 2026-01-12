def showBalance(balance):
    print(f"Your current balance is: {balance:.2f}")

def deposit():
    amount = float(input("amount you want to deposit: "))

    if amount < 0:
        print("NO NEGATIVE NUMBER")
        return 0
    else:
        print("DEPOSIT SUCCESSFULLY")
        return amount
    
def withdraw(balance):
    amount = float(input("amount you want to withdraw: "))

    if amount < 0:
        print("NO NEGATIVE NUMBER")
        return 0
    elif amount > balance:
        print("INVALID")
        return 0
    else:
        print("WITHDRAW SUCCESSFULLY")
        return amount
    
isRunning = True

balance = 1000

while isRunning:
    print()
    print("Banking Program")
    print("[1] Show Balance")
    print("[2] Deposit")
    print("[3] Withdraw")
    print("[4] Exit")
    option = input("Enter your option (1, 2, 3, 4): ")

    if option == "1":
        showBalance(balance)
    elif option == "2":
        balance += deposit()
    elif option == "3":
        balance -= withdraw(balance)
    elif option == "4":
        print("SHUTTING DOWN")
        isRunning = False
    else:
        print("INVALID OPTION")

print("THANK YOU FOR USING!!!")