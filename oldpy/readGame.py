def readGame():
    with open('gamedata.txt', 'r') as file:
        prefix = file.readline(2)
        while prefix != 'G:':
            prefix = file.readline(2)

        line = file.readline();
        items = line.split(', ')

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



