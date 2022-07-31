
class NoItemFoundException(Exception):
    def __int__(self, searched_name):
        super(f"No item named {searched_name} found.")