class Color:
    """
    The Color class will provide the visual game with colors using several methods and even tuple
    
    An instance will hold these variables:
    _red
    _green
    _blue
    _alpha
    """

    def __init__(self, red, green, blue, alpha = 255):
        """
        Creates a new instance of Color based on random RGB values.
        """
        self._red = red
        self._green = green
        self._blue = blue
        self._alpha = alpha

    def to_tuple(self):
        """
        Simply returns RGB and opacity values

        return:
            Tuple:(int, int, int, int) All values are ints
        """
        return(self._red, self._green, self._blue, self._alpha)