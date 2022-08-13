# for a rock-paper-scissor game, we need input, random number generation, three outcomes (win, lose, draw)
# we also need loops, print, and some other stuff which i don't know about

import random
while True:
    inp = input("Let's play a game of Rock-Paper-Scissor! To start game, input 0 for Rock, 1 for Paper and 2 for Scissor. To end game, input 'Done' : ")
    if inp in range(3) :
        print("Sorry, invalid choice. Input 0 for Rock, 1 for Paper and 2 for Scissor. To end game, input 'Done' :", inp)
    n = random.randint(1,3)
    if n == 1 :
        print('You won!')
    elif n == 2 :
        print('You lost...')
    else :
        print('It is a draw.')

print("Hey Yew Mun!")
