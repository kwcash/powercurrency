def calculate_currency_issuance(energy_production, issuance_rate):
    """
    Calculate the amount of Power Currency to issue based on energy production.
    
    :param energy_production: Daily energy production in KWH
    :param issuance_rate: Percentage of energy production to issue as currency
    :return: Amount of currency to issue (in KWH equivalent)
    """
    return energy_production * issuance_rate

# Example usage
daily_production = 96000000  # 96 GWH (from previous example)
issuance_rate = 0.1  # Issue currency equivalent to 10% of production

currency_to_issue = calculate_currency_issuance(daily_production, issuance_rate)
print(f"Daily currency issuance: {currency_to_issue} KWH equivalent")
print(f"Daily currency issuance: {currency_to_issue / 1000} MWH equivalent")
