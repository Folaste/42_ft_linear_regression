import os.path
import sys

import numpy as np

from estimate_price import estimate_price
from matplotlib import pyplot as plt


def normalize_data(mileage, price):
    max_mileage = max(mileage)
    max_price = max(price)
    min_mileage = min(mileage)
    min_price = min(price)
    normalized_mileage = [(mileage[i] - min_mileage) / (max_mileage - min_mileage) for i in range(len(mileage))]
    normalized_price = [(price[i] - min_price) / (max_price - min_price) for i in range(len(price))]
    return normalized_mileage, normalized_price


def mean_squared_error(mileage, price, theta0, theta1):
    error_sum = 0
    for i in range(len(mileage)):
        error_sum += (estimate_price(mileage[i], theta0, theta1) - price[i]) ** 2
    return error_sum / (2 * len(mileage))


def gradient_descent(mileage, price, theta0, theta1):
    learning_rate = 0.1
    sum_theta0 = 0
    sum_theta1 = 0
    for i in range(len(mileage)):
        sum_theta0 += estimate_price(mileage[i], theta0, theta1) - price[i]
        sum_theta1 += (estimate_price(mileage[i], theta0, theta1) - price[i]) * mileage[i]
    new_theta0 = theta0 - (learning_rate * sum_theta0) / len(mileage)
    new_theta1 = theta1 - (learning_rate * sum_theta1) / len(mileage)
    return new_theta0, new_theta1


def main():
    mileage = []
    price = []
    if os.path.exists("data.csv"):
        with open("data.csv", "r") as file:
            file.readline()
            for line in file:
                data = line.split(",")
                mileage.append(int(data[0]))
                price.append(int(data[1]))

    print("mileage", mileage, file=sys.stderr, flush=True)
    print("price", price, file=sys.stderr, flush=True)
    normalized_mileage, normalized_price = normalize_data(mileage, price)
    print("normalized_mileage", normalized_mileage, file=sys.stderr, flush=True)
    print("normalized_price", normalized_price, file=sys.stderr, flush=True)
    theta0 = 1
    theta1 = 1
    for i in range(1000):
        theta0, theta1 = gradient_descent(normalized_mileage, normalized_price, theta0, theta1)
        print(mean_squared_error(normalized_mileage, normalized_price, theta0, theta1), file=sys.stderr, flush=True)
    print("theta0", theta0, file=sys.stderr, flush=True)
    print("theta1", theta1, file=sys.stderr, flush=True)

    plt.scatter(normalized_mileage, normalized_price)
    plt.plot(normalized_mileage, [estimate_price(normalized_mileage[i], theta0, theta1) for i in range(len(mileage))], color='red')
    plt.show()


if __name__ == '__main__':
    main()
