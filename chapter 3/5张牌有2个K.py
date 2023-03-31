# -*- coding: utf-8 -*-
"""
Created on Fri Mar 31 10:10:20 2023

@author: ljhdy
"""

import random

# create a deck of cards with 4 suits and 13 ranks
deck = []
suits = ['Spades', 'Hearts', 'Diamonds', 'Clubs']
ranks = ['Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
for suit in suits:
    for rank in ranks:
        deck.append(f'{rank} of {suit}')

# simulate drawing 5 cards from the deck
num_trials = 1000000
num_successes = 0
for i in range(num_trials):
    hand = random.sample(deck, 5)
    num_kings = hand.count('King of Spades') + hand.count('King of Hearts') + hand.count('King of Diamonds') + hand.count('King of Clubs')
    if num_kings == 2:
        num_successes += 1

# calculate probability of getting exactly 2 kings in a 5-card hand
probability = num_successes / num_trials
print(probability)
