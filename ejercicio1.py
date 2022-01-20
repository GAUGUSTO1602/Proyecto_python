def main():
    print("Welcome to the exponential calculator")
    number = int(input("Please give a number: \n"))
    aux = 1
    base = 2

    while aux < number:
        base *= 2
        aux += 1

    if number == 0:
        print("The result is: 1")
    else:
        print("The result is:", base)
    

if __name__ == "__main__":
    main()