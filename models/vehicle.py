from models.road_user import RoadUser

class Vehicle(RoadUser):
    def __init__(self, pos_x: float, pos_y: float, speed: float, max_speed: float, acceleration: float):
        super().__init__(pos_x, pos_y, speed)
        self.max_speed = max_speed
        self.acceleration = acceleration
        self.is_stopped = False

    def brake(self, decel_rate: float):
        self.speed -= decel_rate
        if self.speed <= 0:
            self.speed = 0.0
            self.is_stopped = True

    def accelerate(self):
        if not self.is_stopped:
            self.speed += self.acceleration
            if self.speed > self.max_speed:
                self.speed = self.max_speed

    def move(self):
        if not self.is_stopped:
            self.pos_x += self.speed


class Car(Vehicle):
    def __init__(self, pos_x: float, pos_y: float, speed: float, passenger_count: int):
        super().__init__(pos_x, pos_y, speed, max_speed=130.0, acceleration=5.0)
        self.passenger_count = passenger_count

    def move(self):
        super().move()
        print(f"Samochód (Pasażerowie: {self.passenger_count}) jedzie na pozycji X: {self.pos_x:.1f} z prędkością: {self.speed:.1f}")


class Bus(Vehicle):
    def __init__(self, pos_x: float, pos_y: float, speed: float, passenger_count: int):
        super().__init__(pos_x, pos_y, speed, max_speed=50.0, acceleration=2.0)
        self.passenger_count = passenger_count

    def move(self):
        super().move()
        print(f"Bus (Pasażerowie: {self.passenger_count}) jedzie na pozycji X: {self.pos_x:.1f} z prędkością: {self.speed:.1f}")

class Motor(Vehicle):
    def __init__(self, pos_x: float, pos_y: float, speed: float, passenger_count: int):
        super().__init__(pos_x, pos_y, speed, max_speed=150.0, acceleration=8.0)
        self.passenger_count = passenger_count

    def move(self):
        super().move()
        print(f"Motor (Pasażerowie: {self.passenger_count}) jedzie na pozycji X: {self.pos_x:.1f} z prędkością: {self.speed:.1f}")



