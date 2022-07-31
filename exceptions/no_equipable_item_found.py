import string


class NoEquipmentFoundException(Exception):
    def __int__(self, search_term: string):
        super(f"No equipment named {search_term} found.")