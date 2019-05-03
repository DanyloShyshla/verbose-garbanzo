from Models.babyShop import BabyShop

class Chair(BabyShop):
    def __init__(self, name, brand, price, safety_standard, good_availability, warranty, age_suitability, supplier, country, heigh, width, depth, weight_limit, material):
        super().__init__(name, brand, price, safety_standard, good_availability, warranty, age_suitability, supplier, country)
        self.heigh = heigh
        self.width = width
        self.depth = depth
        self.weight_limit = weight_limit
        self.material = material
