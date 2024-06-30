task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

f = 'yea'
if priority == 'high':
    f = f"{task} is a high priority task"
elif priority == 'medium':
    f = f"{task} is a medium priority task"
elif priority == 'low':
    f = f"{task} is a low priority task"
else:
    print(f'wrong text')

if time_bound == 'yes':
    print(f"{f} requires immediate attention today!")
elif time_bound == 'no':
    print(f"{f}. Consider completing it when you have free time.")
