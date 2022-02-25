# We can use inheritance in multiple instances on directory 
# when making use of other classes.

class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        _keyboard_service (KeyboardService): For getting directional input.
        _video_service (VideoService): For providing video output.
    """

    def __init__(self, keyboard_service, video_service):
        """Constructs a new Director using the specified keyboard and video services.
        
        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
            video_service (VideoService): An instance of VideoService.
        """
        self._keyboard_service = keyboard_service
        self._video_service = video_service
        self._score = 0
        
    def start_game(self, cast):
        """Starts the game using the given cast. Runs the main game loop.

        Args:
            cast (Cast): The cast of actors.
        """
        self._video_service.open_window()
        while self._video_service.is_window_open():
            self._get_inputs(cast)
            self._do_updates(cast)
            self._do_outputs(cast)
        self._video_service.close_window()

    def _get_inputs(self, cast):
        """Gets directional input from the keyboard and applies it to the miner.
        
        Args:
            cast (Cast): The cast of actors.
        """
        miner = cast.get_first_actor("miners")
        velocity = self._keyboard_service.get_direction()
        miner.set_velocity(velocity)        

    def _do_updates(self, cast):
        """Updates the miner's position and resolves any collisions with treasures.
        
        Args:
            cast (Cast): The cast of actors.
        """
        banner = cast.get_first_actor("banners")
        miner = cast.get_first_actor("miners")
        treasures = cast.get_actors("treasures")

        banner.set_text(f"SCORE: {self._score}")
        max_x = self._video_service.get_width()
        max_y = self._video_service.get_height()
        miner.move_next(max_x, max_y)
        
        for treasure in treasures:
            treasure.move_next(max_x, max_y)
            if treasure.get_position().get_y() == 0:
                treasure.reset_item()
            
                
            if miner.get_position().equals(treasure.get_position()):
                tempscore = treasure.get_points()
                self._score += tempscore
                banner.set_text(f"SCORE: {str(self._score)}") 
           
        
    def _do_outputs(self, cast):
        """Draws the actors on the screen.
        
        Args:
            cast (Cast): The cast of actors.
        """
        
        self._video_service.clear_buffer()
        actors = cast.get_all_actors()
        self._video_service.draw_actors(actors)
        self._video_service.flush_buffer()