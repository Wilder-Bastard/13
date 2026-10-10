class Restaurant:
    def __init__(self, restaurant_name, kitchen_type, rating=0):
        self.restaurant_name = restaurant_name
        self.kitchen_type = kitchen_type
        self.rating = rating

    def describe_restaurant(self):
        print("Название:", self.restaurant_name)
        print("Тип кухни:", self.kitchen_type)
        print("Рейтинг:", self.rating)

    def open_restaurant(self):
        print("Ресторан", self.restaurant_name, "открыт!")

    def update_rating(self, new_rating):
        self.rating = new_rating
        print("Рейтинг обновлён до", self.rating)

restaurant = Restaurant("Большой хинкаль", "грузинская", 4)
restaurant.describe_restaurant()
restaurant.update_rating(5)
restaurant.describe_restaurant()