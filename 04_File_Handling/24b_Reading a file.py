file = open("24_Text File.txt", "r")
first_line = file.readline()  # Reads the first line
second_line = file.readline()  # Reads the second line
print(first_line)
print(second_line)
file.close()