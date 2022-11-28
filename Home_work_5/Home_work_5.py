class BaseAdvert:

    def __init__(self, dictionary):
        self.dictionary = {}
        for key, value in dictionary.items():
            self.dictionary[key] = value

    def __getattr__(self, key):
        value = self.dictionary.get(key)
        if isinstance(value, dict):
            return BaseAdvert(value)
        return value
# out location ?


class ColorizeMixin:

    def __repr__(self):
        return f'\033[0;{self.repr_color_code};48m{self.title} | {self.price} ₽\033[0m'
# Как убрать предупреждения ?


class Advert(ColorizeMixin):
    repr_color_code = 32

    def __init__(self, dictionary):
        if 'price' not in dictionary:
            dictionary['price'] = 0
        elif dictionary['price'] < 0:
            raise ValueError
        self.vocabulary = BaseAdvert(dictionary)

    def __getattr__(self, key):
        return self.vocabulary.__getattr__(key)

    def __repr__(self):
        return super().__repr__()
# В задании нужно добавлять к атрибутам подчеркивание (price_) - зачем?
# Почему нельзя обходиться без миксина?


lesson_str = {
              "title": "python",
              "price": 10,
              "location": {
                  "address": "город Москва, Лесная, 7",
                  "metro_stations": "Белорусская"
                  }
}

ex = Advert(lesson_str)
print(ex.price)
