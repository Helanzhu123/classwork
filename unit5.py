# sentence = "3 8 3 9 6 9 1 0 233"
# words = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
# numbers = sentence.split(" ")
# num = numbers[0:5]
# print(num)
# number_list = []
# for i in num:
#     index = (int(i))
#     # print(words[index])
#     number_list.append(index)

# print(number_list)


# # print(f"{digit:2}")
# print(words.count("b"))



new_list = ["Jonathan", 2, "Banada", "Apple", "bullets", 7, "Apple"]
# index = 0
# for i in new_list:
#     print(f"{index}   {i}")
#     index += 1
# enumerate print out loop of index, value 
for index, value in enumerate(new_list):
    print(f"{index}   {value}")