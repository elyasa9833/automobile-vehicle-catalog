from mobil import sigra, xpander
import json

cars = [sigra, xpander]

class Dealer:
    def show_all_cars(self):
        # Implement code to show all cars
        for i, car in enumerate(cars):
            print(f"{i+1}: {car.serialize()}\n")
        # pass

    def show_all_car_models(self, brand):
        # Implement code to show all car models for a specific brand
        pass

    def show_car_model_detail(self, brand, model):
        # Implement code to show car model detail for a specific brand and model
        pass

dealer = Dealer()
dealer.show_all_cars()