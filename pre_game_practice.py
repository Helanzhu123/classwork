class Character: #has to be self as first parameter
    def __init__(self, gender, age, race, name, level, health, mana):
        self.gender = gender
        self.age = age
        self.race = race
        self.name = name
        self.level = level
        self.health = health
        self.mana = mana

    def attack(self, damage):
        print(f"{self.name} is attacking with the damage of {damage}") 

class Druid(Character):
    def __init__(self, gender:str, age:int, race:str, name:str, level:int, health:int, mana:int):
        super().__init__(gender, age, race, name, level, health, mana) 

    def cast(self, ability):
        print(f"Casting {ability}")



druid = Druid("Female", 30, "Night Elf", "yoyoma", 3, 560, 400)
druid_2 = Druid("Female", 29, "Blood Elf", "dadama", 3, 560, 400)
druid.cast("阳炎之怒")
druid.cast("月光术")
