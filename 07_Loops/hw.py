position = int(input('Enter position: '))

if 0 < position <= 10:
    print('Congratulations!')
    grade = int(input('Enter grade: '))
    if grade >= 290:
        print('you have a scholarship')
    else:
        print('you dont have scholarship')
else:
    print('You lose!')