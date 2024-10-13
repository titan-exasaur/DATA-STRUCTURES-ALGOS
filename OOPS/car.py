class Car:
    def __init__(self, 
                 model:str, 
                 year:int, 
                 color:str, 
                 for_sale:bool ):
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale

    def drive(self):
        print(f"{self.model} Car is driving") # unique for each object
        print("The car is driving") # same for all objects

    def stop(self):
        print(f"{self.model} Car is stopped")
        print("The car is stopped")

    def describe(self):
        print(f"Model: {self.model}, Year: {self.year}, Color: {self.color}")