import string

from exceptions.game_exception import GameException


class NoEquipmentFoundException(GameException):
    def __int__(self, search_term: string):
        super(f"No equipment named \"{search_term}\" found.")