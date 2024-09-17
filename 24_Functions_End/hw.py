def is_palindrome(word: str) -> bool:
    if not word: return True
    return False if word[0] != word[-1] else is_palindrome(word[1:-1])


# res = is_palindrome('level')
# print(res)


l = [1, [1, [1, 1, [1, 1, 1, [1, [1, [1]]]]]]]

def unpack(data):
    if not data: return 0
    return data[0] + unpack(data[1:]) if not isinstance(data[0], list) else unpack(data[0])

# res = unpack(l)
# print(res)


data = {
    'A': 'Alpha',
    'B': 'Bravo',
    'C': 'Charlie'
} 


def nato(word):
    if not word: return ''
    return data[word[0]] + ' ' + nato(word[1:])

# res = nato('BAC')
# print(res)


