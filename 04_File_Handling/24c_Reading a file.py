file = open("24_Text File.txt", "r")
lines = file.readlines()  # Returns a list of all lines
for line in lines:
    print(line.strip())  # Strip removes extra newlines
file.close()