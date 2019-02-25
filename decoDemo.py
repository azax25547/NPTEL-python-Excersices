class Harley():
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
        print("harley Seat")

    # decorator
    @property
    def top_speed(self):
        return self.features.get('topSpeed', None)

    @top_speed.setter
    def top_speed(self, ts):
        self.features['topSpeed'] = ts

    @top_speed.deleter
    def top_speed(self):
        del self.features['topSpeed']


def main():
    streetBob = Harley()
    streetBob.set_features("cc", "1800")
    print(streetBob.get_features("cc"))

    streetBob.top_speed = "300"
    print(streetBob.top_speed)


if __name__ == "__main__":
    main()
