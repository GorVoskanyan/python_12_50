import sys

if len(sys.argv) != 2:
    print('Arguments must be provided as command line arguments')
    exit(1)
    
try:
    filename = sys.argv[1]
    with open(filename, 'r', encoding='utf-8') as file:
        print(''.join(file.readlines()[:10]))
except FileNotFoundError as message:
    print(message)
    
    