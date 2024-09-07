def createDeck():
    deck = []
    suits = ["D", "H", "S", "C"]
    numbers = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "T"]
    
    for suit in suits:
        for number in numbers:
            deck.append(suit + number)
            
    return deck
    

def shuffle(deck):
    shuffledDeck = []
    firstHalf = deck[:26]
    secondHalf = deck[26:]
    
    for card1, card2 in zip(secondHalf, firstHalf):
        shuffledDeck.append(card1)
        shuffledDeck.append(card2)
        
    return shuffledDeck
    
    
def shuffle_multiple_times(deck, times):
    for _ in range(times):
        deck = shuffle(deck)
        
    return deck
    
    
def game(playersNumber, cardsNumber, deck):
    hands = [[] for _ in range(playersNumber) ]
         
    for hand in hands:
        for _ in range(cardsNumber):  
            if deck:  
                card = deck.pop()  
                hand.append(card)  
    
    return hands 
    
        
    
def main():
    result = createDeck()
    print("Playing Cards are: ".center(120))
    print(" ".join(result))

    result1 = result.copy()    
    shuffledResult = shuffle_multiple_times(result1, 3)
    #print("Shuffled Cards are: ".center(120))
    #print(" ".join(shuffledResult))
    print()
    
    playersNumber = int(input("Enter number of players: "))
    cardsNumber = int(input("Enter number of cards for each player: "))
    
    gameResult = game(playersNumber, cardsNumber, shuffledResult)
    print()
    
    print("Players:", end = "")
    print()
    for i in range(1, playersNumber + 1):
        player = ' '.join(gameResult[i - 1])  
        print(i,"Players cards are:  ->", player)
        
if __name__ == "__main__":
    main()
    