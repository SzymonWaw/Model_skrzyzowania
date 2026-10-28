from abc import abstractmethod, ABC

class RoadUser(ABC):
    def __init__(self, speed : float, pos_x, pos_y, ):
        self.speed = speed
        self.pos_x = pos_x
        self.pos_y = pos_y

    @abstractmethod
    def move(self):
        pass