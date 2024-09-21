from typing import List, Any

from triviaQuestRet import triviaQuestRet
player1Score = 0
player2Score = 0
turn: bool = True #If True p1 if False p2
triviaQuestions = triviaQuestRet()
for i in triviaQuestions:
    if turn == True:
        print("Question for the first player:")
    else:
        print("Qestion for the second player")
    print(str(i))
    selection =  int(input('Enter your solution (a number between 1 and 4): '))
    if selection == int(i.get_ca()):
        print("This is the correct answer.\n")
        if turn == True:
            player1Score +=1
        if turn == False:
            player2Score +=1
    else:
        print("That was incorrect. The correct answer is {}.\n".format(int(i.get_ca())))
    if turn == True:
        turn = False
    elif turn == False:
        turn = True
print("The first player earned {} points.".format(player1Score))
print("The second player earned {} points.".format(player2Score))
if player1Score > player2Score:
    win = "first"
else:
    win = "second"
print("The {} player wins the game.".format(win))