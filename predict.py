import os.path
import sys

from estimate_price import estimate_price


def main():
    mileage = int(input("Please enter the mileage of the car: "))
    if os.path.exists("values.txt"):
        with open("values.txt", "r") as file:
            theta0 = float(file.readline().strip())
            theta1 = float(file.readline().strip())
            print("theta0:", theta0, file=sys.stderr, flush=True)
            print("theta1:", theta1, file=sys.stderr, flush=True)
    else:
        theta0 = 0.0
        theta1 = 0.0

    print("The estimated price of the car is:", round(estimate_price(mileage, theta0, theta1), 2), "euros.")


if __name__ == '__main__':
    main()
