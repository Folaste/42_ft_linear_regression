import os.path
import sys

from matplotlib import pyplot as plt

from estimate_price import estimate_price


def normalize_data(mileage, price):
    max_mileage = max(mileage)
    max_price = max(price)
    min_mileage = min(mileage)
    min_price = min(price)
    normalized_mileage = [(mileage[i] - min_mileage) / (max_mileage - min_mileage) for i in range(len(mileage))]
    normalized_price = [(price[i] - min_price) / (max_price - min_price) for i in range(len(price))]
    return normalized_mileage, normalized_price


def denormalize_data(normalized_mileage, normalized_price, mileage, price):
    max_mileage = max(mileage)
    max_price = max(price)
    min_mileage = min(mileage)
    min_price = min(price)
    denormalized_mileage = [normalized_mileage[i] * (max_mileage - min_mileage) + min_mileage for i in
                            range(len(mileage))]
    denormalized_price = [normalized_price[i] * (max_price - min_price) + min_price for i in range(len(price))]
    return denormalized_mileage, denormalized_price


def mean_squared_error(mileage, price, theta0, theta1):
    error_sum = 0
    for i in range(len(mileage)):
        error_sum += (estimate_price(mileage[i], theta0, theta1) - price[i]) ** 2
    return error_sum / (2 * len(mileage))


def gradient_descent(mileage, price, theta0, theta1):
    learning_rate = 0.048
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

    # print("mileage", mileage, file=sys.stderr, flush=True)
    # print("price", price, file=sys.stderr, flush=True)

    normalized_mileage, normalized_price = normalize_data(mileage, price)
    # print("normalized_mileage", normalized_mileage, file=sys.stderr, flush=True)
    # print("normalized_price", normalized_price, file=sys.stderr, flush=True)

    theta0 = 0
    theta1 = 0

    iterations = 1000
    error = []
    for i in range(iterations):
        theta0, theta1 = gradient_descent(normalized_mileage, normalized_price, theta0, theta1)
        error.append(mean_squared_error(normalized_mileage, normalized_price, theta0, theta1))
        # print(mean_squared_error(normalized_mileage, normalized_price, theta0, theta1), file=sys.stderr, flush=True)
    print("theta0 normalized:", theta0, file=sys.stderr, flush=True)
    print("theta1 normalized:", theta1, file=sys.stderr, flush=True)

    # Denormalize theta0 and theta1
    max_mileage = max(mileage)
    max_price = max(price)
    min_mileage = min(mileage)
    min_price = min(price)
    theta1_dn = theta1 * (max_price - min_price) / (max_mileage - min_mileage)
    theta0_dn = min_price + theta0 * (max_price - min_price) - theta1_dn * min_mileage

    print("theta0 denormalized:", theta0_dn, file=sys.stderr, flush=True)
    print("theta1 denormalized:", theta1_dn, file=sys.stderr, flush=True)

    mileage_dn, price_dn = denormalize_data(normalized_mileage, normalized_price, mileage, price)
    print(mileage_dn, file=sys.stderr, flush=True)
    print(price_dn, file=sys.stderr, flush=True)

    plt.subplot(2, 2, 1)
    plt.scatter(mileage, price)

    plt.subplot(2, 2, 2)
    plt.scatter(normalized_mileage, normalized_price)
    plt.plot(normalized_mileage, [estimate_price(normalized_mileage[i], theta0, theta1)
                                  for i in range(len(mileage))], color='red')
    plt.title("Normalized data")

    plt.subplot(2, 2, 3)
    plt.scatter(mileage_dn, price_dn)
    plt.plot(mileage_dn, [estimate_price(mileage_dn[i], theta0_dn, theta1_dn)
                          for i in range(len(mileage))], color='red')
    plt.title("Denormalized data")

    plt.subplot(2, 2, 4)
    plt.plot(range(iterations), error)
    plt.title("Mean squared error")
    plt.ylabel("Error")
    plt.xlabel("Iteration")

    plt.tight_layout()
    plt.show()

    with open("values.txt", "w") as file:
        file.write(f"{theta0_dn}\n{theta1_dn}")


if __name__ == '__main__':
    main()
