#array = list
# list is called complex/compound data type, consists of 4 basic data types as a group, it is loopable
my_list = [] #elements, items
print(len(my_list))
my_list.append(7)
my_list.append("Canada")
print(my_list)
print(my_list[0])
my_list.append(88)
print(my_list[1])
print(my_list[-1])
print(my_list)
# my_list.remove(7) remove by value
# print(my_list)
my_list.pop(1) #remove by index, the last one
print(my_list)
for item in my_list:
    if item == 88:
        print("The list contains 88")


print("--------------------")
print(88 in my_list) #check if the list contain a specific element/item or not 
print("--------------------")
x = 0 in my_list #same with above
print(x)

#replace is not a function for list's data type
my_list[1] = "Japan"
print(my_list)

my_list[1] = "China"
