import os

abs_path = os.path.abspath('.')
filename = 'set.py'
file_path = abs_path + '\\' + filename
file_path = os.path.join(abs_path, filename)

# os.system('mkdir example')

for file_path in os.listdir('.'):
    file_path = os.path.join(os.path.abspath('.'), file_path)
    if os.path.isfile(file_path):
        print(file_path, '-> is file')
    elif os.path.isdir(file_path):
        print(file_path, '-> is directory')
    

print(help(os))
# print(file_path)

# os.system('mkdir example')
# os.system('rmdir example')

# print(os.listdir('.'))