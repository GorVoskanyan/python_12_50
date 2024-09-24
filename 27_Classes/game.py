class StandartDeck:
    def __init__(self):
        self.deck = [
            v + s
            for s in 'hscd'
            for v in '23456789TJQKA'
        ]
        
    def shuffle(self):
        deck_copy = self.deck[:]
        __import__('random').shuffle(deck_copy)
        return deck_copy
    
    def index(self, elem):
        return self.deck.index(elem)
        
        
class Player:
    def __init__(self, name, deck):
        self.name = name
        self.deck = deck
        self.hands = []
    
    
    def __str__(self) -> str:
        return self.name


class Game:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        # self.players = [player1, player2]
        self.deck = StandartDeck()

    def end_game(self):
        return True if not self.player1.deck or not self.player2.deck else False
    
    def one_round(self, player1, player2):
        card1 = player1.deck.pop()
        card2 = player2.deck.pop()
        if self.deck.index(card1) >= self.deck.index(card2):
            player1.hands.append([card1, card2]) 
        else:
            player2.hands.append([card1, card2])
        print(card1, '->', card2)


if __name__ == '__main__':        
    standart_deck = StandartDeck()
    shuffled_deck = standart_deck.shuffle()
    first_player_cards = shuffled_deck[:26]
    second_player_cards = shuffled_deck[26:]
    player1 = Player(name='Astghik', deck=first_player_cards)
    player2 = Player(name='Aghavni', deck=second_player_cards)
    game = Game(player1, player2)
    
    while not game.end_game():
        # player1, player2 = __import__('random').sample(game.players, 2)
        game.one_round(player1, player2)
        
    print(player1, '>>', player1.hands)
    print(player2, '>>', player2.hands)