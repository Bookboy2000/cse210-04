from tkinter import font
from game.shared.point import Point
from game.shared.color import Color

class Actor:
    """
    An actor is the gems and rocks as well as the player

    The actor class is where actors are defined and given their various properties.

    An instance will hold these values:
    _points,
    _color,
    _position,
    _velocity
    """

    def __init__(self):
        """
        Creates new actor
        """
        self._points = 0
        # _points is a new variable to replace the text variable.
        # It holds the amount of points given to, or taken from the player opon colecting any given actor
        # There is also no font_size variable.
        # This is all new, so if we need to change the way we do the _points variable I'm happy to help out!
        self._color = Color(255, 255, 255)
        self._position = Point(0, 0)
        self._velocity = Point(0, 0)
        self._text = ""
        self._font_size = 15


    def get_color(self):
        """
        Gets the color for the gems and rocks

        Return self._color
        """
        return self._color


    def get_position(self):
        """
        Gets the position for gems and rocks

        Return self._position
        """
        return self._position

    
    def get_velocity(self):
        """
        Gets the velocity for gems and rocks

        Return self._velocity
        """
        return self._velocity


    def get_points(self):
        """
        Gets the points for gems and rocks

        Return self._points
        """
        return self._points
    
    def get_text(self):
        """
        Gets the message associated with the actor
        Return self._message
        """

        return self._text
    
    def get_font_size(self):
        """Gets the actor's font size.
        
        Returns:
            Point: The actor's font size.
        """
        return self._font_size
    
    def move(self, max_x, max_y):
        """
        Moves the gems and rocks based on their position and velocity
        Also when velocity reaches max actor will wrap around to the other side of the screen
        """
        x = (self._position.get_x() + self._velocity.get_x()) % max_x
        y = (self._position.get_y() + self._velocity.get_y()) % max_y
        self._position = Point(x, y)


    def set_color(self, color):
        """
        Updates the color with the given one
        """
        self._color = color


    def set_points(self, points):
        """
        Updates the point value with given one
        """
        self._points = points

    
    def set_position(self, position):
        """
        Updates the position with the given one
        """
        self._position = position


    def set_velocity(self, velocity):
        """
        updates the velocity with the given one
        """
        self._velocity = velocity
        
    def set_text(self, text):
        """
        Updates the message with the given message
        """
        
        self._text = text
        
    def set_font_size(self, font_size):
        """
        Sets the font size to a specified size
        """
        self._font_size = font_size
        
    def move_next(self, max_x, max_y):
        """Moves the actor to its next position according to its velocity. Will wrap the position 
        from one side of the screen to the other when it reaches the given maximum x and y values.
        
        Args:
            max_x (int): The maximum x value.
            max_y (int): The maximum y value.
        """
        x = (self._position.get_x() + self._velocity.get_x()) % max_x
        y = (self._position.get_y() + self._velocity.get_y()) % max_y
        self._position = Point(x, y)
