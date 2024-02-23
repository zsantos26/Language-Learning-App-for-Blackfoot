# Helper functions for Blackfoot project
# CMPT 120 
# Nov. 12, 2020

import random

# open translation files and assign variables 
file1 = open("Blackfoot to English Translations.csv")
file2 = open("Blackfoot to English Translations2.csv")
# create a dictionary with English to Blackfoot translations
dictionary1 = {}
for i in file1:
  splitData = i.strip().split(",")
  dictionary1[splitData [1].lower()] = splitData[0].lower()
# create a dictionary with Blackfoot to English translations
dictionary2 = {v: k for k, v in dictionary1.items()}

# create list for English words and Blackfoot words
englishWords = []
blackfootWords = []

# seperate Blackfoot and English words and add them to the lists
for i in file2:
  splitData = i.strip().split(",")
  blackfoot = splitData[0]
  blackfootLower = blackfoot.lower()
  blackfootWords += [blackfootLower]
  english = splitData[1]
  englishLower = english.lower()
  englishWords += [englishLower]

# initialize high scores for tests
highScoreTown1 = 0
highScoreTown2 = 0
highScoreRestaurant1 = 0
highScoreRestaurant2 = 0
highScoreHome1 = 0
highScoreHome2 = 0
highScoreFamily1 = 0
highScoreFamily2 = 0
highScoreGreetings1 = 0
highScoreGreetings2 = 0

# function for learning words 
# input: x - first element of scene relevant Blackfoot and English words, y - last element of scene relevant Blackfoot and English words
# output: none
def learn(x,y):
  print("\nSounds good! Look around for an English word"\
  " you would like to learn in Blackfoot. ")

  j = 0
  # while loop to translate English terms in scene to Blackfoot terms
  while j == 0:
    # ask user for English term 
    learn = ("\nWhat english phrase would you like to "\
    "learn? Type done to stop learning. ")

    print(learn)

    learnAnsLower = input().lower()

    # break from loop and stop learning if user types done
    if learnAnsLower == "done":
      break

    # check if input is in the scene
    # tell user that the input is not on the display if the input is not in scene
    elif learnAnsLower not in englishWords[x:y]:
      print("I'm sorry, that is not showing on the "\
      "display right now. ")
    
    # translate users input to Blackfoot
    else:
      translation1 = dictionary1[learnAnsLower].capitalize()
      print(translation1)

