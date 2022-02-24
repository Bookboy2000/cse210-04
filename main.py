import os
import random

from game.cast.actor import Actor
from game.cast.treasure import Treasure
from game.cast.cast import Cast

from game.directing.director import Director

from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService

from game.shared.color import Color
from game.shared.point import Point

FRAME_RATE = 12
MAX_X = 900
MAX_Y = 600
CELL_SIZE = 15
FONT_SIZE = 15
COLS = 60
ROWS = 40
CAPTION = "Greed"
WHITE = Color(255, 255, 255)
DEFAULT_TREASURES = 40

def main():
    
    # create the cast
    cast = Cast()
    
    # create the banner
    banner = Actor()
    banner.set_text("")
    banner.set_font_size(FONT_SIZE)
    banner.set_color(WHITE)
    banner.set_position(Point(CELL_SIZE, 0))
    cast.add_actor("banners", banner)
    
    # create the player
    x = int(MAX_X / 2)
    y = int(MAX_Y / 2)
    position = Point(x, y)

    miner = Actor()
    miner.set_text("#")
    miner.set_font_size(FONT_SIZE)
    miner.set_color(WHITE)
    miner.set_position(position)
    cast.add_actor("miners", miner)
    
    for n in range(DEFAULT_TREASURES):

        x = random.randint(1, COLS - 1)
        y = 0
        position = Point(x, y)
        position = position.scale(CELL_SIZE)

        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        color = Color(r, g, b)
        
        treasure = Treasure()
        treasure.set_font_size(FONT_SIZE)
        treasure.set_color(color)
        treasure.set_position(position)
        cast.add_actor("treasures", treasure)

    keyboard_service = KeyboardService(CELL_SIZE)
    video_service = VideoService(CAPTION, MAX_X, MAX_Y, CELL_SIZE, FRAME_RATE)
    director = Director(keyboard_service, video_service)
    director.start_game(cast)
    
if __name__ == "__main__":
    main()