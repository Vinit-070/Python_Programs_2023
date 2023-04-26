# Define a class named Rocket and its subclass MarsRover. 
# The Rocket class has an init function that takes two arguments called rocket_name and target_distance 
# and will initialize object of both classes. Subclass Mars Rover has its own attribute called "Maker". 
# Both classes have a launch() function which prints rocket name and target distance. 
# Class MarsRover prints attribute value of "Maker" inside launch() function.
class Rocket:
    def __init__(self, rocket_name, target_distance):
        self.name = rocket_name
        self.distance = target_distance

    def launch(self):
        print("\nThe Name Of The Rocket Is : "+ self.name)
        print("The Distance From The Target Is : ", self.distance)

class MarsRover(Rocket):
    maker = input("Enter The Name Of The Maker : ")

    def launch(self):
        super().launch()
        print("The Name Of The Maker Is : "+ self.maker)

rocket_name = input("Enter The Name Of The Rocket : ")
target_distance = int(input("Enter The Distance From The Target : "))

obj1 = Rocket(rocket_name,target_distance)
obj1.launch()
obj2 = MarsRover(rocket_name,target_distance)
obj2.launch()
