class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.is_running = False

    def start_running(self):
        if not self.is_running:
            self.is_running = True
            print(f"The {self.year} {self.make} {self.model} is now running.")
        else:
            print(f"The {self.year} {self.make} {self.model} is already running.")

    def stop_running(self):
        if self.is_running:
            self.is_running = False
            print(f"The {self.year} {self.make} {self.model} has stopped running.")
        else:
            print(f"The {self.year} {self.make} {self.model} is already stopped.")

    def display_info(self):
        print(f"Car Info: {self.year} {self.make} {self.model}")

car1 = Car("Toyota", "Camry", 2020)
car1.display_info()
car2 = Car("Honda", "Civic", 2019)
car2.display_info()
car1.start_running()
car1.start_running()
car1.stop_running()
car1.stop_running()

class ElectricCar(Car):
    def __init__(self, make, model, year, battery_size):
        super().__init__(make, model, year)
        self.battery_size = battery_size
        self.is_running = False

    def display_info(self):
        return super().display_info()

    def charge_battery(self):
        print(f"The {self.year} {self.make} {self.model} is charging its {self.battery_size}-kWh battery.")

    def start_running(self):
        return super().start_running()

    def stop_running(self):
        return super().stop_running()

ecar1 = ElectricCar("Tesla", "Model 3", 2021, 75)
ecar1.display_info()
ecar1.charge_battery()
ecar1.start_running()
ecar1.start_running()
ecar1.stop_running()
ecar1.stop_running()


