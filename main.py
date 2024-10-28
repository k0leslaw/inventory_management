class Product:
    """represents a product sold by the shop"""
    def __init__(self, brand, model, serial_number, wholesale_price, selling_price, used, color):
        self._brand = brand
        self._model = model
        self._serial_number = serial_number
        self._wholesale_price = wholesale_price
        self._selling_price = selling_price
        self._used = used  # YES or NO
        self._color = color

    def get_brand(self):
        """return product brand"""
        return self._brand

    def get_model(self):
        """return product model"""
        return self._model

    def get_serial_number(self):
        """return product serial_number"""
        return self._serial_number

    def get_wholesale_price(self):
        """return product wholesale_price"""
        return self._wholesale_price

    def get_selling_price(self):
        """return product selling_price"""
        return self._selling_price

    def get_used(self):
        """return if product is used (YES/NO)"""
        return self._used

    def get_color(self):
        """return the color the guitar comes in"""
        return self._color

    def set_selling_price(self, new_price):
        """set a new selling price"""
        self._selling_price = new_price


class Guitar(Product):
    """represents a guitar product"""
    def __init__(self, brand, model, serial_number, wholesale_price, selling_price, used, color, sound, body_shape):
        super().__init__(brand, model, serial_number, wholesale_price, selling_price, used, color)
        self._sound = sound  # ACOUSTIC or ELECTRIC
        self._body_shape = body_shape
        self._color = color

    def get_sound(self):
        """return guitar's sound (ACOUSTIC/ELECTRIC)"""
        return self._sound

    def get_body_shape(self):
        """return guitar's body shape"""
        return self._body_shape


class GuitarPedal(Product):
    """represents a guitar pedal product"""
    def __init__(self, brand, model, serial_number, wholesale_price, selling_price, used, color, effect):
        super().__init__(self, brand, model, serial_number, wholesale_price, selling_price, used, color)
        self._effect = effect

    def get_effect(self):
        """return guitar pedal effect type"""
        return self._effect

