#Xndir 69
# age = input('Enter age:')
# sum =0

# while age != '':
#     age= int(age)
#     if 3<=age<=12:
#         sum = +14
#     elif 0<age<=2:
#         sum =0    
#     elif 12<=age<=65:
#         sum += 23
#     else:
#         sum += 18
#     age = input('Enter age:')    
# print(sum)


#Xndir 63
# num = int(input('Mutqagreq tiv:'))
# count =0
# sum =0
# if num ==0:
#     print('0-n chi karox linel arajin tivy')
# else:
#     while num !=0:
#       sum+= num
#       count +=1
#       num = int(input('Mutqagreq tiv:'))
#     print(sum/count)    


# Xndir 82
# q = int(input("Mutqagreq tivy: "))
# if q == 0:
#      result = "0"
# else:
#      result = ""
#      while q > 0:
#          r = q % 2       
#          result = str(r) + result  
#          q = q // 2      

# print(result)
# print(bin(16))

#Xndir 80
# n = int(input("mutqagreq 2 kam aveli:"))
# if n < 2:
#     print("sxal e,mutqagreq 2 kam avrli:")
# else:
#     factor = 2
#     print(n)
#     while factor <= n:
#         if n % factor == 0: 
#             print(factor)
#             n //= factor
#         else:
#             factor += 1


# Xndir 71
# pi_approximation = 3.0
# numerator = 4.0
# sign = 1
# denominator = 2 * 3 * 4
# i = 2  
# while i <= 15:  
#     term = sign * (numerator / denominator)
#     pi_approximation += term
#     sign *= -1
#     i += 1
#     denominator = i * (i + 1) * (i + 2)  

#     print(pi_approximation)