file_name = 'M7DZ2_file.txt'
with open(file_name, mode = 'r') as file:
    for line in file:
        print(line, end = '')

