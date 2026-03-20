import os
class player:
    def move(maze, score, turns, winRound):
        #getting player position
        for i in range(len(maze)):
            for j in range(len(maze[i])):
                if maze[i][j] == "T":
                    playerPos = [i,j]
        while True:
            #player can move by using wasd keys
            r = 0
            c = 0
            direction = input("\nEnter move(\"w\", \"s\", \"a\", or \"d\"): ")
            
            if direction == "w":
                r -= 1
            elif direction == "s":
                r += 1
            elif direction == "a":
                c -= 2
            elif direction == "d":
                c += 2
            else:
                print("Enter one of the direction options to move.")
                continue
            if (maze[playerPos[0]+r][playerPos[1]+(c//2)] == "#") or (maze[playerPos[0]+r][playerPos[1]+c] == "#"): #check if there's a border
                print("Can't move there!")
            elif (maze[playerPos[0]+r][playerPos[1]+(c//2)] == "@") or (maze[playerPos[0]+r][playerPos[1]+c] == "@"): #check if they reached the end
                os.system("cls" if os.name == "nt" else "clear")
                print("You found the portal!")
                winRound = True
                break
            else: #if area is clear
                if (maze[playerPos[0]+r][playerPos[1]+(c//2)] == "o") or (maze[playerPos[0]+r][playerPos[1]+c] == "o"): #check if there's a coin
                    score += 1
                
                #make the player actually move in the maze array
                maze[playerPos[0]][playerPos[1]] = " "
                maze[playerPos[0]][playerPos[1]+(c//2)] = " "
                maze[playerPos[0]+r][playerPos[1]+c] = "T"
                turns += 1
                break
        return maze, score, turns, winRound
