from game.cast.actor import Actor

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

    def get_message(self):
        """Gets the treasure's message.
        
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