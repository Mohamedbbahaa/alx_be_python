size = int(input("Enter the size of the pattern:"))
i = 1
j = 1
while j <= size:
    while i <= size:
        print("*", end="")
        i += 1
    print("")
    j +=1
    i = 1