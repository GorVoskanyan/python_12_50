class WordPlay:
    def __init__(self, words: list) -> None:
        self.words = words
        
    def words_with_length(self, length: int) -> list:
        return [w for w in self.words if len(w) == length]
        
    def starts_with(self, s: str) -> list:
        return [w for w in self.words if w[:len(s)] == s]
    
    def ends_with(self, s: str) -> list:
        return [w for w in self.words if w[len(w) - len(s):] == s]
        
    def palindromes(self):
        return [w for w in self.words if w == w[::-1]]
        
    def only(self, l: list) -> list:
        return [w for w in self.words if set(w).issuperset(set(l))]
    
    def avoids(self, l: list) -> list:
        # return [w for w in self.words if not set(w).intersection(set(l))]
        result = []
        l = set(l)
        for word in self.words:
            word_set = set(word)
            if not word_set.intersection(l):
                result.append(word)
        return result
 
# create instance of class    
words = ['this', 'is', 'a',  'level', 'madam', 'test', 'of', 'class']
wordplay = WordPlay(words=words)

print(wordplay.words_with_length(5))
print(wordplay.starts_with('t'))
print(wordplay.ends_with('is'))
print(wordplay.palindromes())
print(wordplay.only(['s', 'i']))
print(wordplay.avoids(['s', 'i']))