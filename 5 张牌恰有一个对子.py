# -*- coding: utf-8 -*-
"""
Created on Fri Mar 31 10:16:34 2023

@author: ljhdy
"""

# Example: Simulating the probability of getting exactly one pair in a hand of 5 cards
import random

# Define a function to check if a hand has exactly one pair
def has_one_pair(hand):
    values = [card[0] for card in hand]
    return len(set(values)) == 4

# Define a function to simulate drawing a hand of 5 cards
def draw_hand():
    values = [str(i) for i in range(2, 11)] + ['J', 'Q', 'K', 'A']
    suits = ['♠', '♥', '♦', '♣']
    deck = [value + suit for value in values for suit in suits]
    random.shuffle(deck)
    return deck[:5]

# Simulate drawing many hands and count how many have exactly one pair
num_hands = 100000
num_one_pair = 0
for i in range(num_hands):
    hand = draw_hand()
    if has_one_pair(hand):
        num_one_pair += 1

# Calculate the probability of getting exactly one pair
probability = num_one_pair / num_hands

# Print the result
print('The probability of getting exactly one pair in a hand of 5 cards is:', probability)
