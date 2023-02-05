# # # import random


# # # score = 0

# # # print("10 questions in total, each worth 10 points")
# # # for i in range(10):
# # #     number1 = random.randint(1,20)
# # #     number2 = random.randint(1,20)
# # #     operator = random.randint(1,4)
# # #     if operator == 1:
# # #         symbol = "+"
# # #         correct_answer = number1 + number2
# # #     elif operator == 2:
# # #         symbol = "-"
# # #         correct_answer = number1 - number2
# # #     elif operator == 3:
# # #         symbol = "*"
# # #         correct_answer = number1 * number2
# # #     elif operator == 4:
# # #         symbol = "//"
# # #         correct_answer = number1 // number2
    
# # #     answer = int(input(f"{i+1}. {number1} {symbol} {number2} = ?"))
# # #     if answer == correct_answer:
# # #         score += 10
# # #         print(f"good job ur cuurent point is {score}")
# # #     else:
# # #         print("馬鹿")

# # # print(f"Your final score is {score}")

# # # import random

# # # friends = ["じんた", "ぽっぽ", "めんま"]
# # # print(f"{friends}")
# # # while True:
# # #     answer = input("You want to add more?\n(Y/N)")
# # #     if answer == "Y" or answer == "y":
# # #         new_name = input("Who u want to add?")
# # #         friends.append(new_name)
# # #     elif answer == "N" or answer == "n":
# # #         break

# # # print(f"Here are the people who are attending this game: {friends}")
# # # print("Game name: Anohana")
# # # start = input("Press the enter key to start the game.")

# # # index = random.randint(0,len(friends)-1)
# # # person = friends[index]
# # # amount = random.randint(1,100)
# # # print(f"congrat {person} wins {amount} flowers")

# # user = input("Put in bunch of words\n")
# # list = user.split(" ")
# # result = ""
# # for word in list:
# #     result += (word[0].upper())
# # print(result)



# def sum67(nums):
#     if len(nums) == 0:
#         return 0
    
#     total = 0 
#     found6 = False
#     found7 = False
#     subtotal = 0
#     for number in nums:
#         total += number
#         if number == 6 and not found6:  #check if the first time encountering 6
#             found6 = True

#         if found6:  # sum the section
#             subtotal += number

#         if found6 and (not found7) and (number == 7):
#             found7 = True
#             total -= subtotal

#             found7 = False
#             found6 = False
            

#     return total

# nums  = [6, 7, 1, 6, 7, 7]  #correct: 8,  our: -5
# result = sum67(nums)
# print(result)

a = []
a.reverse()

def middle_way(a, b):

    return [a[1], b[1]]

# 

