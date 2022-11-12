# names_string = "Goku Naruto Luffy"

# friends = names_string.split(" ")
# print(friends)

# for name in friends:
#     print(name)

numbers_string = "65 9 28 30 18 7 96"

numbers_list = []
for num_str in numbers_string.split(" "):
    print(num_str)
    numbers_list.append(int(num_str))
print(numbers_list)


# total = 0
# for n in numbers_list:
#     total += n
# print(total)

print('---------------------')

v_string = "1 0 2 4 9 2 5 87"
v_list= []
count = 0
for v_str in v_string.split(" "):
    v_list.append(str(v_str))
    count += 1
    if count < 5:
       print(v_list)
    elif count >= 5:
        print("unsupported")







