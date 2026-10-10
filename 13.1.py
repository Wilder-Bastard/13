class Restaurant:
    def __init__(self, restaurant_name, kitchen_type):
        self.restaurant_name = restaurant_name
        self.kitchen_type = kitchen_type

    def describe_restaurant(self):
        print("Название:", self.restaurant_name)
        print("Тип кухни:", self.kitchen_type)

    def open_restaurant(self):
        print("Ресторан", self.restaurant_name, "открыт!")

newRestaurant = Restaurant("Большой хинкаль", "грузинская")

print(newRestaurant.restaurant_name)
print(newRestaurant.kitchen_type)

newRestaurant.describe_restaurant()
newRestaurant.open_restaurant()