# Day 4: Random module

#Heads or Tails
import random
coin_toss = random.randint(0,1)
guess =int(input("Guess the coin. 0 or 1: \n"))
if guess == coin_toss:
    if guess == 0:
        print(f'You guessed Heads. Its {coin_toss}. You win!')
    elif guess == 1:
        print(f'You guessed Tails. Its {coin_toss}. You lose!')
else: 
    guess == coin_toss
    if guess == 0:
        print(f'You guessed Heads. Its {coin_toss}. You win!')
    elif guess == 1:
        print(f'You guessed Tails. Its {coin_toss}. You lose!')
    