import random
def createDeck() -> list:
     
    nominal_values = ['2','3','4','5','6','7','8','9','T','j','Q','K','A']
    suites = ['s','h','d','c']
    cards_deck = []
    for suit in suites:
        for nominal_value in nominal_values:
            card =  nominal_value + suit
            cards_deck.append(card) 
    return cards_deck 
        
def mix(cards_deck) -> None:
    lenght = len(cards_deck)
    for i in range(lenght):
        j = random.randint(i, lenght-1)
        cards_deck[i], cards_deck[j] = cards_deck[j], cards_deck[i]
      
      
if __name__ == "__main__":    
    result = createDeck()
    print("cards_deck before mixing")
    print(result)
    mix(result)
    print("cards_deck after mixing:")
    print(result)