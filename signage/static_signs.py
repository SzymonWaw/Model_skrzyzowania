class Sign:
    def __init__(self, description: str):
        self.description = description

class PrioritySign(Sign):
    def __init__(self, description: str, grants_priority: bool):
        super().__init__(description)
        self.grants_priority = grants_priority


class ProhibitiveSign(Sign):
    def __init__(self, description: str, speed_limit: float = None):
        super().__init__(description)
        self.speed_limit = speed_limit

class WarningSign(Sign):
    def __init__(self, description: str, hazard_type: str):
        super().__init__(description)
        self.hazard_type = hazard_type

class InformationalSign(Sign):
    def __init__(self, description: str, info_type: str):
        super().__init__(description)
        self.info_type = info_type