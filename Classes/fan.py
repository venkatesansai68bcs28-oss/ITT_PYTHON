class Fan:
    def __init__(self, speed="Medium"):
        self.speed = speed

    def status(self):
        print(f"The fan speed is set to {self.speed}.")
my_fan = Fan()
my_fan.status()