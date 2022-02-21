class Point:
    """
    Creates points for actors to use

    An instance will hold these values:
    _x
    _y
    """

    def __init__(self, x, y):
        """
        Creates a new point for actors to use
        Values are:
        self._x
        self._y
        """
        self._x = x
        self._y = y
    
    def add_points(self, other):
        """
        Makes a new point that is the sum of to others and returns new point
        """
        x = self._x + other.get_x()
        y = self._y + other.get_y()
        return Point(x, y)


    def equals(self, other):
        """
        Compares the new point to the old one to see if they are equal

        Returns True if equal and False if not.
        """
        return self._x == other.get_x() and self._y == other.get_y()
        

    def get_x(self):
        """
        Gets horizontal distance

        Returns self._x (horizontal)
        """
        return self._x

    
    def get_y(self):
        """
        Gets virtical distance

        Returns self._y (vertical)
        """
        return self._y


    def scale(self, factor):
        """
        Scales our point by the given factor

        Returns x * factor and y * factor
        """
        return Point(self._x * factor, self._y * factor)