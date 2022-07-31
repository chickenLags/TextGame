

class WeaponTypeNotFoundException(Exception):
    def __int__(self):
        self.message = "weapon type was not found."
