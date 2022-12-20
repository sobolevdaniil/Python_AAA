from enum import Enum
from typing import List, Dict


class PizzaType(Enum):
    """В классе перечислены пиццы возможные для заказа"""
    MARGHERITA = 'MARGHERITA 🧀'
    PEPPERONI = 'PEPPERONI 🍕'
    HAWAIIAN = 'HAWAIIAN 🍍'


class Size(Enum):
    """В классе перечислены возможные размеры пицц"""
    M = '🍕 M'
    L = '🍕🍕 L'
    XL = '🍕🍕🍕 XL'
    XXL = '🍕🍕🍕🍕 XXL'


class Recipe:
    """Класс позволюящий составить заказ"""

    recipes = {
        'MARGHERITA 🧀': 'tomato sauce, mozzarella, tomatoes',
        'PEPPERONI 🍕': 'tomato sauce, mozzarella, pepperoni',
        'HAWAIIAN 🍍': 'tomato sauce, mozzarella, chicken, pineapples',
               }

    def __init__(self) -> None:
        self.order: List[(PizzaType, Size)] = []

    def add_pizza(self, pizza: PizzaType, size: Size) -> None:
        """Добавляет в заказ пиццу из меню"""
        if not isinstance(pizza, PizzaType):
            raise ValueError
        if not isinstance(size, Size):
            raise ValueError
        self.order.append([pizza, size])

    def dict(self) -> Dict[str, str]:
        """Выводит рецепты пицц, входящих в заказ"""
        recipes_used = {}
        unique_pizza = []
        for pizza in self.order:
            if pizza[0] not in unique_pizza:
                unique_pizza.append(pizza[0])
                recipes_used[f'{pizza[0].value}'] = self.recipes[pizza[0].value]
        return recipes_used

    def __eq__(self, other) -> bool:
        """
        Сравнивает заказы
            - True - если заказы идентичны
        """
        if isinstance(other, self.__class__):
            return self.order == other.order
        return False

    def __str__(self) -> str:
        """
        Подмена функции print
            Выводит содержимое заказа
        """
        pizza_ = ''
        for pizza in self.order:
            pizza_ += f'Пицца: {pizza[0].value}, размер: {pizza[1].value} \n'
        return pizza_
