#file name : CS112_A1_T2_GameNumber(1)_20230425.py.
# purpose : two players will take turns adding numbers from 1 to 10 and the player who reaches 100 first will be the winner
# name :منة مصطفي محمد عثمان أحمد القللي
#ID: 20230425



# welcome message
print("Welcome to 100 game")

# how the game will display
num1 = 0
num2 = 0

while num1 < 100 and num2 < 100:
    try:

     move1 = int(input("Player1: Please enter a number from 1 to 10.\n"))
    except ValueError:

     move1 = int(input("please enter a valid number from 1 to 10 \n"))

    while move1 > 10 or move1 < 0:
     try:

      move1 = int(input("Sorry, you must enter a number from 1 to 10.\nTry again.\n"))
     except ValueError:
      move1 = int(input("please enter a valid number from 1 to 10 \n"))


    num1 = move1 + num2

    while num1 > 100:
        num1 = num1 - move1
        move1 = int(input("Player 1: Please enter another number.\n"))
        num1 = num2 + move1
    print("sum is",num1)

    if num1 == 100:
        print("Player 1 is the winner")
        break



    try:

     move2 = int(input("Player2: Please enter a number from 1 to 10.\n"))

    except ValueError:

     move2 = int(input("please enter a valid number from 1 to 10 \n"))
    num2 = num1 + move2


    while move2 > 10 or move2 < 0:
        try :

         move2 = int(input("Sorry, you must enter a number from 1 to 10.\nTry again.\n"))
        except ValueError:
         move2 = int(input("please enter a valid number from 1 to 10 \n "))

    num2 = move2 + num1

    while num2 > 100:
        num2 = num2 - move2
        move2 = int(input("Player 2: Please enter another number.\n"))
        num2 = num1 + move2
    print("sum is", num2)

    if num2 == 100:
        print("Player2 is the winner")



