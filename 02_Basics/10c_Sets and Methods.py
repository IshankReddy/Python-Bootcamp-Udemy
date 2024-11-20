my_set = {1, 2, 3}
my_set.remove(2)    # Removes 2, raises KeyError if not present
my_set.discard(3)   # Removes 3, no error if not present
print(my_set)  # Output: {1}