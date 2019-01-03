# Question 1

import random

randNum = 0
count = 0
numList = []

while randNum != 44:
    randNum = random.randint(11, 444)
    numList.append(randNum)
    count = count + 1

numList.sort()
print("Largest number generated:", numList[-1]) # The largest number is at
print("Number of iterations:", count) # the end of the list

# When ran three times, the largest numbers were: 444, 443, 441
# When ran three times, the number of iterations were: 287, 397, 356
