import pandas as pd
import allocation_functions as af

#import datasets
hotels = pd.read_excel("hotels.xlsx")
preferences = pd.read_excel("preferences.xlsx")
guests = pd.read_excel("guests.xlsx")

#drop first columns of all datasets
hotels = hotels.drop(hotels.columns[0], axis=1)
guests = guests.drop(guests.columns[0], axis=1)
preferences = preferences.drop(preferences.columns[0], axis=1)

# Dictionary to store the allocation DataFrames for each strategy
strategy_allocations = {
    "Random": af.random_allocation(hotels, guests, preferences),
    "Customer Preference": af.preference_allocation(hotels, guests, preferences),
    "Price-Based": af.price_allocation(hotels, guests, preferences),
    "Availability-Based": af.availability_allocation(hotels, guests, preferences)
}

# Generate reports
reports = {}
for strategy, allocation_df in strategy_allocations.items():
    reports[strategy] = af.calculate_metrics(allocation_df, hotels, preferences)

# Convert to a DataFrame for easier presentation
report_df = pd.DataFrame(reports).T #T : transpose
print(report_df)