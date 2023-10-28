class Zoo:
    zoo_name = "zoo"
    total_animals = 0

     def __init__(self, animal_type, name, can_fly=False, can_swin=False):

         self.animal_type = animal_type
         self.name = name
         self.can_fly = can_fly
         self.can_swim = can_swin
         Zoo.total_animals += 1

     def fly(self):
         if self.can_fly:
             print(f"{self.name}Полетел")
         else:
             print(f"{self.name}Не смог полететь")
    def swim(sefl):
if self.can_swim:
    print(f"{self.name}поплыл")
else:
    print(f"{self.name}Не смог поплыть")

fish= Zoo("рыба", can_swin=True)
crocodile = Zoo("крокодил", can_swin=True)
bird = Zoo("птица", can_fly=True)
coala = Zoo("коала", can_swin=False)
fish.swim()
crocodile.swim()
bird.fly()
coala.swim()
print(f"Название зоопарку: {Zoo.zoo_name}")
print(f"Сколько всего животных: {Zoo.total_animals}")