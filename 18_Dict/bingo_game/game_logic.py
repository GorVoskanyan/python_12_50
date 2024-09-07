from random import shuffle

def game_logic(card: dict, lucky_number) -> bool:
    
    for value in card.values():
        if lucky_number in value:
            value[value.index(lucky_number)] = 0
            
    