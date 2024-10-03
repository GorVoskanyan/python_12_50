def file_read(file_path: str) -> str:
    with open(file_path, 'r', encoding='utf-8') as file:
        print(file.read())
        file.seek(0)
        lines_count = len(file.readlines())
        return lines_count
    
    
lines = file_read('logger.py')
print(lines, 'lines')