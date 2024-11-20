try:
    file = open("example.txt", "r")
except FileNotFoundError:
    print("File not found!")
finally:
    print("Cleaning up...")