import random

def is_straight(hand):
    hand.sort()
    if hand == [1, 10, 11, 12, 13]:
        return True
    for i in range(len(hand)-1):
        if hand[i+1] - hand[i] != 1:
            return False
    return True

def simulate_straight(num_trials):
    straight_count = 0
    for i in range(num_trials):
        hand = random.sample(range(1, 14), 5)
        if is_straight(hand):
            straight_count += 1
    return straight_count / num_trials

print(simulate_straight(100000))