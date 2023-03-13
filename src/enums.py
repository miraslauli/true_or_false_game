from enum import Enum


class GameStatus(Enum):     # Status of our game
    WON = 1
    LOST = 2
    IN_PROGRESS = 3
    NOT_STARTED = 4
