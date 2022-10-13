# x = 'sutonn'
# # Each variables has its own data type.
# # Four basic data type: Integer, float(decimal), string(something in the quote)(single quote, double quote no difference, but must be the same)
# # boolean(2 values, either true or false)
# y = 100
# z = 90.5
# l = True
# q = False
# print(x, y, z, l, q)
# print(f"x is {x}")
# print(f"There are {y} stand users")
# apple = input("How many apples did you eat?")
# print(f"The user said he ate {apple} apples")



# print(8//4)
# add +, minus -, times *, divide /(answer always float), floor divide //(answer always ewual to integer)
# Bigger >, smaller <, greater or equal >=, smaller or equal <=, value assignment =, compare two variables ==
# check if 2 variavles not equal <>, != not equal, power of **, mod 余数 %, str convert integer to string, int convert string to integer
# print("I have a class of 33 students.")
# print("There are 11 girls, so that means..")
# print("there are " + str(33 - 11) + " boys.")
# print()
# print(f"That means {11 / 33} % are girls...")
# print("and {} % are boys.".format((33 - 11) / 33))
# print()
# print("If we made groups of six...")o
# print(f"There would be {33 // 6} groups of six.")
# print(f"And then a smaller group of {33 % 6} people.")
# print("-" * 100)
# print("If we had 17 apples and 3 people...")
# print(f"Each person would get {17 // 3} whole apples.")
# print("There would be " + str(17 % 3) + " apples remaining.")
# print()
# print("If we charged each person $2 each for their 5 apples..")
# print("they would each pay ${}.".format(2 * 5))
# print(f"they would each pay ${2 * 5}.")


from cgi import print_directory


number_of_banana = input("how many banana did you eat?")
if int(number_of_banana) > 10:
    print("TOO MUCH")
else:
    print("Healthy")
