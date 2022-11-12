my_list = ['China', 'Us', 'Canada']
print(my_list)
my_list.append('Japan') #can not put print in this line
print(my_list)
#C(create)R(read)U(update)D(delete) these are the four basic operations
print('Japan' in my_list) #if japan in list or not. In operation check if the list contains a specific item or not
print('Korea' in my_list)
exist = False
# "". #these are all functions that string data type support

for i in my_list:
    if i.lower() == 'japan':
        exist = True
print(exist)
# iterating means loop, counting means length, searching means in operation(case sensetive) and lower function(convert all to lower case)
print('---------------------- Read ----------------------')
count = 0    
for i in my_list:
    print(i)
    count += 1
print(count)
print("")
print(len(my_list))
print(my_list[-1])
print(my_list[0])

print('--------------------- Update ---------------------')
my_list[0] = 'Russia'
print(my_list)
my_list[-1] = 'France'
# print(my_list[5]) #index error: list index out of range

print('--------------------- Delete ---------------------')
my_list.pop(-1)
my_list.remove('Us')
print(my_list)
my_list.clear() #Remove everything from a list
print(my_list)

print("---------------------------")
# pass occupied the place, a place holder. Does not make the code go wrong. Ex: if statment
# def gigi(): #use def to create one's own function
new_list = ["Jonathan", 2, "Banada", "Apple", "bullets", 7, "Apple"]
print(new_list.index('Apple')) # index finds the index number of an item, it is case sensitive
print(new_list.index(7)) #index only prints the first item if has more than one, and it will go error if an item does not exist

print(new_list.count('Apple')) # counts the number of time this item appears in the list, it is also case sensitive


