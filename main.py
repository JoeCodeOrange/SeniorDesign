import random

def win_lose(cpur,r):
    if cpur == 1 and r == 2:
        print("User Wins The Game")
    elif cpur == 1 and r == 3:
        print("Computer Wins The Game")
    elif cpur == 1 and r == 1:
        print("ITS A TIE")
    elif cpur == 2 and r ==1:
        print("User Wins The Game")
    elif cpur == 2 and r ==2:
        print("ITS A TIE")
    elif cpur == 2 and r ==3:
        print("User Wins The Game")
    elif cpur == 3 and r ==1:
        print("User Wins The Game")
    elif cpur == 3 and r ==2:
        print("Computer Wins The Game")
    elif cpur == 3 and r ==3:
        print("ITS A TIE")


def player_chooses(r):
    #Tasked - Sonny
    #Ask User to choose Rock Paper or Scissors and save it as an int in variable 'r'
    while r > 3 or r < 1:
        print("Please Choose 1 for Rock, 2 for Paper, 3 for Scissors")
        r = input('Choose Rock Paper or Scissors: \n')
        r = int(r)
    
    return r

############## Welcome Section ###############
print("\n#####################################")
print("#                                   #")
print("# Welcome to Rock, Paper, Scissors! #")
print("#  Rock = 1 Paper = 2 Scissors = 3  #")
print("#                                   #")
print("#####################################")


replay = ""

while True:
    r = input('Choose Rock Paper or Scissors: \n')
    r = int(r)
    cpur = random.randint(1, 3) # Jose's Work
    player_chooses(r)
    win_lose(cpur,r)
    replay = input('Would you like to play again?')
    if replay == "n" or replay == "N":
        break
    


print("Thanks for playing!")






#Tasked - Joe
#I will be finish the basic program

