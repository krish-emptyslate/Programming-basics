class car:
    def __init__(self,brand,model,year):
        self.brand = brand
        self.model =model
        self.year = year

    def display_info(self):
            print(f"car {self.brand}{self.model}, Year:{self.year}")

class bike:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year


bike1 = bike("yamaha","rx100",1999)
car1 = car("maruthi","swift",2024)
car2 = car("toyota","innova",2024)
car1.display_info()
