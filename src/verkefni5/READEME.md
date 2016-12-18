- Þetta er ca. 40% komið það fór of mikill tími í að skipta um áætlun og grufla í glugga málum. (þá eru ótaldir mínusar fyrir copy past)
- all sources at https://github.com/gustavhjortur/python/tree/master/src/verkefni5
#Yatzy
##Assignmend deskription
Write a GUI for a game, such as Othello (Reversi), Mastermind or Yahtzee, using TkInter (or any other python GUI). More ideas for games can be found here.

Yatzy it is:
Lets create two files, yatzy.py for the game functionalty and yatzy.gameWindow.py for the display part. 
The logic of yatzy.py can be tested by running yatzy_test.py (The starter() at the bottom of yatzy.py has to be disabled)

"Worked" (if you can call this a game when you can not play it) worked on Fedora 20 Python3.3.2

## Left ToDo :
- Create actual game logic.(how to know who has the game, read dice, store, re-throw rest, add outcome to gameTable on players choice, decide on warnings.)
- Fix window update (usless as-is)
- Remove the -1 in score card for not used spots.
- Add "Name edit" in gameWindow.
- Add "Reset Game" function.
- Add "freez" on dice button for round two(part of first point)
##Next steps
- Add argparser to the startup to enter player names and display help.
- Rewrite gui for score bord (Ugli in every way).
- Create computer player.

Structure idea(dream):
Main logic <--> scorbord(gameWindow) <--> gameManager <--> player1
                                                      <--> player2
                                                      <--> ...
