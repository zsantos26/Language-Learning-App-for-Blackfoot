# CMPT 120 - Final Project
# Name - Zeth Santos
# Date - December 7, 2020
# Description - Final Project - Audio-Visual Language Learning App for Blackfoot

import helper
import cmpt120image

# get 2d array of RGB values for images and assign images to variables
imgTown = cmpt120image.getImage("images/town.jpg")
imgRestaurant = cmpt120image.getImage("images/restaurant.jpg")
imgHome = cmpt120image.getImage("images/home.jpg")
imgFamily = cmpt120image.getImage("images/family.jpg")
imgGreetings = cmpt120image.getImage("images/greetings.jpg")


greetings = ("Hello, welcome to Brocket, Alberta! If you would like, I can teach you some Blackfoot.")

# tell user their options
activities = ("\nWould you like to learn of the "\
"words around you (learn), take a test (test), see your "\
"test high scores (high scores), move to somewhere else "\
"(move) or exit (exit)")

print(greetings)

# initialize Blackfoot and English words for Town scene
x = 0
y = 6
i = 0
# main while loop for moving between scenes
while i == 0:
  # start on Town scene
  if x == 0:
    cmpt120image.showImage(imgTown, "Town")

  # ask user for what activity they want to do
  print(activities)
  
  ans = input()

  # if answer is learn, run learn function depending on scene
  if ans == ("learn"):
    helper.learn(x,y)
  
  # if answer is test, run test function depending on scene
  elif ans == ("test"):
    helper.test(x,y)

  # if answer is high scores, show high scores for all tests
  elif ans == ("high scores"):
    print("Your high score for Town test 1 is: " + \
    str(helper.highScoreTown1) + "\nYour high score for"\
    " Town test 2 is: " + str(helper.highScoreTown2))

    print("Your high score for Resturant test 1 is: " + \
    str(helper.highScoreRestaurant1) + "\nYour high score"\
    " for Resturant test 2 is: " + str(helper.highScoreRestaurant2))

    print("Your high score for Home test 1 is: " + \
    str(helper.highScoreHome1) + "\nYour high score for"\
    " Home test 2 is: " + str(helper.highScoreHome2))

    print("Your high score for Family test 1 is: " + \
    str(helper.highScoreFamily1) + "\nYour high score for"\
    " Family test 2 is: " + str(helper.highScoreFamily2))

    print("Your high score for Greetings test 1 is: " + \
    str(helper.highScoreGreetings1) + "\nYour high score"\
    " for Greetings test 2 is: " + str(helper.highScoreGreetings2))
    
  #if answer is move, ask user where they want to go
  elif ans == ("move"):
    print("Where would you like to go? Town (town)"\
    " restaurant (restaurant), home (home), family"\
    " (family) or greetings (greetings)") 

    move = input().lower()

    # change display image and relevant English and Blackfoot words based on answer
    if move == "town":
      x = 0
      y = 6
      showTown = cmpt120image.showImage(imgTown, "Town")
      showTown
    if move == "restaurant":
      x = 6
      y = 16
      showRestaurant = cmpt120image.showImage(imgRestaurant, "Restaurant")
      showRestaurant
    if move == "home":
      x = 16
      y = 23
      showHome = cmpt120image.showImage(imgHome, "Home")
      showHome
    if move == "family":
      x = 23
      y = 29
      showFamily = cmpt120image.showImage(imgFamily, "Family")
      showFamily
    if move == "greetings":
      x = 29
      y = 38
      showGreetings = cmpt120image.showImage(imgGreetings, "Greetings")
      showGreetings

  # if answer is exit, break from while loop and say goodbye
  elif ans == ("exit"):
    print("I hope you enjoyed your stay. Goodbye! ")
    break