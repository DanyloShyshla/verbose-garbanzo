from Models.chair import Chair
from Models.SafetyStandard import SafetyStandard
from Models.diapers import Diapers
from Models.DiapersSize import DiapersSize
from Models.KidWeight import KidWeight


class BabyShopManager:
    def __init__(self, baby_shop_list):
        self.baby_shop_list = baby_shop_list


chair = Chair(name="Brand chair", brand="Chicco", price=2999, safety_standard=SafetyStandard.EN_1400_2013,
              good_availability=14, warranty=30, age_suitability=3, supplier="National delivery", country="Ukraine",
              heigh=56, width=44, depth=42, weight_limit=50, material="wood")

print(chair)
