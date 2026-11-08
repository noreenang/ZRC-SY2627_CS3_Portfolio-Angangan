
# ACTIVITY 2: Duck Typing and Polymorphism


# 2.1 Answer the following questions:

# a. What is duck typing, as explained in the video?
# Answer: Duck typing is another way to achieve Polymorphism besides using Inheritance. Objects can be treated as if they're a different type as long as they meet the minimum attributes and methods required.


# b. What did the Car class need to have so it could work inside the same loop as Dog and Cat, even if it does not inherit from the Animal class?
# Answer: The Car class needed to have a move() method so it could work with Dog and Cat in the same loop.


# 2.2 Create the Python code:



class Car:
    def move(self):
        print("The car drives on the road.")


class Boat:
    def move(self):
        print("The boat sails on water.")


class Drone:
    def move(self):
        print("The drone flies in the sky.")




def start_trip(vehicle):
    vehicle.move()



car = Car()
boat = Boat()
drone = Drone()


print("Output:")
start_trip(car)
start_trip(boat)
start_trip(drone)


# 2.3 How does the code in 2.2 demonstrate polymorphism?
# Answer: The code demonstrates polymorphism because all three classes use the same move() method but perform different actions.
