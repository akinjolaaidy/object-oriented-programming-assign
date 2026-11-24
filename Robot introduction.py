class Robot:
    maker = "Bright Bots"                

    def __init__(self, name, model, battery):
      
        self.name = name
        self.model = model
        self.battery = max(0, min(100, battery))

    def introduce(self):
        return f"Hi, I am {self.name}, a {self.model} robot made by {self.maker}. Battery: {self.battery}%"

    def charge(self, amount):
        if amount <= 0:
            return "Charge amount must be positive."
        self.battery = min(100, self.battery + amount)
        return f"{self.name} charged to {self.battery}%"

tom = Robot("Tom", "T-100", 40)
jerry = Robot("Jerry", "J-200", 120)
print(tom.introduce())                                         
print(jerry.introduce())
print(tom.charge(50))                                          
print(tom.charge(30))                                        
print(tom.charge(-5))                                       
