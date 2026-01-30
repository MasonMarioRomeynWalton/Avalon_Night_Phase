#!/bin/python3                                                                  
from flask import *
from random import shuffle
from lib import information
import time
                                                                                
app = Flask(__name__)                                                           

## The number of players to be played with
## Should make route that has this and characters as input to start game
number_of_players = 10

## The names of the players
players = []
players_with_info_delivered = []

@app.route('/')
def main():
    global player_information
    name = request.args.get('name')

    ## If still in joining phase
    if number_of_players > len(players):

      ## Your name here will be the example name when the formatting is sent in chat
      if name == 'your_name_here':
          return 'Put your name where it says your_name_here'
      if name in players:
          return 'That name is already taken'
      else:
          players.append(name)
          ## If everyone has joined create the information
          if len(players) == number_of_players:
              player_information = information.create_info(players)
          return 'You succesfully join'

    ## If in the info phase
    else:
      if name not in players:
          return 'You are not playing'
      if name in players_with_info_delivered:
          return 'Someone has already gotten your information'

      players_with_info_delivered.append(name)

      return str(player_information[name])

if __name__ == '__main__':                                                      
    app.run(host='0.0.0.0', port=5000, debug=True, threaded=False)  
