import time
from models.vehicle import Car, Bus, Motor
from signage.dynamic_signs import TrafficLight


def run_simulation():
    print("=== URUCHAMIANIE SYMULACJI SKRZYŻOWANIA ===")

    traffic_light = TrafficLight(state="CZERWONE")

    vehicles = [
        Car(pos_x=0.0, pos_y=0.0, speed=0.0, passenger_count=2),
        Bus(pos_x=-10.0, pos_y=0.0, speed=0.0, passenger_count=15),
        Motor(pos_x=-5.0, pos_y=0.0, speed=0.0, passenger_count=1)
    ]

    for step in range(1, 6):
        print(f"\n--- KROK SYMULACJI NR {step} ---")

        if step == 3:
            print("[ZDARZENIE] Światła zmieniają się na zielone!")
            traffic_light.change_state("ZIELONE")

        for vehicle in vehicles:
            if traffic_light.state == "CZERWONE":
                vehicle.brake(decel_rate=5.0)
                print(f"{vehicle.__class__.__name__} stoi na czerwonym świetle.")
            elif traffic_light.state == "ZIELONE":
                vehicle.accelerate()
                vehicle.move()

        time.sleep(0.5)

    print("\n=== SYMULACJA ZAKOŃCZONA SUKCESEM ===")


if __name__ == "__main__":
    run_simulation()
