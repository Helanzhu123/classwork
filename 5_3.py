friends = ["Jonathan", "Joseph", "Jolyne", "Josuke", "johnny", "Gyro", "jojo", "ojoj"]

count = 0

for n in friends:
    print(n, end = ' ')
    if n[0].lower() == "j":
        count += 1
print(count)

i = 0
while i < len(friends):
    name = friends[i].lower()
    print(f"i: {i}, name: {name}")
    if name == "josuke":
        friends[i] = "東方"
        break
    i += 1

print(friends)