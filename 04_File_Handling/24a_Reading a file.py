file = open("24_Text File.txt", "r")  # "r" means read mode
content = file.read()
print(content)
file.close()  # Always close the file after you're done