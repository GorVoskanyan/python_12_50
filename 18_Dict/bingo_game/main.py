from random import shuffle
from time import sleep

from bingo_card import card_generator, show_card
from check_card import is_win_card
from game_logic import game_logic


def game_main_loop():
    card = card_generator()
    box = list(range(1, 76))
    shuffle(box)
    
    while True:
        show_card(card)
        sleep(2)
        lucky_number = box.pop()
        print(f"{lucky_number}".center(25, '_'))
        game_logic(card, lucky_number)
        if is_win_card(card):
            show_card(card)
            print(f'Bingo!'.center(25, '_'))
            break
        
        
if __name__ == '__main__':
    game_main_loop()
        