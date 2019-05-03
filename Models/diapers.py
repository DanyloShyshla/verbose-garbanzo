from Models.babyShop import BabyShop

class Diapers:
    def __init__(self, name, brand, price, safety_standard, good_availability, warranty, age_suitability, supplier, country, amount_in_pack, diapers_size, kid_weight):
        super().__init__(self, name, brand, price, safety_standard, good_availability, warranty, age_suitability, supplier, country)
        self.amount_in_pack = amount_in_pack
        self.diapers_size = diapers_size
        self.kid_weight = kid_weight