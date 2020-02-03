# -*- coding: utf-8 -*-
"""
Created on Tue Jan 18 2020

@author: Ashley Pettibone
"""

import Dominion
import testUtility
import random
from collections import defaultdict

from pettiboa.dominion.testUtility import getPlayerNames, getVictoryCards, getCurseCards

player_names = getPlayerNames()

# introduced bug here
# I changed the number of victory cards you can have in a 2 and 4 player game
# 2 players is now 10 and > 2 is 14
#I fixed the bug for testing
# number of curses and victory cards
nV = getVictoryCards(player_names)

nC = getCurseCards(player_names)

# Define box
box = testUtility.GetBoxes(nV)
supply_order = testUtility.getSupplyOrder()

# Pick 10 cards from box to be in the supply.
boxlist = testUtility.GetBoxList(box, nV, nC, player_names)

# The supply always has these cards
supply = testUtility.GetSupply(nV, nC, player_names, boxlist, box)

# initialize the trash
trash = []

# Construct the Player objects
players = testUtility.buildPlayers(player_names)

# Play the game
runDomGame = testUtility.runGame(supply,supply_order,players,trash)

# Final score
dcs = Dominion.cardsummaries(players)
vp = dcs.loc['VICTORY POINTS']
vpmax = vp.max()
winners = []
for i in vp.index:
    if vp.loc[i] == vpmax:
        winners.append(i)
if len(winners) > 1:
    winstring = ' and '.join(winners) + ' win!'
else:
    winstring = ' '.join([winners[0], 'wins!'])

print("\nGAME OVER!!!\n" + winstring + "\n")
print(dcs)