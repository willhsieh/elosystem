import pandas as pd
from ratings import *

# Sort CSV by rating
def rankAll():
    # https://www.usepandas.com/csv/sort-csv-data-by-column
    df = pd.read_csv("gameslog.csv")
    sorted_df = df.sort_values(by=["Rating"], ascending = False)
    sorted_df.to_csv("gameslog.csv", index = False)
    return sorted_df
    
# Add game
def addGame():
    winplayers = []
    winacs = []
    winratings = []
    lossplayers = []
    lossacs = []
    lossratings = []
    newratings = []
    
    # Winning team
    for x in range(5):
        print("Winning player", x+1)
        currentPlayer = input()
        winplayers.append(currentPlayer)

        print("ACS", x+1)
        currentACS = int(input())
        winacs.append(currentACS)

        winratings.append(lookupRating(currentPlayer))

    # Losing team
    for x in range(5):
        print("Losing player", x+1)
        currentPlayer = input()
        lossplayers.append(currentPlayer)

        print("ACS", x+1)
        currentACS = int(input())
        lossacs.append(currentACS)

        lossratings.append(lookupRating(currentPlayer))

    
    # Calculate ratings for each winning player
    count = 0
    for x in winplayers:
        rating = lookupRating(x)
        newratings.append(newRating(rating, winacs[count], lossratings[0], lossratings[1], lossratings[2], lossratings[3], lossratings[4], "win"))
        count += 1
    
    count = 0
    for x in lossplayers:
        rating = lookupRating(x)
        newratings.append(newRating(rating, lossacs[count], winratings[0], winratings[1], winratings[2], winratings[3], winratings[4], "loss"))
        count += 1

    # Update file
    df = pd.read_csv("gameslog.csv")
    count = 0
    for i in winplayers:
        row = df[df['Player'] == i].index[0]
        df.at[row, 'Rating'] = newratings[count]
        df.at[row, 'Games'] = df.at[row, 'Games'] + 1
        count += 1
    for i in lossplayers:
        row = df[df['Player'] == i].index[0]
        df.at[row, 'Rating'] = newratings[count]
        df.at[row, 'Games'] = df.at[row, 'Games'] + 1
        count += 1
    df.to_csv('gameslog.csv', index = False)

    rankAll()
    return


# Returns a player's rating given their name
def lookupRating(player):
    df = pd.read_csv("gameslog.csv")
    selected = df.loc[df['Player'] == player]
    return int((selected['Rating'].to_string(index = False)), base=10)

def printLeaderboard():
    df = pd.read_csv("gameslog.csv")
    print(df)
    return