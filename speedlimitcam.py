class Car:
    def __init__(self, brand, color, speed ,plate_number):
        self.brand = brand
        self.color = color
        self.speed = speed
        self.plate_number = plate_number

    def isOutofSpeedlimit(self):
        if int(self.speed) > 60:
            print(f"\nYes, Get Slowly {self.plate_number}!\n")
        else:
            print(f"\nSafe! {self.plate_number}\n")

s = input(("Input brand, color, speed and plate_number(With Space): ")).split()
vehicle = Car(*s) # Unpacks list elements as positional arguments: s[0], s[1]...
vehicle.isOutofSpeedlimit()



    