def main():
    print("Welcome to the Mersenne Prime calculator")
    number = int(input("Please give a number: \n"))
    aux = 0
    result = 1
    base = 2

    while aux < number:
        result *= base
        aux += 1

    result -= 1 #To convert the result in Mersenne number
    print("The number of Mersenne is:", result)

    number_to_verify = result
    aux = number_to_verify - 1
    cont = 0

    if number_to_verify == 1:
        print("The number", number_to_verify, "is not Mersenne prime")
    else:
        while aux > 1:
            if number_to_verify % aux == 0:
                cont+=1
            aux -=1

        if cont == 0:
            print("The number", number_to_verify, "is Mersenne prime")
        else:
            print("The number", number_to_verify, "is Mersenne not prime")
    

if __name__ == "__main__":
    main()