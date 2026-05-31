grade = input("Enter your grade (A/B/C/D): ").upper()

match grade:
    case "A":
        print("Excellent!")
    case "B":
        print("Good Job!")
    case "C":
        print("Keep Improving!")
    case "D":
        print("Work Harder!")
    case _:
        print("Invalid Grade")