import sys

# print(sys.version)
# print(sys.platform)
# print(sys.argv)

def add(a, b):
    return a + b

def main():
    a = int(sys.argv[1])
    b = int(sys.argv[2])
    res = add(a, b)
    print(res)


if __name__ == '__main__': 
    main()