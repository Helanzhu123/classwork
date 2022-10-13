# Integer, Float(decimal), String, Boolean



# x = 5
# g = int(x)
# y= str(x)
# z = bool(x)
# a = float(x)
# print(x, g, y, z, a)

age = int(input("how old are you?"))
if age <3: 
    print("you are a baby")
elif age >= 3 and age <= 18:
    print("grow grow")
elif age > 18 and age < 65:
    print("old old")
else:
    print("no no")