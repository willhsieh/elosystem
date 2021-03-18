def Players():
    p_list = []
    with open('gamedata.txt', 'r') as file:
        line = file.readline() # skip first line 'Players:'
        line = file.readline()
        line = line.strip('\n')
        while line != '':
            p_list.append(line)
            line = file.readline()
            line = line.strip('\n')

    return p_list


def SelectPlayer():
    Players() # TODO: make this autofill with tab
    player = input('Enter player name: ')
    return player

    