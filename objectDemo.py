from classDemo import Harley


def main():
    streetBob = Harley()
    streetBob.set_features("cc", "1800")
    print(streetBob.get_features("cc"))
    streetBob.big_engine()
    streetBob.seat()


if __name__ == "__main__":
    main()
