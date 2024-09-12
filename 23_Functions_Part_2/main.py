import functools
import sys

sys.setrecursionlimit(2000)


data = {}

# @functools.cache
def fibonaccii(n):
    if n < 2: return n
    
    if n not in data:
        result = fibonaccii(n-1) + fibonaccii(n-2)
        data[n] = result
    
    return data[n]


# fibo = fibonaccii(1000)
# print(fibo)


# positional and keyword arguments
def function(pos_only, /, pos_or_kwd, *, kwd_only):
    print(pos_only)
    print(pos_or_kwd)
    print(kwd_only)
    
# function(1, pos_or_kwd=2, kwd_only=3)


# arguments, keyword arguments
def function(*args, sep=' ', **kwargs,):
    print(sep.join(args))
    print(kwargs)
    
    
# function('a', 'b', 'c', a=1, b=2, c=3)


def evklid(a, b):
    if b == 0:
        return a
    else:
        c = a % b
        return evklid(b, c)
    
# res = evklid(21325131, 553441324)
# print(res)


def int_to_binary(n):
    if n < 2: return str(n)
    return  int_to_binary(n // 2) + str(n % 2)


# binary = int_to_binary(14)
# print(binary)
# print(bin(14))