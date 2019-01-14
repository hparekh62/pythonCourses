# Question 1

try:
    #fileIn = open("Lottery_Winning_Numbers SHORT.txt", "r")
    fileIn = open("Lottery_Winning_Numbers.txt", "r")
except:
    print("The file does not exist or cannot be found.")
else:
    lineCount = 0
    lottery = dict()
    for line in fileIn:
        lineCount = lineCount + 1 # The number of lines is the number of complete winning number series
        lotteryData = line.split(",")
        series = lotteryData[1]
        winningNums = series.split()
        for num in winningNums:
            lottery[num] = lottery.get(num, 0) + 1

    winList = list() # Need to do this step to sort keys
    for (key, val) in lottery.items(): # This method is in the example shown in Sunday Session 11/4
        winList.append((key, val))
    winList.sort()
    print("There are", lineCount, "complete winning numbers.")
    for (key, val) in winList:
        print((key, val))

    fileIn.close()

# I tried to pop the tuples created from the first line in the file
# but I couldn't figure out how to do it.
