from  createDeck import createDeck, mix

def deal(num_players, cards_per_player, deck):  
    hands = []
    for _ in range(num_players):
     hands.append([])

    for _ in range(cards_per_player):  
        for player in range(num_players):
            if deck:  
                card = deck.pop(0)
                hands[player].append(card)  
    return hands

def main():
    deck = createDeck()
    print("Working deck forward:")
    print(deck)
    mix(deck)
    print("mix deck:")
    print(deck)
    num_players = int(input('Enter num_players:'))
    cards_per_player = int(input('Enter cards_per_player:'))
    hands = deal(num_players, cards_per_player, deck)
    for i, hand in enumerate(hands):
     print(f"players {i + 1}: {hand}")
   
    print("The rest of the cards are in the deck:")
    print(deck)

if __name__ == "__main__":
    main()