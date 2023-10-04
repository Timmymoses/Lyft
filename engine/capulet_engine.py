from engine.Engine import Engine


class CapuletEngine(Engine):
    def __init__(self, last_service_mileage, current_mileage):
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

    def needs_service(self) -> bool:
        service_criteria = 30000
        return self.current_mileage - self.last_service_mileage >= service_criteria
