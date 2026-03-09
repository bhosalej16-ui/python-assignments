class Vehicle:
    def move(self):
        print("Vehicle is moving")
class car(Vehicle):
    def move(self):
         print ("Driving on the road")
class bicycle(Vehicle):
    def move(self):
        print("Pedelling on the road")


v1 = car()
v2 = bicycle()
v1.move()
v2.move()