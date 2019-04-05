import random 
// made by chris wong, dax fulton and taiga hoeft
wordBank = ["cooing", "pytoon", "coolmathgames", "jooce"]
bankChoice = random.randint(0,len(wordBank)-1)
word = wordBank[bankChoice]
wordList = list(word)
blankList = []
missCount = 0
missList = []

for i in range (0,len(wordList)):
  blankList.append("_")

play = True
while(play):
  print(blankList)
  playerGuess = input("What letter would you like to guess?")
  doubleCheck = True
  if (playerGuess in wordList):
    while(doubleCheck):
      rIndex = wordList.index(playerGuess)
      blankList[rIndex] = wordList[rIndex]
      wordList[rIndex] = "!"
      #print(wordList)
      if (playerGuess not in wordList):
        doubleCheck = False
  else: 
    missList.append(playerGuess)
    missCount += 1
    print ("Letters not in word: ", missList)
    print ("You've guessed wrong ", missCount, " times")
  
  if ("_" not in blankList):
    print("You managed to win :)")
    play = False
  if (missCount >= 10):
    print("You're a loser :(")
    play = False
