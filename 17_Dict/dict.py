# n = int(input("enter count: "))
# dict = {}
# for _ in range(n):
#     position = input("enter position: ")
#     name = input("enter name: ")
#     dict[position] = name


# q = int(input("enter query:" ))
# lst = []
# for _ in range(q):
#     lst.append(input("enter position for query: "))
    
# for item in lst:
#      if item in dict:
#             print(dict[item])
        

# n = int(input())
# lst1 = []
# lst2 = []
# for _ in range(n):
#     elem1 = input()
#     elem2 = input()
#     lst1.append(elem1)
#     lst2.append(elem2)

# print(lst1)
# print(lst2)
# for x ,y in zip(lst1, lst2):
#     dict = {x: y}
# print(dict)





#N136


# def reverseLookup(myDict, key):
#     for elem in myDict.values():
#         return myDict[key]
    
# def main():
#     myDict = {
#         "name": "Poxos",
#         "surname": "Petrosyan",
#         "age": "25",
#     }
#     key = input("Enter key: ")
#     if key in myDict.keys():
#         result = reverseLookup(myDict, key)
#         print(result)
#     else:
#         print("Try again!")

# if __name__ == "__main__":
#     main()



# N137?

# import random

# def diceRoll():

#     dice1 = random.randint(1, 6)
#     dice2 = random.randint(1, 6)
    
#     return dice1 + dice2


# def main():
#     result = [diceRoll() for _ in range(1000)]
#     data = {i: result.count(i) * 100 / 1000 for i in sorted(result)}
#     for key, value in data.items():
#         print(key, '-', value)
        
# main()
#N138

# data = {
#     '1': ',.?!:',
#     '2': 'ABC',
#     '3': 'DEF',
#     '4': 'GHI',
#     '5': 'JKL',
#     '6': 'MNO',
#     '7': 'PQRS',
#     '8': 'TUV',
#     '9': 'WXYZ',
#     '0': ' ' 
# }

# text = input("Enter your text: --> ").upper()
# converted = ""
# for char in text:
#     for key, value in data.items():
#         if char in value:
#             quantity = value.index(char) + 1
#             converted += quantity * key

# print(converted)


#N139

# morse_code = {
#     'A': '.-',
#     'B': '-...',
#     'C': '-.-.',
#     'D': '-..',
#     'E': '.',
#     'F': '..-.',
#     'G': '--.',
#     'H': '....',
#     'I': '..',
#     'J': '.---',
#     'K': '-.-',
#     'L': '.-..',
#     'M': '--',
#     'N': '-.',
#     'O': '---',
#     'P': '.--.',
#     'Q': '--.-',
#     'R': '.-.',
#     'S': '...',
#     'T': '-',
#     'U': '..-',
#     'V': '...-',
#     'W': '.--',
#     'X': '-..-',
#     'Y': '-.--',
#     'Z': '--..',
#     '0': '-----',
#     '1': '.----',
#     '2': '..---',
#     '3': '...--',
#     '4': '....-',
#     '5': '.....',
#     '6': '-....',
#     '7': '--...',
#     '8': '---..',
#     '9': '----.',

# }

# text = input("Enter your text: ->").upper()
# for char in text:
#     for key in morse_code.keys():
#         if char == key:
#             print(morse_code[key], end = "")


#N140
# postalCode = input("Enter your postal code here: -> ").upper()

# province_codes = {
#     'Newfoundland': 'A',
#     'Nova Scotia': 'B',
#     'Prince Edward Island': 'C',
#     'New Brunswick': 'E',
#     'Quebec': 'G, H, J',
#     'Ontario': 'K, L, M, N, P',
#     'Manitoba': 'R',
#     'Saskatchewan': 'S',
#     'Alberta': 'T',
#     'British Columbia': 'V',
#     'Nunavut': 'X',
#     'Northwest Territories': 'X',
#     'Yukon': 'Y'
# }
# if len(postalCode) == 6:
#     for index in range(len(postalCode)):
#         if (index % 2 == 0 and postalCode[index].isalpha()) or (index % 2 != 0 and postalCode[index].isdigit()):
#                 for key, value in province_codes.items():
#                     if postalCode[0] == province_codes[key]:
#                         result = key

#         else:
#             result = "Invalid input!"           
#     print(result)
# else:
#     print("Your postal code shoulde have 6 characters!")


#N141

# number = int(input('>>> '))

# ten_to_twenty = {
#     11: "eleven",
#     12: "twelwe",
#     13: "threteen",
#     14: "fourteen",
#     15: "fifteen",
#     16: "sixteen",
#     17: "seventeen",
#     18: "eightteen",
#     19: "nineteen"
# }

# dictTens = {
#     10: "ten",
#     20: "twenty",
#     30: "thirty",
#     40: "forty",
#     50: "fifty",
#     60: "sixty",
#     70: "seventy",
#     80: "eighty",
#     90: "ninety"
# }

# dictPoints = {
#     1: "one",
#     2: "two",
#     3: "three",
#     4: "four",
#     5: "five",
#     6: "six",
#     7: "seven",
#     8: "eight",
#     9: "nine"
# }


# if number in dictPoints:
#     result = dictPoints[number]
# elif 10 <= number < 100:
#     if number in dictTens:
#         result = dictTens[number]
#     else:
#         result = dictTens[number // 10 * 10] + ' ' + dictPoints[number % 10]
# elif 100 <= number < 1000:
#     if number % 100 in dictTens:
#         result = dictPoints[number // 100] + ' hundred ' + dictTens[number % 100]
#     else:
#         result = dictPoints[number // 100] + ' hundred ' + dictTens[number // 100 % 10 * 10] + ' ' + dictPoints[number % 10]
# print(result)


#N142

# def count(text):
#     counts = {i: 0 for i in text}
#     for char in text:
#         counts[char] += 1
    
    
#     return counts

# def uniqueMember(counts):
#     lst = []
#     for key, value in counts.items():
#         if value == 1:
#             lst.append(key)
#     return lst


# def main():
#     text = input("Enter you text: -> ")
#     result = count(text)
#     finalResult = uniqueMember(result)
#     print(result)
#     print(finalResult)
    

# if __name__ == "__main__":
#     main()