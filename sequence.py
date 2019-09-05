n = int(input("Enter the length of the sequence: "))
num1 = 1
num2 = 2
num3 = 3
counter = 0
i = 1
for i in range(1, n+1):
    if 1 <= i <= 3:
        print(i)
    else:
        total = num1 + num2 + num3
        num1 = num2
        num2 = num3
        num3 = total
        print(total)