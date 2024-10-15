def calculate_energy_production(num_homes, avg_capacity, efficiency):
    """
    Calculate total energy production from distributed residential systems.
    
    :param num_homes: Number of homes with energy production systems
    :param avg_capacity: Average capacity per home in KW
    :param efficiency: Efficiency factor (0-1)
    :return: Total daily energy production in KWH
    """
    daily_hours = 24
    total_capacity = num_homes * avg_capacity
    daily_production = total_capacity * daily_hours * efficiency
    return daily_production

# Example usage
num_homes = 2000000  # 2 million homes
avg_capacity = 10  # 10 KW per home
efficiency = 0.2  # 20% efficiency (accounting for variations in sunlight, etc.)

total_production = calculate_energy_production(num_homes, avg_capacity, efficiency)
print(f"Total daily energy production: {total_production} KWH")
print(f"Total daily energy production: {total_production / 1000000} GWH")
