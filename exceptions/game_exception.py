from dataclasses import dataclass


# this class is used for exceptions that shouldn't kill the game but only stop and return to the
# main loop.
@dataclass
class GameException(Exception):
    message: str
