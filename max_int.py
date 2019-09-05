num_int = 0
total = 0
max_int = 0

while True:
    num_int = int(input("Input a number: "))
    if num_int < 0:
        if total >= 0:
            print("The maximum number is", max_int)
        break
    total += num_int
# largest number calculation
    if max_int is 1:
        max_int = num_int
    elif max_int < num_int:
        max_int = num_int