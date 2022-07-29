from locations.Location import TopLevelLocation
from locations.location_base import LocationBase


class LocationLeaveGameInstance(LocationBase):
    def __init__(self, instance, character):
        super().__init__(instance, character)
        exit()
