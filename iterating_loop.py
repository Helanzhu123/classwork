thing = "what a beautiful dAy"
for char in thing:
    if char == " ":
        continue
    elif char == "a" or char == "A":
        continue
    print(char, end = ",")

print("------------------------------------")

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

# len is a function which counts the length of the string

print("----------   JOJO bank system   ----------")
print()
username = input("User name please:")
if username != "Kevin":
    print("Get Out!!!INCORRECT USERNAME!!!")
    exit()
user_password = input("Please insert your password:")
if len(user_password) < 6 or len(user_password) > 8:
    print("Your password should be in the length of 6-8 letters")
else:
    print("Welcome")