# Question 2

number = float(input("Enter a number between 205 and 259: "))

while True:
    if number <= 205 or number >= 259:
        print("The number must be in the range.")
        number = float(input("Enter a number between 205 and 259: "))
    else:
        print("Thank you.")
        break

# I wasn't able to figure out a way to do this without while True or break
