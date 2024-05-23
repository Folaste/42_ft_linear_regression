import os.path


def main():
    mileage = int(input("Please enter the mileage of the car: "))
    # if os.path.exists("values.txt"):
    #     with open("values.txt", "r") as file:
    # else:
    theta0 = 0
    theta1 = 0

    print("The estimated price of the car is: ", theta0 + theta1 * mileage)


if __name__ == '__main__':
    main()
