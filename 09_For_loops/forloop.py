#Fizz- Buzz game
# for i in range(1,101):
#     if i % 15 == 0:
#         response = "Fizz - Buzz"
#         print(response)
#     elif i % 3 == 0:
#         response = "Fizz"
#         print(response)
#     elif i % 5 == 0:
#         response = "Buzz"
#         print(response)
#     else:
#         print(i)

#Write a program that counts how many times a specific digit appears in numbers from 1 to a user-provided number.

# n = int(input("enter any number: "))
# number = input("enter specific number: ")
# count = 0
# for i in range(n + 1):
#     if number in str(i):
#         count += 1
# print("count = ", count)


# Write a program that counts and prints the number of divisors of a user-provided number.

# n = int(input("enter any number: "))
# divisorsCount = 0
# for i in range(1, n + 1):
#     if n % i == 0:
#         divisorsCount += 1
# print(divisorsCount)


# Check for Palindrome Number.

# n = int(input("enter start number: "))
# m = int(input("enter stop number: "))
# for i in range(n, m + 1):
#     i = str(i)
#     if i == i[::-1]:
#         print(i, "is Polindrome")
#     else:
#         print(i, "is not Polindrome")

# Check for Palindrome Word.

# text = input("enter text :")
# print(text == text[::-1])



#Write a program that finds and prints all perfect numbers up to a user-provided limit. 
#A perfect number is a number that is equal to the sum of its proper divisors (excluding itself).    (6 is perfect number)
# n = int(input("enter number: "))
# sum = 0
# for i in range(1, n):
#     if n % i == 0:
#         sum += i
#         print("divisor of", n, "is", i )
# print("sum of divisors is ", sum )
# if sum == n:
#     print(n,"is a perfect number")
# else:
#     print(n,"is not a perfect number")


# Multiplication Table: Write a program that prints a multiplication table for a number (e.g., from 1 to 10) using nested for loops.
# n = int(input("enter n :"))
# for i in range(1, n + 1):
#     for j in range (1, 11):
#         print(f"{i * j :8}", end = " ")
#     print()
    
# Fibonacci sequence
# n = int(input("enter n: "))
# a = 0
# b = 1
# for _ in range(n + 1):
#     print (a, end = " ")
#     a, b = b, a + b 

# Count Vowels: Write a program that counts the number of vowels in a given string using a for loop.
# text = input("enter text: ")
# vowels = "a", "e", "i", "o", "u"
# count = 0
# for i in text:
#     i = str(i)
#     if i in vowels:
#         count += 1
# print(count)