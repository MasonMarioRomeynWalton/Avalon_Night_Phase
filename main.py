#!/bin/python3                                                                  
from flask import *
from random import shuffle
from lib import information, pass_key
import time
                                                                                
app = Flask(__name__)                                                           

## The number of players to be played with
## Should make route that has this and characters as input to start game
number_of_players = 10

## The names of the players
players = []
pass_keys = {}
players_with_info_delivered = []

## Joins the game but doesn't give any info yet
@app.route('/')
def main():
    global player_information

    ## Get the players name from the http arguments if possible
    name = request.args.get('name')

    ## If that is not possible
    if not name:
        with open('lib/join_form.html', 'r') as f:
            return f.read()

    ## If we're still waiting on more people to join
    if number_of_players > len(players):

        if name in players:
            return 'You have already joined'
        else:
            players.append(name)

            ## If everyone has joined create the information
            if len(players) == number_of_players:
                player_information = information.create_info(players)

            ## Return message with js to store pass key locally in session data
            return 'You have succesfully joined'

    ## If enough people have already joined
    else:
        if name not in players:
            return 'You are not playing. You may need to launch a new game'

        ## Generate pass key for player
        generated_pass_key = pass_key.generate_pass_key()
        pass_keys[generated_pass_key] = name

        ## java script to retrieve pass key and get information from info/
        return pass_key.retrieve_info_with_pass_key_js()

## Gives the info
@app.route('/info')
def info():

    ## Get the players name from the http arguments if possible
    name = request.args.get('name')

    ## Get the players pass_key from the http arguments if possible
    pass_key = request.args.get('pass_key')

    ## If the player enters a passkey give them their info no matter what
    if pass_key and pass_key in pass_keys:
        name = pass_keys[pass_key]

        ## Keep track of players who have recieved info
        if name not in players_with_info_delivered:
            players_with_info_delivered.append(name)

        ## Return info for player with given pass_key
        return str(player_information[name])

    ## If players don't enter a passkey give their info only once
    else:

        ## If they don't submit a name, promt them
        if not name:
            with open('lib/join_form.html', 'r') as f:
                return f.read()

        else:
            if name not in players_with_info_delivered:
                ## Keep track of players who have recieved info
                players_with_info_delivered.append(name)

                ## Return info for player with given pass_key
                return str(player_information[name])
            else:
                return 'You may only access your night info once'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True, threaded=False)  
