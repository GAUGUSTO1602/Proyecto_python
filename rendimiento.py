employee = input('Please give the name of the employee\n--> ')
score = input('What was his/her score this year?\n--> ')
score = float(score)
if score == 0.0:
    remuneration = 2400 * score
    print('The performance of', employee, 'was unnaceptable')
    print('His/Her remuneration shall be:', remuneration, end='$')
elif score == 0.4:        
    remuneration = 2400 * score
    print('The performance of', employee, 'was aceptable')
    print('His/Her remuneration shall be:', remuneration, end='$')
elif score >= 0.6:
    remuneration = 2400 * score
    print('The performance of', employee, 'was meritorius')
    print('His/Her remuneration shall be:',remuneration , end='$')
else:
    print('The information is not valid') 
