#!/usr/bin/env python3

# Taken from http://brewster.kahle.org/2019/11/30/the-game-of-oligarchy/ this
# simulates the basic game and then passes judgement on the winner and losers.
#
# The game is played as follows. Initally everyone starts out with an equal amount
# of money. During each round, players are paired off and flip a coin. The
# winner takes half of the minimum amount of the two players from the loser.
#
# Even though the pairs are random, and the coin flips are fair, the money
# concentrates, just like in real life. When you play this with real people,
# the "winners" start to act like they're "skilled" and "entitled" to their
# winnings, just like billionares do today.



import argparse
import sys
import random

parser = argparse.ArgumentParser()
parser.add_argument("--history", action='store_true', help="Show win-loss history per player.")
parser.add_argument("--verbose", action='store_true', help="Show results after every round.")
args = parser.parse_args()

num_players = int(input('Number of players: '))
num_rounds = int(input('Number of rounds: '))


amounts = [100.0] * num_players
total_money = 100 * num_players
histories = [''] * num_players
battles = list(range(num_players))

for round in range(1, num_rounds + 1):
    if args.verbose:
        print()
        print(f'Round {round}')
        print('----------------------------------')
        for (player, amount) in enumerate(amounts):
            print(f'Player {(player + 1):2}: {amount:8.3f} ({(amount / total_money * 100):5.2f} %)')
        print()
    random.shuffle(battles)
    for i in range(0, num_players, 2):
        if i + 1 >= num_players:
            break
        player_a = battles[i]
        player_b = battles[i + 1]
        wager = min(amounts[player_a], amounts[player_b]) / 2.0

        winner = player_a
        loser = player_b
        if random.random() > 0.5:
            winner = player_b
            loser = player_a

        amounts[winner] += wager
        amounts[loser] -= wager
        histories[winner] += 'W'
        histories[loser] += 'L'

        if args.verbose:
            print(f'Player {winner + 1} takes {wager:0.5f} from player {loser + 1}')


print()
print(f'Final Results')
print('----------------------------------')
for (player, amount) in enumerate(amounts):
    h = ''
    if args.history:
        h = str(histories[player])
    print(f'Player {(player + 1):2}: {amount:8.3f} ({(amount / total_money * 100):5.2f} %) {h}')
print()

for (player, amount) in sorted(list(enumerate(amounts)), key=lambda x: -x[1]):
    percentage = amount / total_money
    if percentage >= 0.99:
        print(f'Player {(player + 1):2} IS THE GOD-EMPEROR! YOU SHOULD SACRAFICE YOURSELF FOR MERE CHANCE THAT THEY WOULD THINK ABOUT GLANCING YOUR WAY!')
    elif percentage >= 0.9:
        print(f'Player {(player + 1):2} is truely a demigod who has earned their place in Heaven through skill and hard work!')
    elif percentage >= 0.7:
        print(f'Player {(player + 1):2} is superior to all others and has bent the universe to their will through shear gumption and talent!')
    elif percentage >= 0.5:
        print(f'Player {(player + 1):2} is a talented wealth creator!')
    elif percentage >= 0.1:
        print(f'Player {(player + 1):2} is hard worker who nothing has ever been given to.')
    elif percentage >= 0.001:
        print(f'Player {(player + 1):2} could have achieved success if they just wanted it. They must not have wanted it.')
    elif percentage < 0.001:
        print(f'Player {(player + 1):2} is lazy and has only themselves to blame for their position in life. A waste of flesh, that deserves their place.')
    else:
        print(f'Player {(player + 1):2} is an enigma.')
