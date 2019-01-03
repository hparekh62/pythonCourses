# Question 3

wordList = []
wordCount = int(input("How many words would you like to enter? : "))

for i in range(wordCount): #i = storeIndex
    userWord = str(input("Enter a word: "))
    wordCheck = 0
    wordCheck = userWord.count(" ")
    if wordCheck > 0: #i.count(" ") > 1 #wordCheck > 1
        #print("You may only enter one word at a time.")
        print("You may only enter one word at a time. Try again.")
        i = i - 1
        #get input again
        userWord = str(input("Enter a word: "))
        wordList.append(userWord)
    else:
        wordList.append(userWord)

sentence = " ".join(wordList)
print(sentence)
