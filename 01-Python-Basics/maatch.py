day = input("Enter a day of the week: ")

match day:
    case "Monday":
        print("Start of the week!")
    case "Tuesday":
        print("Keep going!")
    case "Wednesday":
        print("Halfway through the week!")
    case "Thursday":
        print("Almost there!")
    case "Friday":
        print("Weekend is coming!")
    case "Saturday":
        print("Enjoy your weekend!")
    case "Sunday":
        print("Holiday!")
    case _:
        print("Please enter a valid day.")