class TrafficRule:
    def __init__(self, description: str):
        self.description = description

    def check_rule(self, vehicle, context) -> bool:
        raise NotImplementedError("Musisz zaimplementować tę metodę w klasie pochodnej.")


class SpeedLimitRule(TrafficRule):
    def __init__(self, speed_limit: float):
        super().__init__("Ograniczenie prędkości")
        self.speed_limit = speed_limit

    def check_rule(self, vehicle, context=None) -> bool:
        if vehicle.speed > self.speed_limit:
            print(f"[ZASADA] OSTRZEŻENIE: Pojazd jedzie za szybko! ({vehicle.speed} km/h przy limicie {self.speed_limit})")
            return False
        return True


class RightHandRule(TrafficRule):
    def __init__(self):
        super().__init__("Zasada pierwszeństwa z prawej")

    def check_rule(self, vehicle, other_vehicle) -> bool:
        print(f"[ZASADA] Sprawdzanie pierwszeństwa z prawej dla pojazdów.")
        return True


class CollisionDetector(TrafficRule):
    def __init__(self, min_distance: float = 2.0):
        super().__init__("Detekcja kolizji")
        self.min_distance = min_distance

    def check_collision(self, vehicle1, vehicle2) -> bool:
        distance = abs(vehicle1.pos_x - vehicle2.pos_x)
        if distance < self.min_distance and vehicle1 != vehicle2:
            print(f"[KOLIZJA] Niebezpieczna odległość między pojazdami! Odległość: {distance:.1f}")
            return True
        return False