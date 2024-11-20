try:
    result = int("hello")
except ValueError:
    print("Error: Cannot convert to integer.")
except TypeError:
    print("Error: Wrong type provided.")
