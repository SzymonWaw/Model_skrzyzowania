import time

from models.vehicle import Car, Bus, Motor, EmergencyVehicle
from infrastructure.path import Lane
from infrastructure.intersection import Intersection
from signage.dynamic_signs import TrafficLight
from signage.static_signs import PrioritySign, InformationalSign
from logic.rules import SpeedLimitRule, CollisionDetector


def run_simulation():
    print("==================================================")
    print("   SYMULACJA SKRZYŻOWANIA - MODEL OBIEKTOWY (OOP)  ")
    print("==================================================\n")

    intersection = Intersection(name="Skrzyżowanie Centralne")
    main_lane = Lane(lane_id=1, speed_limit=50.0)
    intersection.add_lane(main_lane)

    traffic_light = TrafficLight(state="CZERWONE")
    intersection.add_traffic_light(traffic_light)

    stop_sign = PrioritySign(description="Ustąp pierwszeństwa", grants_priority=False)
    info_sign = InformationalSign(description="Przejście dla pieszych za 50m", info_type="INFORMATYWNY")

    print(f"Stworzono skrzyżowanie: {intersection.name}")
    print(f"Znak stały: {stop_sign.description}")
    print(f"Znak informacyjny: {info_sign.description}\n")

    speed_rule = SpeedLimitRule(speed_limit=main_lane.speed_limit)
    collision_detector = CollisionDetector(min_distance=3.0)

    vehicles = [
        Car(pos_x=0.0, pos_y=0.0, speed=0.0, passenger_count=2),
        Bus(pos_x=-12.0, pos_y=0.0, speed=0.0, passenger_count=20),
        Motor(pos_x=-6.0, pos_y=0.0, speed=0.0, passenger_count=1),
        EmergencyVehicle(pos_x=-20.0, pos_y=0.0, speed=0.0, siren_on=True)
    ]

    for v in vehicles:
        main_lane.add_vehicle(v)

    for step in range(1, 7):
        print(f"--- KROK SYMULACJI NR {step} ---")

        if step == 3:
            print("\n>>> ZDARZENIE: Zmiana świateł! <<<")
            traffic_light.change_state("ZIELONE")
            print()

        for vehicle in vehicles:
            if traffic_light.state == "CZERWONE":
                vehicle.brake(decel_rate=5.0)
            elif traffic_light.state == "ZIELONE":
                vehicle.accelerate()
                vehicle.move()
                speed_rule.check_rule(vehicle)

        for i in range(len(vehicles)):
            for j in range(i + 1, len(vehicles)):
                collision_detector.check_collision(vehicles[i], vehicles[j])

        time.sleep(0.4)

    print("\n==================================================")
    print("       SYMULACJA ZAKOŃCZONA POMYŚLNIE             ")
    print("==================================================")


if __name__ == "__main__":
    run_simulation()
