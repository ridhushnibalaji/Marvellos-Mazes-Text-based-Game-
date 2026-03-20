import module2
import os
class game:
    wizard = """               | 
              / \\      
  .||.       /\ /\\     
 \.''./      |','|    
 = .. =      | - | 
 / || \    ,-'\\"/,'`.   
   ||     ,'   /,.  `.  
   ,|____,' , ,;' \| |  
  (3|\    _/|/'   _| |  
   ||/,-''  | <-'' _,\\ 
   ||'      ==\\ ,-'  ,' 
   ||       |  V \\ ,|   
   ||       |    |` |   
   ||       |    |   \\  
   ||       |    \\    \\ 
   ||       |     |    \\
   ||       |      \\_,-'
   ||       |___,,--")_\\
   ||         |_|   ccc/
   ||        ccc/"""   
   
    defeatedWizard = """                 )
                  ) ' (
                 ( / \\ ,      
                .'/_ _\\ (     
  ( )          ).,|>,<|. )    
   \\\\          (_,| o |), ) 
    \\\\         ,-'\\"/,'`.   
     \\\\       ,'   /,.  `.  
      \\\\ ____,' , ,;' \\| |  
      (3|\    _/|/'   _| |  
       \ /,-''  | <-'' _,\\ 
       ||'      ==\\ ,-'  ,' 
       ||       |  V \\ ,|   
       ||       |    |` |   
       ||       |    |   \\  
       ||       |    \\    \\ 
       ||       |     |    \\
       ."       |      \\_,-'
     ( ' ( ,    |___,,--")_\\ '   .    , (
    ,.    (  .   '|_|  )ccc/(  .     )   "
   ("  "  )  )'  ) " ,     )   )  . (`     '`
 .; )  ' (( (" )    ;(,)    ((  (  ;)  "  )"
 _"., ,._'_.,)_(..,( . )_  _' )_') (. _..( '.."""\
    
    def opening():
        print(" ====================")
        print(" | MARVELO\'S MAZES  |")
        print(" ====================")
        #story
        print(game.wizard)
        print("\nSTORY:")
        print("Oh no! On your way to defeat the wizard Marvelo the Evil, \nhe transports you to a maze in an attempt to trap you. Get \nthrough each round to get back to his castle where you \ncan finally defeat him once and for all!")
        
        #instructions
        print("\nINSTRUCTIONS:")
        print("You are represented by the \"T\" character.")
        print("The \"#\"'s are walls you cannot cross.")
        print("You can enter either a \"w\", \"a\", \"s\", or \"d\" to move up, left, down, or right.")
        print("If you collect a coin represented by a \"o\", you can increase your score.")
        print("Try to get to the portal represented by \"@\" to get to the next round.")
        print("Good luck!")
    
    #printing stats for each turn
    def stats(score, turns, roundNum):
        os.system("cls" if os.name == "nt" else "clear")
        print("score: ", score, "     turns: ", turns)
        module2.mazes.printMaze(module2.mazes.getMaze(roundNum))

    #printing stats at the end of each round
    def winRoundStats(score, turns, roundNum):
        print(''' ____________________
|                    |''')
        print('''|{:^20}|'''.format("YOU BEAT ROUND " + str(roundNum)))
        print('''|{:^20}|'''.format("score: " + str(score)))
        print('''|{:^20}|'''.format("turns: " + str(turns)))
        print('''|____________________|''')
    
    #printing the final screen
    def end():
        print("\n\nYou defeated Marvelo the Evil, great job!")
        print(game.defeatedWizard)

        
        
        
        
        
        
        
