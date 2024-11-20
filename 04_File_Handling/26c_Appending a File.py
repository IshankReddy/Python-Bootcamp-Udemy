file = open("notes.txt", "a")
file.write("This is a new note.\n")
file.close()

# Reopen the file in read mode to verify the appended content
file = open("notes.txt", "r")
content = file.read()
file.close()
print(content)