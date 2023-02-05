#tuple is for the use of not changing a done list
#only difference between lists[] and tuples()
my_list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
my_list.append("Myday")
your_list = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday") #this is a tuple
print(your_list[2])
print(my_list)

print(your_list)
your_list[2] = "Mayday" #does not allow to change bc of tuple