# function for testing user on Blackfoot words
# input: x - first element of scene relevant Blackfoot and English words, 
# y - last element of scene relevant Blackfoot and English words
# output: none
def test(x,y):
  global highScoreTown1
  global highScoreTown2
  global highScoreRestaurant1
  global highScoreRestaurant2
  global highScoreHome1
  global highScoreHome2 
  global highScoreFamily1
  global highScoreFamily2
  global highScoreGreetings1
  global highScoreGreetings2
  
  print("\nTest? Let's do it!\n")
  
  # explain rules for testing
  print("We have two types of tests. \nIn test number 1, "\
  "I will ask you 10 questions. I will randomly choose a "\
  "word in the scene for each question. You will then try "\
  "to respond with the correct English translation. At "\
  "the end, I will give you your score out of 10. \nIn "\
  "test number 2, I will display an English phrase and "\
  "two Blackfoot phrases. One of the Blackfoot words "\
  "corresponds to the English word. You must guess which "\
  "one is correct. There will be 10 questions and at the"\
  " end, I will give you your score out of 10.")

  j = 0
  # while loop for testing user
  while j == 0:
    # ask user if they want to do test 1 or test 2
    test = input("\nWould you like to do test number 1 (1)"\
    ", test number 2 (2), see high scores (high score) or "\
    "would you like to stop testing (stop) ? ")

    if test == "1":
      print("You have chosen test number 1.")
      
      # explain test 1 rules
      print("\nI will randomly choose a word in the "\
      "scene. You must then try to respond with the "\
      "correct English translation. ")
      
      # initialize current score 
      score = 0
      
      # initialize question number
      k = 0
      # while loop for first test. ask 10 questions
      while k < 10 :
        # choose random Blackfoot word specific to scene
        testWord = random.choice(blackfootWords[x:y])
        
        # choose English word that corresponds to the Blackfoot word
        answer = (dictionary2[testWord])
        
        # ask user for guess
        print("\nThe blackfoot phase is: " + testWord)
        
        testAnswer = input().lower()
        
        # check whether guess is correct or incorrect
        # add 1 to score if answer is correct
        if testAnswer == answer:
          print("Correct! ")
          score += 1
        
        else:
          print("Incorrect")
          
        # show the current score
        print("Your score is: " + str(score))
        
        # update high score if the current score is higher
        if x == 0:
          if score > highScoreTown1:
            highScoreTown1 = score
        elif x == 6:
          if score > highScoreRestaurant1:
            highScoreRestaurant1 = score
        elif x == 16:
          if score > highScoreHome1:
            highScoreHome1 = score
        elif x == 23:
          if score > highScoreFamily1:
            highScoreFamily1 = score
            return highScoreFamily1
        elif x == 29:
          if score > highScoreGreetings1:
            highScoreGreetings1 = score
            return highScoreGreetings1
        
        k += 1

    elif test == "2":
      print("You have chosen test number 2. ")

      # explain test 1 rules
      print ("In test number 2, I will display an English"\
      " phrase and two Blackfoot phrases. One of the "\
      "Blackfoot words corresponds to the English word. You"\
      " must respond with the correct answer.")
      # initialize current score
      score = 0

      # initialize question number
      k = 0
      # while loop for second test. ask 10 questions
      while k < 10 :
        # choose random English word specific to scene
        testWord = random.choice(englishWords[x:y])

        # choose Blackfoot word that corresponds to the English word
        answer = (dictionary1[testWord])

        # make a list consisting of the correct answer and an incorrect answer
        answerList = []

        answerList += [answer]

        # choose a Blackfoot word that is not the correct answer
        other = random.choice(blackfootWords[x:y])

        while other == answer:
          other = random.choice(blackfootWords[x:y])

        answerList += [other]

        print("\nThe english phrase is: " + testWord)

        # randomize order of possible answers
        random.shuffle(answerList)

        # ask user for guess
        print("The corresponding blackfoot word is "\
        "either: \n" + answerList[0] + " or " + answerList[1] + "\n")

        testAnswer = input().lower()

        # check whether guess is correct or incorrect
        # add 1 to score if answer is correct
        if testAnswer == answer:
          print("Correct! ")
          score += 1
          
        else:
          print("Incorrect")

        # show current score
        print("Your score is: " + str(score))

        # update high score if the current score is higher
        if x == 0:
          if score > highScoreTown2:
            highScoreTown2 = score
        elif x == 6:
          if score > highScoreRestaurant2:
            highScoreRestaurant2 = score
        elif x == 16:
          if score > highScoreHome2:
            highScoreHome2 = score
        elif x == 23:
          if score > highScoreFamily2:
            highScoreFamily2 = score
        elif x == 29:
          if score > highScoreGreetings2:
            highScoreGreetings2 = score
        
        k += 1

    # show high scores for test 1 and 2 for the current scene 
    elif test == "high score":
      if x == 0:
         print ("Your high score for test 1 is: " + \
         str(highScoreTown1) + "\nYour high score for "\
         "test 2 is: " + str(highScoreTown2))
      elif x == 6:
          print ("Your high score for test 1 is: " + \
          str(highScoreRestaurant1) + "\nYour high score "\
          "for test 2 is: " + str(highScoreRestaurant2))
      elif x == 16:
        print ("Your high score for test 1 is: " + \
        str(highScoreHome1) + "\nYour high score for test "\
        "2 is: " + str(highScoreHome2))
      elif x == 23:
        print ("Your high score for test 1 is: " + \
        str(highScoreFamily1) + "\nYour high score for "\
        "test 2 is: " + str(highScoreFamily2))
      elif x == 29:
        print ("Your high score for test 1 is: " + \
        str(highScoreGreetings1) + "\nYour high score for " \
        "test 2 is: " + str(highScoreGreetings2))
    
    # break loop and stop testing if user types stop
    elif test == "stop":
      break
