balance = 5000

print("1. Check Balance")
print("2. Deposit Money")
print("3. Withdraw Money")

choice = input("Enter your choice: ")

match choice:
    case "1":
        print("Your balance is:", balance)

    case "2":
        amount = float(input("Enter deposit amount: "))
        balance += amount
        print("Updated balance:", balance)

    case "3":
        amount = float(input("Enter withdrawal amount: "))
        if amount <= balance:
            balance -= amount
            print("Updated balance:", balance)
        else:
            print("Insufficient balance!")

    case _:
        print("Invalid choice!")