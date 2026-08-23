print("MENU")
print("1. Pizza")
print("2. Burger")
print("3. Salad")
print("4. Pasta")
print("5. Biryani")

choice = input("Enter your choice:")
match choice:
    case "1":
        print("Pizza. Bill: $15")
    case "2":
        print("Burger. Bill: $17")
    case "3":
        print("Salad. Bill: $12")
    case "4":
        print("Pasta. Bill: $22")
    case "5":
        print("Biryani. Bill: $27")
    case _:
        print("Not Available")