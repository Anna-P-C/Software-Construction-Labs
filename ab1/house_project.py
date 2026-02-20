class House:
    def __init__(self, area=100, price=100000):

        self._area = area
        self._price = price

    def final_price(self, discount=0):

        return self._price * (1 - discount / 100)
#виправлення по Issue #1
    def get_details(self):
        return f"House(area={self._area}, price={self._price})"

class SmallHouse(House):
#виправлення по Issue #2
    DEFAULT_AREA = 40
    
    def __init__(self):

        super().__init__(area=self.DEFAULT_AREA)


class Human:
    # Статичні атрибути
    default_name = "John Doe"
    default_age = 30
#виправлення по Issue #2
    DEFAULT_DISCOUNT = 10

    def __init__(self, name, age, money=0, house=None):

        self.name = name
        self.age = age
        self.__money = money
        self.__house = house

    def info(self):
#виправлення по Issue #1
        house_info = self.__house.get_details() if self.__house else "No house"
        print(f"Name: {self.name}, Age: {self.age}, Money: {self.__money}, House: {house_info}")

    @staticmethod
    def default_info():

        print(f"Default name: {Human.default_name}, Default age: {Human.default_age}")

    def __make_deal(self, house, price):

        self.__money -= price
        self.__house = house
        print(f"{self.name} купив будинок площею {house._area} м2 за {price}.")

    def earn_money(self, amount):
#виправлення по Issue #3:
        if amount > 0:
            self.__money += amount
            print(f"{self.name} заробив {amount}. Зараз має {self.__money}.")
        else:
            print("Сума заробітку повинна бути більшою за нуль!")
            
    def buy_house(self, house, discount=DEFAULT_DISCOUNT):

        price = house.final_price(discount)
        if self.__money >= price:
            self.__make_deal(house, price)
        else:
            print(f"{self.name} не вистачає грошей! Потрібно {price}, а має {self.__money}.")



Human.default_info()


person = Human("Anna", 28)
person.info()


# Створення об'єкта класу SmallHouse
small_house = SmallHouse()


person.buy_house(small_house)


person.earn_money(100000)


person.buy_house(small_house)


person.info()
