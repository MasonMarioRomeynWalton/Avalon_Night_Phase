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

@app.route('/')
def main():
    global player_information
    name = request.args.get('name')

    ## If still in joining phase
    if number_of_players > len(players):

      ## Your name here will be the example name when the formatting is sent in chat
      if name == 'your_name_here' or not name:
          with open('lib/join_form.html', 'r') as f:
              return f.read()
      if name in players:
          return 'That name is already taken'
      else:
          players.append(name)
          ## If everyone has joined create the information
          if len(players) == number_of_players:
              player_information = information.create_info(players)

          ## Generate pass_key for player
          generated_pass = pass_key.generate_pass_key()
          pass_keys[generated_pass] = name

          ## Return message with js to store pass key locally in session data
          return 'You succesfully join' + pass_key.pass_key_js(generated_pass);

    ## If in the info phase
    else:
      if name not in players:
          return 'You are not playing'

      ## java script to retrieve pass key and get information from info/
      return pass_key.retrieve_info_with_pass_key_js()

# Gives the info
@app.route('/info')
def info():
    pass_key = request.args.get('pass_key')
    if pass_key:
        if pass_key in pass_keys:
            name = pass_keys[pass_key]
            # Keep track of players who have recieved info
            if name not in players_with_info_delivered:
                players_with_info_delivered.append(name)

            # Return info for player with given pass_key
            return str(player_information[name])
        else:
            return 'Your game has expired'
    else:
        return 'Please visit the home page with your name to get info'



if __name__ == '__main__':                                                      
    app.run(host='0.0.0.0', port=5000, debug=True, threaded=False)  
