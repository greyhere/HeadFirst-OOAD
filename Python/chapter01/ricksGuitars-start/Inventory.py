from Guitar import Guitar


class Inventory:
    def __init__(self):
        self.__guitars = []

    def add_guitar(self, serial_number, price, builder, model, type, back_wood, top_wood):
        guitar = Guitar(serial_number, price, builder, model, type, back_wood, top_wood)
        self.__guitars.append(guitar)

    def get_guitar(self, serial_number):
        for guitar in self.__guitars:
            if guitar.serial_number == serial_number:
                return guitar
        return None

    def search(self, search_guitar):
        for guitar in self.__guitars:
            # Ignore serial number since that's unique
            # Ignore price since that's unique
            builder = search_guitar.builder
            if (builder != None) and (builder != "") and (builder != guitar.builder):
                continue
            model = search_guitar.model
            if (model != None) and (model != "") and (model != guitar.model):
                continue
            type = search_guitar.type
            if (type != None) and (model != "") and (type != guitar.type):
                continue
            back_wood = search_guitar.back_wood
            if (back_wood != None) and (back_wood != "") and (back_wood != guitar.back_wood):
                continue
            top_wood = search_guitar.top_wood
            if (top_wood != None) and (top_wood != "") and (top_wood != guitar.top_wood):
                continue
            return guitar
        return None
