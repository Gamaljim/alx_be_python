task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

match priority:
    case 'high':
        f = f"{task} is a high priority task"
    case 'medium':
        f = f"{task} is a medium priority task"
    case 'low':
        f = f"{task} is a low priority task"
    case _:
        print(f'wrong text')

if time_bound == 'yes':
    print(f"{f} requires immediate attention today!")
elif time_bound == 'no':
    print(f"{f}. Consider completing it when you have free time.")
