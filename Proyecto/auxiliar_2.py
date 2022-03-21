class sillas():
    def __init__(self, total):

        self.total = total
    
    def get_total(self):
        return self.total
    
    def set_total(self, resta):
        self.total -= resta
        return self.total

total = 10
silla = sillas(total)
print(silla.get_total())

quitar = 4

silla.set_total(quitar)

print(silla.get_total())