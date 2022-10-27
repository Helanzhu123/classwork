from ctypes.wintypes import WORD


for number in range(15, 46, 7):
    print(number)
print("-----------------")
count = 15
while count < 45:
    print(count)
    count += 7
print("-----------------")
for blah in range(3):
    print("blah")
print("-----------------")
count = 0
while count < 3:
    print("blah")
    count += 1
    if count == 3:
        break
print("-----------------")
my_string = "Hallo ha!"
for char in my_string:
    print(char, end = " ")
print("-----------------")
thing = "ジョジョの奇妙な冒険"
for char in thing:
    if char == "な":
        continue
    print(char, end = " ")
print("-----------------")
old = "computer science is the best course"
new = old.replace(" ", "-")
print(new)
