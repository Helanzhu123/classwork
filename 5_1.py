my_list = [6, 8, 9, 23, 45, 6]

print(my_list[3])
print(my_list[0])

my_list.append(99)
print(my_list)

print(my_list[len(my_list) -1])
print(my_list[-1]) 

print()
for number in my_list:
    print(f"Number: {number}")

print("----------------")

for i in range(len(my_list)):
    print(my_list[i])
    print(i)

print("-----SLICING-----")
print(my_list)



print(my_list[3:5])      #very important
print(my_list[0:len(my_list):2])
print(my_list[0:6:2])



print("------------------")
#also very important
print(my_list[2:])    #from 2, give everything else in the line
print(my_list[:5])

print(my_list[::-1]) #reverse a list

print("-----------------")
friends = ["Jolyne", "Sanji", "L"]
print(friends)
friends.append("Kitagawa")
friends.append("Edogawa")
for f in friends:
    print(f, end = " ")
print(friends)
print("---------------")
print(friends[0])
print(friends[-5])
print("-----------")
pick = friends[0]
print(pick)
print("----------------")
print(friends[1:5])
print(friends[0:len(friends):3])
print(friends[0:5:2])
