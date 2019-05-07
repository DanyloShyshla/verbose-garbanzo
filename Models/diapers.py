from Models.baby_shop import BabyShop


class Diapers(BabyShop):

    def __init__(self, name, brand, price, safety_standard, good_availability, warranty, age_suitability, supplier,
                 country, amount_in_pack, diapers_size, kid_weight):
        super().__init__(name, brand, price, safety_standard, good_availability, warranty, age_suitability, supplier, country)
        self.amount_in_pack = amount_in_pack
        self.diapers_size = diapers_size
        self.kid_weight = kid_weight
