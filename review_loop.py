n = int(input("Please input"))
k = int(input("Please input"))
count = 0
total = n
while count < k:
    count += 1
    n = n * 10
    total += n
print(total)

