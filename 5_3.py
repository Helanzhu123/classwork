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

print("---------------------------")


marks = [10, 2, 5, 2, 6, 900, 1000, 200, 1]
count = 0
location = 0
for n in marks:
    count += 1
    location += 1
    if n < 50:
        pass
    elif n > 100:
        print(f"Invalid, location: {location-1}")
        break
print(f"There are {count} numbers less than 50")
