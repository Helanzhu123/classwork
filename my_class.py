#function is not inside any class
#method is function in class
#def create functions and class create classes
#method's first parameter always is self.
#variable scope including: global, local
class Car: 
    def run(self): 
        print("my car is running")
        self.color = "black"
        self.price = 9000000
    
    def stop(self):
        print("my car is stopped")
    
    def __init__(self,color,brand):  
        self.color =  color             #field: with a dot #it contains self, shares all field in the class
        self.price = 100000             #now every method can use these fields now
        self.brand = brand
        self.stop()

my_car = Car("black","benz") #data type: object/instance of Car
my_car.run()
my_car.stop()
# class recommend capital
class Tesla(Car): #now they are connected(parent class and child class)
    def __init__(self, color, brand, model):
        super().__init__(color, brand)         #super automaticaly call the parent class's init method
        self.model = model
    
    def charge(self, time:int, amount:int):
        self.time = time
        self.amount = amount

my_tesla = Tesla("white", "Tesla", "model 3")
my_tesla.charge(20, 1000)

#OOP stands for (object oriented programming)