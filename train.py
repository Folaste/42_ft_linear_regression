import os.path

from estimate_price import estimate_price


def mean_squared_error(mileage, price, theta0, theta1):
    error_sum = 0
    for i in range(len(mileage)):
        error_sum += (estimate_price(mileage[i], theta0, theta1) - price[i]) ** 2
    return error_sum / (2 * len(mileage))


def gradient_descent(mileage, price, theta0, theta1, learning_rate):
    pass


def main():
    pass


if __name__ == '__main__':
    main()
