# 10 rounds of games
# create a list to recall each game's score
#random number
my_list = [6, 8, 9, 10, 2]

for i in range(len(my_list)):
    print(my_list[i])
for i in my_list:
    print(i)

print('------------------')

my_list = [2, 3, 4, "Canada", "China", "USA"]
for i in my_list:
    print(i)
my_list.append(10)
print (my_list[3])
print (my_list[-4])
my_list.remove(2)
my_list.pop(1)
print(my_list)
