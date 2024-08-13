from mobil import cars

class Dealer:
    def show_all_cars(self):
        # Implement code to show all cars
        for i, car in enumerate(cars):
            print(f"{i+1}. Brand: {car.merk}, Model: {car.model}")

    def show_all_car_models(self, brand):
        # Implement code to show all car models for a specific brand
        car_models = []
        for car in cars:
            if car.merk == brand:
                car_models.append(car.model)
        return car_models

    def show_car_model_detail(self, brand, model):
        # Implement code to show car model detail for a specific brand and model
        for car in cars:
            if car.merk == brand and car.model == model:
                return car.serialize()
        return None

