class Restaurant:
    def __init__(self, restaurant_name, kitchen_type):
        self.restaurant_name = restaurant_name
        self.kitchen_type = kitchen_type

    def describe_restaurant(self):
        print("Название:", self.restaurant_name)
        print("Тип кухни:", self.kitchen_type)
        print("-" * 20)

    def open_restaurant(self):
        print("Ресторан", self.restaurant_name, "открыт!")

restaurant1 = Restaurant("Большой хинкаль", "грузинская")
restaurant2 = Restaurant("Долма и точка", "армянская")
restaurant3 = Restaurant("Шашлык-башлык", "азербайджанская")

restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()