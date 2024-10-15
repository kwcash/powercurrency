def calculate_economic_impact(energy_production, job_factor, local_multiplier):
    """
    Calculate the economic impact of Power Currency implementation.
    
    :param energy_production: Annual energy production in MWH
    :param job_factor: Jobs created per MWH of energy production
    :param local_multiplier: Local economic multiplier effect
    :return: Dictionary with job creation and economic impact
    """
    jobs_created = energy_production * job_factor
    direct_economic_impact = energy_production * 100  # Assume $100 per MWH
    total_economic_impact = direct_economic_impact * local_multiplier
    
    return {
        "jobs_created": jobs_created,
        "direct_economic_impact": direct_economic_impact,
        "total_economic_impact": total_economic_impact
    }

# Example usage
annual_production = 35040000  # 35,040 GWH (96 GWH * 365 days)
job_factor = 0.0001  # 1 job per 10 GWH of annual production
local_multiplier = 1.5  # Each dollar of direct impact generates $0.50 in additional local economic activity

impact = calculate_economic_impact(annual_production, job_factor, local_multiplier)
print(f"Jobs created: {impact['jobs_created']}")
print(f"Direct economic impact: ${impact['direct_economic_impact']:,}")
print(f"Total economic impact: ${impact['total_economic_impact']:,}")
