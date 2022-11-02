# for n in range(5):
#     print(n)

# numbers = []
# for n in range(5, 51, 3):
#     numbers.append(n)
# print(numbers)

numbers = [7, 'Japan']
for n in range(3):
    num = int(input("Enter an item: ")) #if use int to change data type, after printing out the list, numbers will have no quotes.
    numbers.append(num)
print("You choose: ")
print(numbers)

print("Modify the items...")
for i in range(len(numbers)):
    print(f"Location: {i}, Original item: {numbers[i]}")
    num = int(input("Enter new number: "))
    numbers[i] = num

print(numbers)