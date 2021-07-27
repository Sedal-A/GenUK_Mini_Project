class Vehicle:
    
    def __init__(self, speed_max, colour):
        self.speed_max = speed_max
        self.colour = colour

mustang = Vehicle(150, "Blue")
toyatoa = Vehicle(80, "Red")


print(mustang.speed_max)
print(mustang.colour)
#.........................
#.........................
#.........................
#... 2 
class Vehicle:
    
    def __init__(self, speed_max, colour):
        self.speed_max = speed_max
        self.colour = colour
    
    def change_speed_max(self, new_speed_max):
        self.speed_max = new_speed_max
        
    
    def change_colour(self, new_colour):
        self.colour = new_colour

mustang = Vehicle(150, "Blue")
toyatoa = Vehicle(80, "Red")


print(mustang.speed_max)
print(mustang.colour)


mustang.change_speed_max(200)
print(mustang.speed_max)
mustang.change_colour("Red")
print(mustang.colour)

# # THIS IS TO GET INPUT CHANGE
# new_colour = input("Enter a new colour: ")
# mustang.change_colour(new_colour)

#.........................
#.........................
#.........................









