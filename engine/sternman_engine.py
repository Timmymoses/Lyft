from engine.Engine import Engine


class SternmanEngine(Engine):
    def __init__(self, warning_light_is_on: bool):
        self.service_indicator = warning_light_is_on

    def needs_service(self):
        return self.service_indicator
