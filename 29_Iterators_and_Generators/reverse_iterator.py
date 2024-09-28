class ReverseIterator:
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index != 0:
            self.index -= 1
            return self.data[self.index]
        raise StopIteration


reverse_iterator = ReverseIterator([10, 20, 30])

for elem in reverse_iterator:
    print(elem)