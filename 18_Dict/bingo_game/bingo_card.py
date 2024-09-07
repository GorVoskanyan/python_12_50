from random import sample

def card_generator() -> dict:
    card = {
        'B': sorted(sample(range(1, 16), k=5)),
        'I': sorted(sample(range(16, 31), k=5)),
        'N': sorted(sample(range(31, 46), k=5)),
        'G': sorted(sample(range(46, 61), k=5)),
        'O': sorted(sample(range(61, 76), k=5))
    }
    
    return card

def show_card(card: dict) -> None:
    """Generate a bingo card.
    Attributes:
        param card: dict
        return: None
    """
    
    for key in card.keys():
        print(f"{key:>5}", end='')
    
    print()
    
    for i in range(len(card)):
        for value in card.values():
            print(f"{value[i]:>5}", end='')
        print()

def main():
    card = card_generator()
    show_card(card)

if __name__ == '__main__':  
    main()