# number = -2
# while number < 100:
#     number += 3
#     if number == 33:
#         break
#     elif number % 7 == 0:
#         continue
#     print(number)

# # for number in range(1, 101, 3):
# #     if number == 33:
# #         continue
# #     elif 100 % 7 == 0:
# #         continue
# #     elif number != 7:
# #         print(number)

# for number in range(1,101,3):
#     if number == 33:
#         continue
#     elif 100 % 7 == 0:
#         continue



# from re import I


# i = 1000
# sum = 0

# while i <= 1500:
#     if i % 9 == 0:
#         print(f"sum is {sum}")
#         sum += i
#     i += 1

# print(sum)

# sum = 0
# for number in range(1000, 1501):
#     if number % 9 == 0:
#         print(sum)
#         sum = sum + number
#     number = number + 1

number = 45
while number <= 45:
    print(number)
    number -= 1
    if number == 32:
        break
print("-----------------------------------")
for number in range(45, 32, -1):
    print(number)



count = 0
while True:
    print("Repeat")
    count += 1
    if count == 3:
        break