# #Xndir 75
# text = input("Mutqagreq teqst: ").replace(" ", "").lower()  
# start = 0
# end = len(text) - 1

# is_palindrome = True 

# while start < end:
#      if text[start] != text[end]:
#          is_palindrome = False  
#          break  
#      start += 1
#      end -= 1

# if is_palindrome:
#      print("Palindrum e:")
# else:
#      print("Palindrum che:")

#Xndir 77
max_value =10

i=1
while i<=max_value:
      j =1
      while j<=max_value:
         print(f'{(i*j):4d}',end= ' ') 
         j+=1
      print()   
      i +=1
