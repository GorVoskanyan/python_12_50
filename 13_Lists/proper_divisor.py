def proper_divisor(number):
    result = []
    for divisor in range(1, number):
        if number % divisor == 0:
            result.append(divisor)
            
    return result


# def main():
#     number = int(input('Enter number: '))
#     result = proper_divisor(number)
#     print(result)
    
# if __name__ == '__main__':
#     main()

# print(__name__)