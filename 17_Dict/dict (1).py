#xndir 136
# def reverseLookup(dictionary, value):
#     keys = [key for key, val in dictionary.items() if val == value]
#     return keys

# if __name__ == "__main__":
#     my_dict = {
#         'a': 10,
#         'b': 20,
#         'c': 10,
#         'd': 30,
#         'e': 20
#     }
#     value_to_search = 10
#     keys_found = reverseLookup(my_dict, value_to_search)
#     print(f" {value_to_search}: {keys_found}")
#     value_to_search = 20
#     keys_found = reverseLookup(my_dict, value_to_search)
#     print(f" {value_to_search}: {keys_found}")
#     value_to_search = 50
#     keys_found = reverseLookup(my_dict, value_to_search)
#     print(f"{value_to_search}: {keys_found}")



#Xndir 139
# morse_code = {
#     'A': '._',
#     'B': '_...',
#     'C': '_._.',
#     'D': '_..',
#     'E': '.',
#     'F': '.._.',
#     'G': '__.',
#     'H': '....',
#     'I': '..',
#     'J': '.___',
#     'K': '_._',
#     'L': '._..',
#     'M': '__',
#     'N': '_.',
#     'O': '___',
#     'P': '.__.',
#     'Q': '__._',
#     'R': '._.',
#     'S': '...',
#     'T': '_',
#     'U': '.._',
#     'V': '..._',
#     'W': '.__',
#     'X': '_.._',
#     'Y': '_.__',
#     'Z': '__..',
#     ',': '__..__',
#     '.': '._._._',
#     '?': '..__..',
#     ';': '_._._.',
#     ':': '___...',
#     "'": '.____.',
#     '"': '._.._.',
#     '!': '_._.__',
#     ' ': ' '  
# }
# word = input().upper()  
# convert = ''  
# for char in word:
#     if char in morse_code:
#         convert += morse_code[char] + ' '  
#     else:
#         convert += ' '  
# print(convert)
#xndir 146
# import random
# def generate_lotto_card():
#     card = {}
#     ranges = {
#         'B': range(1, 16),
#         'I': range(16, 31),
#         'N': range(31, 46),
#         'G': range(46, 61),
#         'O': range(61, 76)
#     }
#     for letter in 'BINGO':
#         card[letter] = random.sample(ranges[letter], 5)
#     return card

# def display_lotto_card(card):
#     print(" B   I   N   G   O")
#     for i in range(5):
#         row = [str(card[letter][i]).rjust(2, ' ') for letter in 'BINGO']
#         print(" ".join(row))
# if __name__ == '__main__':
#     lotto_card = generate_lotto_card()
#     display_lotto_card(lotto_card)

#Xndir 144
# import string
# def clean_text(text):
#     text = text.lower()  
#     text = text.translate(str.maketrans('', '', string.punctuation))  
#     text = text.replace(" ", "")
#     return text

# def are_anagrams(s1, s2):
#     cleaned_s1 = clean_text(s1)
#     cleaned_s2 = clean_text(s2)
#     freq_s1 = {char: cleaned_s1.count(char) for char in cleaned_s1}
#     freq_s2 = {char: cleaned_s2.count(char) for char in cleaned_s2}
    
#     return freq_s1 == freq_s2

# if __name__ == '__main__':
#     s1 = input('Enter s1: ')
#     s2 = input('Enter s2: ')
    
#     if are_anagrams(s1, s2):
#         print('anagram։')
#     else:
#         print('anagram chi։')
#xndir 145
# letter_scores = {
#     'A': 1, 'E': 1, 'I': 1, 'L': 1, 'N': 1, 'O': 1, 'R': 1, 'S': 1, 'T': 1, 'U': 1,
#     'D': 2, 'G': 2,
#     'B': 3, 'C': 3, 'M': 3, 'P': 3,
#     'F': 4, 'H': 4, 'V': 4, 'W': 4, 'Y': 4,
#     'K': 5,
#     'J': 8, 'X': 8,
#     'Q': 10, 'Z': 10
# }

# def calculate_score(word):
#     word = word.upper()
#     score = 0
#     for char in word:
#         if char in letter_scores:
#             score += letter_scores[char]
#     return score

# if __name__ == '__main__':
#     word = input('Enter word: ')
#     score = calculate_score(word)
#     print(f'word "{word}" total number of points՝ {score}')
