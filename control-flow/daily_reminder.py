task = input("Enter your task:")
p = input("Priority (high/medium/low):").lower()
t = input("Is it time-bound? (yes/no):").lower()
match p:
    case "high":
        if t == "yes":
            print(f"Reminder: {task} is a high priority task that requires immediate attention today!")
        elif t == "no":
            print(f"Note: {task} is a high priority task that requieres attention when you have time")
    case "medium":
        if t == "yes":
            print(f"Reminder: {task} is a medium priority task that requires immediate attention today!")
        elif t == "no":
            print(f"Note: {task} is a medium priority task that requieres attention when you have free time")
    case "low":
        if t == "yes":
            print(f"Reminder: {task} is a low priority task that requires attention today!")
        elif t == "no":
            print(f"Note: {task} is a low priority task that requieres attention when you have free time")
    case _:
        print("Wrong entry")