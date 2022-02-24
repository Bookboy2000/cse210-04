from game.cast.actor import Actor
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
        
        """Gets the treasure's pounts"""
        return self._points