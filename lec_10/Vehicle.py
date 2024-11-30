class Vehicle:
    def __init__(self, name, model, year):
        self.name = name
        self.model = model
        self.year = year

    def display_info(self):
        return f"{self.year} {self.name} {self.model}"

    def move(self):
        return f"{self.display_info()} is moving."

    def stop(self):
        return f"{self.display_info()} is stopping."
