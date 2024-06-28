pattern = int(input("Enter the size of the pattern: "))

count = 0
while pattern > count:
    for i in range(1,pattern+1):
        print("*" , end='')
    print()
    count += 1