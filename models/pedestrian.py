from models.road_user import RoadUser

class Pedestrian(RoadUser):
    def move(self):
        self.pos_x += self.speed
