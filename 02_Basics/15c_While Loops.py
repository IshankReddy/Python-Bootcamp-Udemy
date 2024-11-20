count = 0

while count < 5:
    count += 1
    if count == 3:
        continue  # Skip printing when count is 3
    print(f"Count is: {count}")