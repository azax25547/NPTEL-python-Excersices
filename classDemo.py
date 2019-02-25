from inherit import Bike


class Harley(Bike):
    def __init__(self, **kwargs):
        self.features = kwargs

    def big_engine(self):
        print("Big Engine")

    def loud_sound(self):
        print("potato sound")

    def set_features(self, k, v):
        self.features[k] = v

    def get_features(self, k):
        return self.features.get(k, None)

    def seat(self):
        super().seat()
        print("harley Seat")
