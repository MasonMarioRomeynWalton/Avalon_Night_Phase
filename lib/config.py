from random import shuffle,choice
import json


def create_config_info(names):
    #TODO: update this to be enterable
    file = open("lib/cleric.json", 'r')
    data = json.load(file)


    # Get the number of people
    number_people = 0
    number_people = data["people"]

    if len(names) != number_people:
        raise "not the right number of people"


    cards = data["cards"]
    
    # Initialize player list
    players = list()
    for i in range(number_people):
        players.append(list())
    
    for deck in cards:
        # Shuffle the deck
        shuffle(deck)
        i = 0
        # Give out cards in this deck to people until they run out
        while deck:
            players[i].append(deck.pop(0))
            i = i + 1
            if i == number_people:
                i = 0
        # Shuffle the players 
        #   (this is as not all decks need to be divisible by the numeber of players)
        shuffle(players)
    
    # Join names to players
    players = dict(zip(names, players))

    # Conglomerates properties and attributes for players
    player_props = {}
    player_attributes = {}
    for name in players:
        player_attributes[name] = {}

    for name, player_data in players.items():
        props = set
        for card in player_data:
            # Accumulate properties
            props = props.union(set(card["prop"]))

            # Set attributes.
            for description, attribute in card.items():
                if description != "prop":
                    # Note if multiple attributes are listed in 
                    #   multiple cards they will overwrite eachother
                    player_attributes[name][description] = attribute

        player_props[name] = props


    # Get knowledge for each subset of parameters listed
    knowledge = list()
    for sight in data["knowledge"]:
        text = ""
        for name in players:
            # If player has all of the props they are added to the list to be seen
            #   The players with all of the properties in sight["needs"] will see that they have 
            #   said properties and see any listed attributes that are seen with them
            if  set(sight["sees"]) <= player_props[name]:
                text += "You see " + name + " is"
                for prop in sight["sees"]:
                    text += ", " + prop 
                text += ". "
                if "info" in sight:
                    for description in sight["info"]:
                        text += "You see that for " + description + " they are " + player_attributes[name][description]
                text += "<br>";
        knowledge.append((set(sight["needs"]),text))

    # Construct information
    information = {}
    for name in names:
        information[name] = ""

        # Tells players what they have
        for card in players[name]:
            information[name] += "You are " + card["text"] + "!<br>"

        # Give info to those who meet the needed properties
        for sight in knowledge:
            if sight[0] <= player_props[name]:
                information[name]+= sight[1]
    
    return information
