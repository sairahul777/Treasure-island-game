print('''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************''')

print("welcome to treasure island \nyour mission is to find treasure")
choice1=input("you are at a crossroad, where do you want to go? type left or right:").lower()
if choice1=="left":
    choice2=input('You have come to a lake.\nthere is a island in middle of the lake,\ntype "wait" to wait for a boat \nor "swim" to swim to across:').lower()
    if choice2=="wait":
          choice3=input('You have 3 doors to enter.\ntype "red" to choose red door,\ntype "blue" to choose blue door \nor type "yellow" to choose yellow door:').lower()
          if choice3=="red":
           print("Burned by fire.Game Over.")
          elif choice3=="blue":
           print("Eaten by beasts.Game Over.")
          elif choice3=="yellow":
           print("You Win!")
          else:
           print("Game over!!!")
    else:
     print("You got attacked by trout.Game Over. ")
else:
    print("You fell into a hole.Game Over.")
