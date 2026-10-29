class Lane:
    def __init__(self, lane_id: int, speed_limit: float):
        self.lane_id = lane_id
        self.speed_limit = speed_limit
        self.vehicles_on_lane = []

    def add_vehicle(self, vehicle):
        self.vehicles_on_lane.append(vehicle)

    def remove_vehicle(self, vehicle):
        self.vehicles_on_lane.remove(vehicle)