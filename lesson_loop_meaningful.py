# for number in range(1, 11,):
#     if number == 4:
#         continue
#     print(number, end = " ")

# for number in range(1, 21):
#     if number == 4 or number == 13 or number == 14:
#         continue
#     print(number, end = " ")

count = 0
while count < 20: 
    count = count + 1
    if count == 4 or count == 13 or count == 14:
        continue
    print(count, end =" ")
