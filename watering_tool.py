from abc import ABCMeta
from abc import abstractmethod

class WateringTool(metaclass=ABCMeta):
    @abstractmethod
    def water(self):
        pass

    @abstractmethod
    def stop_water(self):
        pass

class Pomp(WateringTool):
    def __init__(self):
        pass
    def water(self):
        print("水をあげます")

    def stop_water(self):
        print("水を止めます")