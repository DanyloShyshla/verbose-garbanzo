from Models.baby_shop import BabyShop


class SkinCare(BabyShop):

    def __init__(self, name, brand, price, safety_standard, good_availability, warranty, age_suitability, supplier,
                 country, hypoallergenic, bottle_size_in_ml, skin_care_type):
        super().__init__(name, brand, price, safety_standard, good_availability, warranty, age_suitability, supplier,
                         country)
        self.hypoallergenic = hypoallergenic
        self.bottle_size_in_ml = bottle_size_in_ml
        self.skin_care_type = skin_care_type
