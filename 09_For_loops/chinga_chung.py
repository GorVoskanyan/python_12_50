import random

combs = 'Rock', 'Paper', 'Scissors'
pc_score = user_score = 0
print('='*30)
print(f"User | Pc".center(30))
print('='*30)

while pc_score != 3 and user_score != 3:
    pc_choice = random.choice(combs)
    user_choice = input('>>> ').capitalize()
    print(f"{user_choice} | {pc_choice}".center(30))
    match (pc_choice, user_choice):
        case ('Paper', 'Rock') | ('Scissors', 'Paper') | ('Rock', 'Scissors'):
            pc_score += 1
        case ('Rock', 'Paper') | ('Paper', 'Scissors') | ('Scissors', 'Rock'):
            user_score += 1
        case _:
            print('Try again!')
            continue
    print(f"{user_score} | {pc_score}".center(30))

winner = 'Pc' if pc_score == 3 else 'User'
print('='*30)
print(f"{winner} Win!".center(30))
print('Game Over!'.center(30))