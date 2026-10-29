class DynamicSign:
    def __init__(self, is_active: bool = True):
        self.is_active = is_active


class TrafficLight(DynamicSign):
    def __init__(self, state: str = "CZERWONE"):
        super().__init__(is_active=True)
        self.state = state

    def change_state(self, new_state: str):
        self.state = new_state
        print(f"[ŚWIATŁA] Zmieniono stan na: {self.state}")

    def next_state(self):
        if self.state == "CZERWONE":
            self.state = "ZIELONE"
        elif self.state == "ZIELONE":
            self.state = "ŻÓŁTE"
        elif self.state == "ŻÓŁTE":
            self.state = "CZERWONE"
        print(f"[ŚWIATŁA] Aktualny stan: {self.state}")