friends = ["Jonathan", "Joseph", "Jolyne", "Josuke", "johnny", "Gyro", "jojo", "ojoj"]

count = 0

for n in friends:
    print(n, end = ' ')
    if n[0].lower() == "j":
        count += 1
print(count)