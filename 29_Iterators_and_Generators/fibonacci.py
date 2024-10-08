class Fibonacci:
    def __init__(self, number):
        self.number = number
        self.cur_value = 0
        self.next_value = 1
        self.count = 0
        
    def __iter__(self):
        self.cur_value, self.next_value = 0, 1
        self.count = 0
        return self
    
    def __next__(self):
        if self.count < self.number:
            self.count += 1
            self.cur_value, self.next_value = self.next_value, self.cur_value + self.next_value
            return self.cur_value
        else:
            raise StopIteration
        

fibo = Fibonacci(number=10)

for fib in fibo: print(fib)
for fib in fibo: print(fib)
for fib in fibo: print(fib)