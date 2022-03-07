#author (AMDG) 3/4/22
#input statements to use in function 
wheels = int(input("Enter the number of wheels: "))
axel = int(input("enter the number of axels: "))
doors= int(input("Enter the number of doors: "))
color= input("Enter the color of the car: ")

def build_vehicle(wheels, axel, doors, color):
    print("Your car has {0} wheels {1} axels {2} doors and is the color {3}.".format(wheels, axel, doors, color))
build_vehicle(wheels, axel, doors, color)