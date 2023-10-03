class Evento(): #Clase eventos
    def __init__(self, title, tipo, cartel, asientos, date, ingresos, apertura):

        self.title = title
        self.tipo = tipo
        self.cartel = cartel
        self.asientos = asientos
        self.date = date
        self.ingresos = ingresos
        self.apertura = apertura

    def get_title(self):
        return self.title
    
    def get_tipo(self):
        return self.tipo
    
    def get_cartel(self):
        return self.cartel
    
    def get_asientos(self):
        return self.asientos
    
    def get_date(self):
        return self.date
    
    def get_ingresos(self):
        return self.ingresos
    
    def set_ingresos(self, nuevos_ingresos):
        self.ingresos += nuevos_ingresos
        return self.ingresos
    
    def get_apertura(self):
        return self.apertura
    
    def set_apertura(self, opt_apertura): #Funcion para cerrar o abrir el evento
        self.apertura = opt_apertura
        return self.apertura

class Musical(Evento):
    def __init__(self, title, tipo, cartel, asientos, date, ingresos, apertura, bands):
        Evento.__init__(self, title, tipo, cartel, asientos, date, ingresos, apertura)

        self.bands = bands

    def get_bands(self):
        return self.bands
    


class Teatral(Evento):
    def __init__(self, title, tipo, cartel, asientos, date, ingresos, apertura, synopsis):
        Evento.__init__(self, title, tipo, cartel, asientos, date, ingresos, apertura)

        self.sypnosis = synopsis

    def get_synopsis(self):
        return self.sypnosis