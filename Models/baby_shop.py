class BabyShop:
    def __init__(self, name, brand, price, safety_standard, good_availability, warranty, age_suitability, supplier,
                 country):
        self.name = name
        self.brand = brand
        self.price = price
        self.safety_standard = safety_standard
        self.good_availability = good_availability
        self.warranty = warranty
        self.age_suitability = age_suitability
        self.supplier = supplier
        self.country = country

    def __del__(self):
        print("Object " + self.name + " was deleted")

    def __str__(self):
        return str(self.__dict__)
