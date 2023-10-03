class Productos(): #Clase productos
    def __init__(self, name, amount, amount_sell):

        self.name = name
        self.amount = amount
        self.old_amount = amount #Guardar la cantidad total original
        self.amount_sell = amount_sell #Guardar cuantas existencias se han vendido
    
    def get_name(self):
        return self.name
    
    def get_amount(self):
        return self.amount
    
    def set_amount(self, productos_vendidos):
        self.amount -= productos_vendidos
        return self.amount

    def set_old_amount(self): #Reestaurar la cantidad incial de existencias
        self.amount = self.old_amount
        return self.amount
    
    def get_amount_sell(self):
        return self.amount_sell
    
    def set_amount_sell(self, sales):
        self.amount_sell += sales
        return self.amount_sell

class Bedidas(Productos):
    def __init__(self, name, amount, little_amount, middle_amount, big_amount, little_price, middle_price, big_price, amount_sell):
        Productos.__init__(self, name, amount, amount_sell)

        self.little_amount = little_amount #Cantidades de acuerdo al tamaño de la bebida
        self.middle_amount = middle_amount
        self.big_amount = big_amount

        self.all_old_amount = little_amount

        self.little_price = little_price #Precios de acuerdo al precio de las bebidas segun el tamaño
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
        self.little_amount = self.all_old_amount #Reestaurar las cantidades de todos los tamaños de bebidas
        self.middle_amount = self.all_old_amount
        self.big_amount = self.all_old_amount
        return self.little_amount, self.middle_amount, self.big_amount
    
    def get_price(self):
        return self.little_price
    
    def get_middle_price(self):
        return self.middle_price
    
    def get_big_price(self):
        return self.big_price


class Comidas(Productos):
    def __init__(self, name, amount, presentation, price, amount_sell):
        Productos.__init__(self, name, amount, amount_sell)

        self.presentation = presentation
        self.price = price
    
    def get_presentation(self):
        return self.presentation
    
    def get_price(self):
        return self.price