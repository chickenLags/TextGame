
from exceptions.game_exception import GameException


class NoItemFoundException(GameException):
    def __init__(self, searched_name):
        self.message = f"No item named \"{searched_name}\" found."