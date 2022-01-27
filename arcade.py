print('Welcome to Kiwami Arcade!')
age = input('Please, give your age\n-->')
if age.isnumeric() == True:
    age = int(age)
    if age < 4:
        print('You can enter without pay!')
    elif 4 <= age <=18:
        print('You must pay $5 to enter')
    else:
        print('You must pay $10 to enter')
else:
    print('The information is not valid')