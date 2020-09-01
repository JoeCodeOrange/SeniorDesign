import random

def cpu_chooses():
    #Tasked - Jose
    #Create a random number between 1 - 3 for CPU to choose and assign it to a variable 'cpur'
    cpur = random.randint(1, 3)
    print(cpur)

def player_chooses():
    #Tasked - Sonny
    #Ask User to choose Rock Paper or Scissors and save it as an int in variable 'r'
    #Remember it comes in as a string so you need to convert it as an int.
    pass

############## Welcome Section ###############
print("\n#####################################")
print("#                                   #")
print("# Welcome to Rock, Paper, Scissors! #")
print("#  Rock = 1 Paper = 2 Scissors = 3  #")
print("#                                   #")
print("#####################################")

cpu_chooses()
player_chooses()

#Tasked - Joe
#I will be finish the basic program

