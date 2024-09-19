task = input("Enter your task:")
priority = input("Priority (high/medium/low):").lower()
time_bound = input("Is it time-bound? (yes/no):").lower()
match priority:
    case "high":
        if time_bound == "yes":
            print(f"Reminder: {task} is a high priority task that requires immediate attention today!")
        elif time_bound == "no":
            print(f"Note: {task} is a high priority task that requieres attention when you have time")
    case "medium":
        if time_bound == "yes":
            print(f"Reminder: {task} is a medium priority task that requires immediate attention today!")
        elif time_bound == "no":
            print(f"Note: {task} is a medium priority task that requieres attention when you have free time")
    case "low":
        if time_bound == "yes":
            print(f"Reminder: {task} is a low priority task that requires attention today!")
        elif time_bound == "no":
            print(f"Note: {task} is a low priority task that requieres attention when you have free time")
    case _:
        print("Wrong entry")