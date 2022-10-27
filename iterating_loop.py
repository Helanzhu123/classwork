# thing = "what a beautiful dAy"
# for char in thing:
#     if char == " ":
#         continue
#     elif char == "a" or char == "A":
#         continue
#     print(char, end = ",")

# print("------------------------------------")

count = 0
thing = "what a beautiful dAy"
for char in thing:
    count += 1
print(f"this is the number of letters in cluding spaces:{count}")

print("------------------------------------")

thing = "what a beautiful dAy"
print(len(thing))
value = len(thing)
print(value)

# # len is a function which counts the length of the string

# print("----------   JOJO bank system   ----------")
# print()
# username = input("User name please:")
# if username != "Kevin":
#     print("Get Out!!!INCORRECT USERNAME!!!")
#     exit()
# user_password = input("Please insert your password:")
# if len(user_password) < 6 or len(user_password) > 8:
#     print("Your password should be in the length of 6-8 letters")
# else:
#     print("Welcome")



# thing = "what a beautiful dAy"
# new_thing = ""
# for char in thing:
#     if char == "a":
#         continue
#     elif char != " ":
#         new_thing += thing
#     print(char, end = " ")
# print(new_thing)

# my_string = "Canada is really a great country."
# new_string = "-"

# for char in my_string:
#     if char != " ":
#         new_string += char
 
# print(new_string)

# my_string = "Canada is really a great country."
# new_string = my_string.replace(" ", "-")
# print(new_string)