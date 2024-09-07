def is_win_card(card: dict) -> bool:
    if any(sum(value) == 0 for value in card.values()):
        return True
    
    # if any(sum([value[i]]) == 0 for value in card.values() for i in range(len(card))):
    #     return True
    
    for i in range(len(card)):
        row_sum = 0
        for value in card.values():
            row_sum += value[i]
        if row_sum == 0:
            return True
        
    main_diagonal = 0
    i = 0
    for value in card.values():
        main_diagonal += value[i]
        i += 1
    
    if main_diagonal == 0:
        return True
    
    diagonal = 0
    i = -1
    for value in card.values():
        diagonal += value[i]
        i -= 1
    
    if diagonal == 0:
        return True
    
    return False


