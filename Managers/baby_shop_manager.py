from Models.chair import Chair
from Models.SafetyStandard import SafetyStandard
from Models.diapers import Diapers
from Models.DiapersSize import DiapersSize
from Models.KidWeight import KidWeight
from Models.thermometer import Thermometer
from Models.ThermometerType import ThermometerType
from Models.skin_care import SkinCare
from Models.SkinCareType import SkinCareType


class BabyShopManager:
    def __init__(self, baby_shop_list):
        self.baby_shop_list = baby_shop_list

    def find_good_by_age(self, age_suitability):
        return list(filter(lambda good: good.age_suitability == age_suitability, self.baby_shop_list))

    def sort_good_by_price(self, reverse):
        return sorted(self.baby_shop_list, key=lambda good: good.price, reverse=reverse)

    def sort_good_by_warranty(self, reverse):
        return sorted(self.baby_shop_list, key=lambda good: good.warranty, reverse=reverse)


chair = Chair(name="Brand chair", brand="Chicco", price=2999, safety_standard=SafetyStandard.EN_1400_2013,
              good_availability=14, warranty=30, age_suitability=3, supplier="National delivery", country="Ukraine",
              height=56, width=44, depth=42, weight_limit=50, material="wood")
diapers = Diapers("Pampers active", "Pampers", 249.99, SafetyStandard.EN_1400_2019, 17, 0, 1, "delivery", "China", 250,
                  DiapersSize.MEDIUM, KidWeight.FROM_3_TO_6)
thermometer = Thermometer("Thermometer", "Thermometer", 120, SafetyStandard.EN_1400_2016, 10, 90, 3, "delivery",
                          "Italy", "white", ThermometerType.INFRARED)
skin_care = SkinCare("Skin creme", "Bubchen", 320.99, SafetyStandard.EN_1400_2016, 30, 0, 1, "Skin care delivery",
                     "France", True, 200, SkinCareType.CREME)
goods = [thermometer, diapers, chair, skin_care]
manager = BabyShopManager(goods)
print(chair)
print(manager.find_good_by_age(3))
print(manager.sort_good_by_price(True))
print(manager.sort_good_by_warranty(True))
