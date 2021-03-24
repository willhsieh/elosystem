from games import *
from ratings import *

def make():
    # playerlist = []
    playerratings = []
    # totalsum = 0

    # Input all names
    for x in range(10):
        print("Player", x+1)
        currentPlayer = input()
        # playerlist.append(currentPlayer)
        # totalsum += lookupRating(currentPlayer)
        playerratings.append(lookupRating(currentPlayer))
    
    team1 = "Team 1: "
    team2 = "Team 2: "

    # Sort ratings
    playerratings.sort(reverse = True)

    # Snake draft
    i = 0
    team1 += lookupPlayer(playerratings[i])
    team1rating = playerratings[i]
    i += 1
    while i < 9:
        team1 += ", "
        team2 += lookupPlayer(playerratings[i])
        team2rating = playerratings[i]
        team2 += ", "
        i += 1

        team2 += lookupPlayer(playerratings[i])
        team2rating = playerratings[i]
        team2 += ", "
        i += 1

        team1 += lookupPlayer(playerratings[i])
        team1rating = playerratings[i]
        team1 += ", "
        i += 1

        team1 += lookupPlayer(playerratings[i])
        team1rating = playerratings[i]
        i += 1

    team2 += lookupPlayer(playerratings[i])
    team2rating = playerratings[i]

    # Probability of team 1 winning over team 2
    chance = round(expected(team1rating / 5, team2rating / 5), 3)
    chance = str(chance)

    # Print teams and chance of winning
    print(team1)
    print(team2)
    print ("Team 1 has a " + chance + " probability of winning versus Team 2.")
    return


# Returns a player's name given their rating
def lookupPlayer(rating):
    df = pd.read_csv("gameslog.csv")
    selected = df.loc[df['Rating'] == rating]
    return selected['Player'].to_string(index = False)
