import sys

def function(file_name, mode, data):
    with open(file_name, mode, encoding='utf-8') as file:
        if mode == 'w':
            if data:
                file.write(data)
            else:
                file.write('Not data')
        elif mode == 'r':
            data = file.read()
            print(data)
    
    
def main():
    filename = sys.argv[1]
    mode = sys.argv[2]
    data = None if len(sys.argv) != 4 else sys.argv[3]

    function(file_name=filename, mode=mode, data=data)
    
main()