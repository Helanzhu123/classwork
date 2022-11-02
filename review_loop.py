n = int(input("Please input"))
k = int(input("Please input"))
count = 0
total = n
while count < k:
    count += 1
    n = n * 10
    total += n
print(total)

answer = 0
number = int(input("Please input"))
for number in range(1, number + 1):
    old_answer = answer
    answer += number
    # print(answer)
    print(f"{old_answer} + {number} = {answer}")