class Guitar:
    def __init__(self, serial_number, price, builder, model, type, back_wood, top_wood):
        self.__serial_number= str(serial_number)
        self.__price = float(price)
        self.__builder = str(builder)
        self.__model = str(model)
        self.__type = str(type)
        self.__back_wood = str(back_wood)
        self.__top_wood = str(top_wood)

    @property
    def serial_number(self):
        return self.__serial_number

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        if not isinstance(new_price, float):
            raise TypeError("Price must be a number.")
        else:
            self.__price = price

    @property
    def builder(self):
        return self.__builder

    @property
    def model(self):
        return self.__model

    @property
    def type(self):
        return self.__type

    @property
    def back_wood(self):
        return self.__back_wood

    @property
    def top_wood(self):
        return self.__top_wood
