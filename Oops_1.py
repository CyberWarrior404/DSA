#composition"programing classes(a blueprint of how objects are going to behave) objects(this is an instance of a class) and its methods"
#inheritance"""
#abstraction
#encapsulation
class vehicle:
    def __init__(self, x, y, z):
        self.wheels = x
        self.people = y
        self.colors = z

    def Get_Vehicle_Type(self):
        if self.wheels == 2:
            print("its a bike")
        elif self.wheels == 4:
            print("its a car")
        else:
            print("its a bus or a truck")

object_1 = vehicle(4, 5, "blue")
vehicle_2= vehicle(2, 2, "red")
print(object_1.wheels)
print(vehicle_2.colors)
object_1.Get_Vehicle_Type()
vehicle_2.Get_Vehicle_Type()


class car(vehicle):
    def __init__(self, x, y, z, d):
        super().__init__(x, y, z)
        self.doors = d


bmw = car(4,5,"black",4)
print(bmw.doors)
print(bmw.people)
bmw.Get_Vehicle_Type()
#create a child class bike and implement inheritance and create a method
class bike(vehicle):
    def __init__(self, x, y, z, t):
        super().__init__(x, y, z)
        self.type = t

    def Ride(self):
        print("The bike is ready to ride!")


bike_1 = bike(2, 2, "red", "mountain")
print(bike_1.type)
print(bike_1.colors)
bike_1.Get_Vehicle_Type()
bike_1.Ride()

