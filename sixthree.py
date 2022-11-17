# import random

# def main():
#     print("Hello")
#     name = input("Enter your name: ")
#     num = random.randint(1, 11)

#     print(name)
#     print(num)
# if __name__ == "__main__":
#     main()

# print("--------------------------")

# def plus_five(n):
#     return n + 5

# def main():
#     result = plus_five(10)
#     print(result)

# if __name__ == "__main__":
#     main()

# print("--------------------------")

from typing import List

def count_evens(nums: List[int])-> int:
    even = 0 
    for n in nums:
        if n % 2 == 0:
            even += 1
    return even
result = count_evens([2, 1, 2, 3, 4])
print(f"There are {result} even numbers in the list")