import datetime
from datetime import timedelta
fecha = datetime.date(2020, 4, 10)
fecha1 = datetime.date(2020, 4, 10)
fecha2 = datetime.date(2020, 4, 11)
fecha3= datetime.date(2020, 4, 17)
fecha4 = datetime.date(2020, 4, 30)
fecha_final = datetime.date(2020, 5, 2)
Saldo_Inicial = int(3480)

while fecha < fecha_final:
    if fecha == fecha1:
      print(fecha,': El saldo disponible es de $',Saldo_Inicial, sep='',end='\n') 
    elif fecha == fecha2:
      print('Se han retirado $96')
      Saldo_restante = Saldo_Inicial - int(96)
      print('Saldo actual a la fecha ',fecha,': $',Saldo_restante, sep='', end='\n')
    elif fecha == fecha3:
      print('Se ha transferido a la cuenta $1200', end='\n')
      Saldo_restante = Saldo_restante + int(1200)
      print('Saldo actual a la fecha ',fecha,': $',Saldo_restante, sep='', end='\n')
    elif fecha == fecha4:
      print('Se ha abonado a su cuenta un 3% de intereses', end='\n')
      Intereses = float(3)
      Saldo =  float(Saldo_restante)
      Saldo_restante = Intereses * Saldo / 100 + Saldo_restante
      Saldo_restante = round(Saldo_restante, 2)
      print('Saldo actual a la fecha ',fecha,': $',Saldo_restante, sep='', end='\n')
    fecha = fecha + timedelta(days=1)

if fecha == fecha_final:
  print('Se han retirado $51')
  Saldo_restante = Saldo_restante - int(51)
  print('Saldo actual a la fecha ',fecha,': $',Saldo_restante, sep='')
