def main():

    num = input('Dame un numero: ')
    num = int(num)
    flag = False
    for x in range(2, num):
        if num % x == 0:
            flag = True
            break
    if flag == True:
        print('No es primo')
    else:
        print('Es primo')

main()