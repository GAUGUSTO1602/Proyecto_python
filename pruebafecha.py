import datetime
from datetime import timedelta
fecha = datetime.date(2021, 7, 22)
print(fecha)
fecha2 = fecha + timedelta(days=2)
print(fecha2)

if fecha < fecha2:
    print('funciona!')
else:
    print('no funciona :c')

