class Rocket:
    def __init__(self, name, fuel_amount):
        if not name:
            raise ValueError("Missing name")
        if fuel_amount < 0:
            raise ValueError("Fuel amount cannot be negative.")
        self.name = name
        self.__fuel_amount = fuel_amount

    def __str__(self):
        return f"{self.name}"
    
    def fuel(self, fuel_added):
        if (fuel_added > 0):
            self.__fuel_amount += fuel_added
            print(f"Fuel added. New amount: {self.__fuel_amount}")
        else:
            print("Fuel added must be greater than 0.")

    def show_fuel(self):
        print(f"Fuel amount: {self.__fuel_amount}")

    def launch(self):
        if (self.__fuel_amount < 10):
            print("Not enough fuel. Please add fuel.")
        else:
            self.__fuel_amount -= 10
            print(f"{self.name} launched successfully")

def show_fuel(rocket):
    print(f"Fuel amount: {rocket.fuel_amount}")

def test():
    rocket = Rocket("Apollo 49", 0)
    print(rocket)
    rocket.show_fuel()
    rocket.fuel(-5)
    rocket.show_fuel()
    rocket.fuel(0)
    rocket.show_fuel()
    rocket.fuel(7)
    rocket.show_fuel()
    rocket.launch()
    rocket.show_fuel()
    rocket.fuel(3)
    rocket.show_fuel()
    rocket.launch()
    rocket.show_fuel()
    rocket.fuel(5)
    rocket.show_fuel()
    rocket.launch()
    rocket.show_fuel()
    rocket.__fuel_amount = 100 # fuel amount dışardan değiştirilemiyor
    rocket.show_fuel()

if __name__ == "__main__":
    test()