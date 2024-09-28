class Primes:
    def __init__(self, number):
        self. number = number
        self.current = 1

    def __iter__(self):
        self.current = 1
        return self

    def __next__(self):
        while self.current < self.number:
            self.current += 1
            if self._is_prime(self.current):
                return self.current
        raise StopIteration

    def _is_prime(self, number):
        for n in range(2, int(number**0.5) + 1):
            if number % n == 0:
                return False
        return True


primes = Primes(40)

# for elem in primes:
#     print(elem)
#
# for elem in primes:
#     print(elem)

print(primes._is_prime(7))