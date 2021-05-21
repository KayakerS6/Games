Import random

print("Let's play a game!\nThe game is 21\nRules:\nThe first player may select any whole interger between 1 and 3\nThe second player may select any whole interger no more than 3 greater than the first player.\nExample:  Player 1 selects 2, Player 2 may select 3, 4 or 5")

game = int(0)
Menu = int(0)

def ComputerTurn(game):
    game = random.randrange((game + 1,game + 3,1)
    return(game)

def PlayerTurn(game)
    game = input("Select a number between " + game + 1 + " and " + game + 3 + ":  ")
    return(game)

def RandStart()
    Menu = random.randrange(1,2,1)
    return(menu)

def Playing(game)
    

while Menu < 4:
    input(int("Are you ready?\nWho will go first:\n1:  Me\n2:  You\n3:  Random"))
    if Menu == 1:
        ComputerTurn(game)
        '''game = random.randrange((game + 1,game + 3,1)
        return(game)'''
    elif Menu == 2:
        PlayerTurn(game)
        '''game = input("Select a number between " + game + 1 + " and " + game + 3 + ":  ")
        return(game)'''
    elif Menu == 3:
        RandStart()

