def cpu_chooses():
    #Tasked - Jose
    #Create a random number between 1 - 3 for CPU to choose and assign it to a variable 'cpur'
    pass

def player_chooses():
    #Tasked - Sonny
    #Ask User to choose Rock Paper or Scissors and save it as an int in variable 'r'
    player_0 = 'user'
    r = ''
    choices = input('Choose Rock Paper or Scissors: \n')
    if player_0 == 'Rock':
        print('user chooses Rock')
        player_0 = 'Rock'
        r = player_0
    elif player_0 == 'Paper':
         print('user chooses Paper')
         player_0 = 'Paper'
         r = player_0
    elif player_0 == 'Scissors':
        print('user chooses Scissors')
        player_0 = 'Scissors'
        r = player_0
    else:
        print('try again')




    #Remember it comes in as a string so you need to convert it as an int.
r = int(r)


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

