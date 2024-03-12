home = 'M7DZ1_rezh_open_file.txt'
home = open(home, mode = 'r')
home_content = home.read()
home.close()
print(home_content)