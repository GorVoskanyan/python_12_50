#Xndir
# 5........5
# 54......45
# 543....345
# 5432..2345
# 5432112345

# n = int(input("Enter a number: "))
# for i in range(n):
#     for j in range(n, n - i - 1, -1):
#         print(j, end='')
#     for _ in range(8-2 * i):
#         print('.', end='')
#     for l in range(n - i, n + 1):
#         print(l, end='')
#     print() 


#        1
#       3  5
#      7  9  11 
#    13  15  17  19 
#  21 23   25  27  29

# n = 5 
# start = 1  
# for i in range(1, n + 1):
#     spaces = ' ' * (n - i) * 2
#     row_numbers = []
#     for j in range(i):
#         row_numbers.append(start)
#         start += 2  
#     row_str = ''
#     for number in row_numbers:
#         row_str += str(number) + ' '
#     print(spaces + row_str)


#Xndir
n = int(input('Enter n:'))

for i in range(0,n,2):
      for j in range(i,i+11,2):
             print(j,end='   ')          
      print()         
      for l in range(i+1,i+12,2):
              print(l,end='   ')      
      print()



#Xndir
# height = int(input('Enter height:'))  
# width = int(input('Enter width:'))    
# for row in range(height+1):
#    for col in range(width+1):
#      if col==0 or col == width   :
#        print('|',end=' ')
#      elif row == 0:
#        print('-',end=' ')  
#      else:
#        print(' ',end =' ')  
#    print() 

