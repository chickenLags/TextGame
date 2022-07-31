

class MaterialNotFoundException(Exception):
    def __int__(self):
        self.message = "material was not found."
