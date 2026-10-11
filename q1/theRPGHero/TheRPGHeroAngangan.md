# Activity 1: The RPG Hero

**Student Name:** Noreen Ysabelle C. Angangan  
**Section:** IX- Potassium  

---

## 1. Problem Requirements

* **Define:** Create a `Hero` class with attributes `name` and `hp`.
* **Act:** Add a method `take_damage(amount)` that subtracts from `hp`.
* **Instantiate:** Create two heroes: `Arthur` and `Morgana`. Make Arthur and Morgana. Make Arthur take 10
 damage. Print both their HPs to see that Morgana is still at full health!
---

## 2. Python Source Code (`TheRPGHero.py`)

```python
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
```
