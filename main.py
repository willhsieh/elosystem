from ratings import *
from games import *
from matchmaking import *

def main():
    print("Type 'a' to add game, 'l' to show leaderboard, 'm' to make teams")
    action = input()
    if action == 'a':
        addGame()
    elif action == 'l':
        printLeaderboard()
    elif action == 'm':
        make()
    else:
        print("Enter a valid character")

if __name__ == "__main__":
    main()


# TODO: split addGame into multiple functions
# def main():
#     # Initialize arrays
#     winplayers = [] # list of winning players
#     winacs = [] # list of winning player's ACS
#     winratings = [] # list of winning player's rating before the game
#     lossplayers = [] # list of losing players
#     lossacs = [] # list of losing player's ACS
#     lossratings = [] # list of losing player's rating before the game
#     newratings = [] # list of all player's ratings after the game

# if __name__ == "__main__":
#     main()