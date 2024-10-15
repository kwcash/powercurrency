import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def model_adoption_rate(t, k, x0):
    """
    Model the adoption rate of Power Currency over time using a sigmoid function.
    
    :param t: Time in years since introduction
    :param k: Steepness of the curve
    :param x0: Midpoint of the sigmoid
    :return: Adoption rate (0-1)
    """
    return sigmoid(k * (t - x0))

# Example usage
years = np.arange(0, 20)
adoption_rates = model_adoption_rate(years, 0.5, 10)

for year, rate in zip(years, adoption_rates):
    print(f"Year {year}: {rate:.2%} adoption")
