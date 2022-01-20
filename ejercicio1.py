def main():
    print("Welcome to the exponential calculator")
    number = int(input("Please give a number: \n"))
    aux = 0
    result = 1

    while aux < number:
        result *= 2
        aux += 1

    print("The result is:", result)
    

if __name__ == "__main__":
    main()