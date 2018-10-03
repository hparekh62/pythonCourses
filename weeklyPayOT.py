# This program calculates salaries

def payCalc(payRate, hoursWorked):
    if hoursWorked > 40:
        hoursOT = hoursWorked - 40
        payOT = hoursOT * (payRate * 1.5)
        payTotal = payOT + (payRate * 40)
        print("The total pay is: $", round(payTotal, 2)) # Currency formatting
        # Only works with print. This doesn't work: return payTotal
    else:
        payTotal = payRate * hoursWorked
        print("The total pay is: $", round(payTotal, 2)) # Currency formatting
        # Only works with print. This doesn't work: return payTotal

payRate = float(input("Enter the pay rate: $"))
hoursWorked = float(input("Enter the hours worked: "))
payCalc(payRate, hoursWorked)
# This doesn't work: print("The total pay is: $", payTotal)

# I'm not sure when and when not to use return
