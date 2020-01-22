#setup
Yes_No = ["Yes" , "No"]
directions = ["left" , "right" , "forward" , "backward"]
Dollar = 0
if Dollar > 1:
  "dollars!"
elif Dollar < 1:
      "dollar!"

#introduction
print ("Welcome to 'Candy Bar Adventure!' \n Press enter to continue.")
Answer = input()
print ("In this game, your quest is to buy a candy bar. Exit your house, navigate through the streets, and head to the store. \n Sadly you forgot your money and need to earn enough along the way to buy your treat. The candy bar costs 5 dollars. Good luck!")

#GAME: BEGIN
response = input()

response = input("Are you ready to begin? Type Yes or No to continue.\n")
while response not in Yes_No:
    response = input() # Hei kjære! #Hi, Peperkakemann!
if response == "Yes":
  print ("Let's begin! What is your character's name?")
  name = input()
  print(f"Welcome to the adventure, {name}")
  print("It's time to purchase a candybar.")
  Answer = input("^_^")
elif response == "No":
  print("Please join us again when you're ready to begin. Thank you.")
  quit()
else:
  print("Please restart the game because the creater doesn't know how to help you go back. Have fun reading all the boring text again. P.S. Great job following directions!")
  quit()

#GAME: First Trial
response = ""
while True:
  print("To your left, you see neighbor José walking his dog.")
  print("To your front, you see the road, free of cars for you to cross.")
  print("To your right, you see a squirrel being chased by a racoon.")
  print("Behind you, you see the locked front door to your house.\n")
  response = input("You leave your house. It's a sunny day and the neighbors are walking their dog. Which direction would you like to go? \n left \n right \n forward \n backward \n")
  if response == "left":
    print("You walk towards José and his dog Guapo.")
    Pause = input()
    print("José: Thanks for taking care of Guapo last week. Here's the money I owe you!")
    print("José gives you 1 dollar.")
    Pause = input()
    print("You're 1/5 of the way to the candy bar!")
    Dollar = Dollar + 1
    if Dollar > 1: print("You have" , Dollar , "dollars!")  
    elif Dollar <= 1: print("You have" , Dollar , "dollar!")
  elif response == "right":
    print("You walk towards the squirrel being chased by the racoon.")
    Pause = input()
    print("The racoon changes directions and comes for you.")
    Pause = input()
    print("You try to dodge him but you're too tasty of a meal to evade. You delicious piece, you.")
    Pause = input()
    print("The racoon bites you.\n You have rabies.\n You die.")
    quit()
  elif response == "forward":
    print("You walk forward. \n You step off the sidewalk. \n You look both ways just in case. \n Your head is still turned to watch for cars as you step off the curb. \n You gasp as your foot misses its next step--you've fallen into a pot hole.")
    Help = input("Would you like to scream for help? \n Yes \n No \n")
    while Help not in Yes_No: 
      print("No one can hear you scream those words.")
    if Help == "Yes":
      print("A big strong fireman comes to your rescue.")
      Pause = input()
      print("He lifts you into his strong, muscular arms and you feel yourself shiver at the contact.")
      Pause = input()
      print("You wonder what the point of this game is...\n Right! That candybar. \n You're looking for a different chocolate hunk.")
      Pause = input()
      print("He puts you back on your feet and walks you to the curb.")
      Pause = input()
      print("Fireman: Be careful where you step, " + name + ".")
      Pause = input()
      print("You sigh and watch him as he walks to help a wounded squirell.")
    if Help == "No":
      print("Your pride was your downfall.")
      Pause = input()
      print("You watch the heavens change above and your body whithers away to dust.")
      quit()
  elif response == "backward":
    print("You chose to go back indoors and forget about your candybar. \n You reevaluate your life and wonder whether you should be making your food instead of buying everything. \n You make your own chocolate!!")
    Pause = input()
    print("It's poisonous.")
    Pause = input()
    print("You die.")
    quit()