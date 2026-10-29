from path import Lane

class Intersection:
    def __init__(self, name: str):
        self.name = name
        self.lanes = []
        self.traffic_lights = []

    def add_lane(self, lane: Lane):
        self.lanes.append(lane)

    def add_traffic_light(self, light):
        self.traffic_lights.append(light)