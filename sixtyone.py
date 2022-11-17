#store an action
# define a function
#parameter(inside define)
# def add(x:int,y:float)->float: #int plus float and gives float
#     return x + y     # return the calculated result to its original place
# # call a function(run it)
# result = add(3.0,4) #argument(inside call)
# print(result)

print("--------------------------")
def circle_area(radius: float = 100)-> float: #default value 100
    result = 3.1415926 * (radius**2)
    return result

user = int(input("Radius : ? "))

result = circle_area(user)
print(result)





