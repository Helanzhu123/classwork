def one():
    global a
    a = 1
    print(a)

def two():
    a = 10
    print(a)

a = 0
print(a)
one()
two()
print(a)

print("----------------------")

def one():
    b = 1
    print(b)

def two():
    global b
    b += 2
    print(b)

b = 3
print(b)
one()
print(b)
two()
print(b)

# print("-------------")

#global variable can work in the whole file.
#local variable can only work in the function that it is located in
name = "Jeff"

def set_name():
    global name
    name = "David"
    age = 13
    age += 1
    print(age)

def say_hello():
    print(f"Hello {name}")


name = "Dave"
say_hello()
set_name()
print(name)

