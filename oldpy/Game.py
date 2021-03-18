from Players import SelectPlayer

def addGame():
    with open('gamedata.txt', 'a') as file:
        player = SelectPlayer()
        print('Enter data here: Game #, ACS, Kills, Deaths, Assists, Rounds Won, Rounds Lost')
        line = 'G: ' + player + ', ' + input()
        file.write(line + '\n')


def readGame():
    with open('gamedata.txt', 'r') as file:
        prefix = file.readline(3)
        while prefix != 'G: ':
            prefix = file.readline(3)

        g_line = file.readline()
        items = g_line.split(', ')

        gamenum = int(items[0])
        acs = int(items[1])
        kills = int(items[2])
        deaths = int(items[3])
        assists = int(items[4])
        roundswon = int(items[5])
        roundslost = int(items[6])

        print(gamenum)
        print(acs)
        print(kills)
        print(deaths)
        print(assists)
        print(roundswon)
        print(roundslost)
