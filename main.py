import module1, module2, module3

#global variables
roundNum = 1
score = 0
turns = 0

#set up game
module1.game.opening()

#rounds with one maze each
while roundNum < 6:
    while True:
        if input("\nEnter \"start\" to begin Round " + str(roundNum) + ": ") == "start":
            module1.game.stats(score, turns, roundNum)
            maze = module2.mazes.getMaze(roundNum) 
            break
        else:
            print("Please enter the right thing to begin playing!")
    winRound = False
    while winRound == False:
        maze, score, turns, winRound = module3.player.move(maze, score, turns, winRound) #print player screen and make move
        if winRound: #check if player reached the end of the maze
            module1.game.winRoundStats(score, turns, roundNum) #print win screen
            roundNum += 1
            break
        else:
            module1.game.stats(score, turns, roundNum)
module1.game.end()
