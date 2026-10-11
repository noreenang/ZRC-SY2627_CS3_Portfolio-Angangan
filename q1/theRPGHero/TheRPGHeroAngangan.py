# Activity 1: The RPG Hero
# Name: Noreen Ysabelle C. Angangan

class Hero:
    def __init__(self, name, hp):
        self.name = name
        self.hp = hp

    def take_damage(self, amount):
        self.hp -= amount

# Make heroes
arthur = Hero("Arthur", 100)
morgana = Hero("Morgana", 100)

# Arthur takes damage
arthur.take_damage(10)

# Output HP statuses
print(f"{arthur.name}'s HP: {arthur.hp}")
print(f"{morgana.name}'s HP: {morgana.hp}")
