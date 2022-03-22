class productos():
    def __init__(self, name, amount):

        self.name = name
        self.amount = amount
        self.old_amount = amount
    
    def get_name(self):
        return self.name
    
    
    def get_amount(self):
        return self.amount
    
    def set_amount(self, productos_vendidos):
        self.amount -= productos_vendidos
        return self.amount

    def set_old_amount(self):
        self.amount = self.old_amount
        return self.amount

class bedidas(productos):
    def __init__(self, name, amount, little_amount, middle_amount, big_amount, little_price, middle_price, big_price):
        productos.__init__(self, name, amount)

        self.little_amount = little_amount
        self.middle_amount = middle_amount
        self.big_amount = big_amount

        self.all_old_amount = little_amount

        self.little_price = little_price
        self.middle_price = middle_price
        self.big_price = big_price

    
    def get_little_amount(self):
        return self.little_amount    
    
    def set_little_amount(self, productos_vendidos):
        self.little_amount -= productos_vendidos
        return self.little_amount

    def get_middle_amount(self):
        return self.middle_amount
    
    def set_middle_amount(self, productos_vendidos):
        self.middle_amount -= productos_vendidos
        return self.middle_amount
    
    def get_big_amount(self):
        return self.big_amount
    
    def set_big_amount(self, productos_vendidos):
        self.big_amount -= productos_vendidos
        return self.big_amount
    
    def set_all_old_amount(self):
        self.little_amount = self.all_old_amount
        self.middle_amount = self.all_old_amount
        self.big_amount = self.all_old_amount
        return self.little_amount, self.middle_amount, self.big_amount
    
    def get_price(self):
        return self.little_price
    
    def get_middle_price(self):
        return self.middle_price
    
    def get_big_price(self):
        return self.big_price


class comidas(productos):
    def __init__(self, name, amount, presentation, price):
        productos.__init__(self, name, amount)

        self.presentation = presentation
        self.price = price
    
    def get_presentation(self):
        return self.presentation
    
    def get_price(self):
        return self.price