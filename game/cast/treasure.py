from game.cast.actor import Actor
from game.shared.point import Point
from game.shared.color import Color
import random

class Treasure(Actor):
    """
    Two items to be displayed on screen. Rock and Gems. 

    The responsibility of an this class is to create rocks and gems.

    Attributes:
        _message (string): A short description about the item.
    """

    def __init__(self):
        super().__init__()
        self._message = ""
        self._type_determiner = random.randint(1,10) % 2
        if self._type_determiner == 1:
            super().set_text("*")
            self._points = 100
            self._type = "jewel"
        else:
            super().set_text("O")
            self._points = -100
            self._type = "rock"
        super().set_velocity

    def get_message(self):
        """Gets the treasure's score whether is adding points or losing them.
        
        Returns:
            string: The message.
        """
        return self._message
    
    def set_message(self, message):
        """Updates the message to the given one.
        
        Args:
            message (string): The given message.
        """
        self._message = message
        
    def get_points(self):
        
        """Gets the treasure's points"""
        return self._points
    
    def set_points(self, points):
        
        """Sets the treasure to have new points"""
        
        self._points = points
    
    def reset_item(self):

        """Once the actor gets to the cell just below the top one
        reset_item sets its x axis, sets the color, and sets the type (Jewel or rock)."""
        
        self._type_determiner = random.randint(1,10) % 2
        if self._type_determiner == 1:
            super().set_text("*")
            self._points = 100
            self._type = "jewel"
        else:
            super().set_text("O")
            self._points = -100
            self._type = "rock"
            
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        super().set_color(Color(r, g, b))
            
        
        x = random.randint(1, 599)
        y = 1
        position = Point(x, y)
        position = position.scale(15)
        
        super().set_position(position)