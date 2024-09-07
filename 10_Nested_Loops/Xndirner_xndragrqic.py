#Xndir 64
# original_prices = [4.95, 9.95, 14.95, 19.95, 24.95]


# print(f"{'Original Price':<15} {'Discount Amount':<15} {'New Price':<15}")

# for price in original_prices:
#     discount_amount = price * 0.60  
#     new_price = price - discount_amount  
#     print(f"{price:<15.2f} {discount_amount:<15.2f} {new_price:<15.2f}")


#Xndir
# x = float(input("Մուտքագրեք թիվը, որի քառակուսի արմատը ցանկանում եք գտնել: "))


# if x < 0:
#     print("Քառակուսի արմատ չի կարող լինել բացասական թվի համար:")
# else:
    
#     guess = x / 2.0

    
#     tolerance = 1e-12
#     while abs(guess * guess - x) > tolerance:
#         guess = (guess + x / guess) / 2.0

    
#     print(f"Քառակուսի արմատը {x} թվի մոտավոր արժեքն է {guess:.12f}")

#xndir
# n = int(input())
# m = int(input())


# d = min(n, m)


# while n % d != 0 or m % d != 0:
#     d -= 1
# print( d)

#Xndir
# l= int(input())
# r = int(input())
# for i in range(l,r+1):
#     for j in range(i,i+1):
#         print(j)
#         for l in range(1,j+1):
#             if j % l==0:
#               print('+',end='')
#             else:
#                 print('-',end='')  
#     print()

#xndir
# num = int(input())
# artadryal =1
# factorial = 1

# for j in range(1,num+1):
#         factorial*=j
#         artadryal *= factorial    
# print(artadryal) 