from random import shuffle,choice

def create_info(names):

    ## Decide what characters are in play
    characters = []

    ## Fill the names with VTs
    for i in range(0,len(names)):
        characters.append('vt')
        
    characters[0] = 'Merlin'
    characters[1] = 'Percival'
    characters[2] = 'Lunatic'
    characters[3] = 'Morgana'
    characters[4] = 'Oberon'
    characters[5] = 'Mordred'

    ## Shuffle the cards and assign them to players
    shuffle(characters)
    characters = dict(zip(names,characters))

    ## Randomly decide who goes first
    first_player = choice(names)

    ## Get the alignments of the players
    evils = ['Assassin','Morgana','Mordred','Oberon','Lunatic']
    alignment = {}
    for name in names:
        if characters[name] in evils:
            alignment[name] = 'evil'
        else:
            alignment[name] = 'good'

    ## Determine what their information should be
    information = {}
    for name in names:
        information[name] = 'You are ' + characters[name] + '!<br>'

        if alignment[name] == 'evil' and characters[name] != 'Oberon':
            for name_seen in names:
                if alignment[name_seen] == 'evil' and characters[name_seen] != 'Oberon':
                    information[name] += name_seen + ' is one of your fellow evils<br>'
        
        if characters[name] == 'Merlin':
            for name_seen in names:
                if alignment[name_seen] == 'evil' and characters[name_seen] != 'Mordred':
                    information[name] += 'You see ' + name_seen + ' as evil<br>'

        if characters[name] == 'Percival':
            for name_seen in names:
                if characters[name_seen] == 'Merlin' or characters[name_seen] == 'Morgana':
                    information[name] += name_seen + ' is either Merlin of Morgana<br>'
        if name == first_player:
            information[name] += 'You go first<br>'
    return information
