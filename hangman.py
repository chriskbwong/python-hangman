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
