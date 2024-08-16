class car:
   """An indicator for the coordinates of a car and the direction it's heading in.

   Attributes:
        x (int)= the first value listed in the coordinates, representing a position horizontally.
        y (int)= the second value listed in the coordinates, representing a position vertically.
        heading (str)= a string representing what direction the car is traveling.

    """
   def __init__(self):
    """Initialize a new object for the car class.

    Side effects:
        Sets attributes x, y, and heading.
    """
    self.x = 0
    self.y = 0
    self.heading = "n"

   def turn(self, direction):
    """Indicates which direction the car is turning.

    Once the direction of the car is known, the way the car is heading is updated to that direction.
    
    Args:
        direction (str): can be either right(r) or left(l). 
    
    Side effect:
        Has the ability to change the value of the heading attribute. 
    
    """
    heading_values = ["n", "e", "s", "w"]
    heading_index = heading_values.index(self.heading)

    if direction == "r":
            updated_heading = heading_index + 1

    if direction == "l":
            updated_heading = heading_index - 1
        
    self.heading = heading_values[updated_heading]

   def drive (self, distance = 1):
       """Add or subtract the distance from a cooridanate based on the direction its heading.
       
       Args:
            distance (int): an integer representing how far the car has traveled in a given direction.
            
       Side effects:
            Can increase or decrease coordinate values.
        """
    
       if self.heading == "n":
           self.y += distance
       if self.heading == "e":
           self.x += distance
       if self.heading == "s":
           self.y -= distance
       if self.heading == "w":
           self.x -= distance
   
   def status (self):
       """Indicates the current state of the car.

       Takes each attribute into account and prints them into a simple format. 

       Acts as the 'result' of the rest of the code above. 
       """
       print(f"Coordinates: {self.x}, {self.y} \n Heading: {self.heading}")


    









