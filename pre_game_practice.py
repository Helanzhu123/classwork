class Character: #has to be self as first parameter
    def __init__(self, gender, age, race, name):
        self.gender = gender
        self.age = age
        self.race = race
        self.name = name

    def attack(self, damage):
        print(f"{self.name} is attacking with the damage of {damage}") 

class Druid(Character):
    def __init__(self, gender, age:int, race, name):
        super().__init__(gender, age, race, name) 

    def cast(self, ability):
        print(f"Casting {ability}")



druid = Druid("Female", 30, "Night Elf", "yoyoma")
druid_2 = Druid("Female", 29, "Blood Elf", "dadama")
druid.cast("阳炎之怒")