import os.path

from estimate_price import estimate_price


def main():
    mileage = int(input("Please enter the mileage of the car: "))
    # if os.path.exists("values.txt"):
    #     with open("values.txt", "r") as file:
    # else:
    theta0 = 0
    theta1 = 0

    print("The estimated price of the car is:", estimate_price(mileage, theta0, theta1))


if __name__ == '__main__':
    main()
