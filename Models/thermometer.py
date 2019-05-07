from Models.baby_shop import BabyShop


class Thermometer(BabyShop):

    def __init__(self, name, brand, price, safety_standard, good_availability, warranty, age_suitability, supplier,
                 country, color, thermometer_type):
        super().__init__(name, brand, price, safety_standard, good_availability, warranty, age_suitability,
                         supplier, country)
        self.color = color
        self.thermometer_type = thermometer_type
