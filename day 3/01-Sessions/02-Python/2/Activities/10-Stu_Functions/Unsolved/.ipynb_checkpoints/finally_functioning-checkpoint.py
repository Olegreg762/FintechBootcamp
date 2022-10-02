"""
Determine the Compound Annual Growth Rate for an investment
"""

# Declare a variable beginning_balance as a float
beginning_balance = 29000.00

# Declare a variable ending_balance as float
ending_balance = 45000.10

# Declare a variable years as an float
years = 1.0

# Define a function called calculate_compound_growth_rate with three arguments: beginning_balance, ending_balance, years. Function should output growth_rate.
def calculate_compound_growth_rate(beginning_balance,ending_balance,years) :
    growth_rate = ((ending_balance / beginning_balance)**(1/years) - 1)*100
    return growth_rate

# Call calculate_compound_growth_rate using beginning_balance, ending_balance, and years. Capture as year_one_growth.
year_one_growth = calculate_compound_growth_rate(beginning_balance,ending_balance,years)

# Update beginning_balance and ending balance for year two, and then execute calculate_compound_growth_rate
beginning_balance =  45000.10
ending_balance = 47000.00

# Call calculate_compound_growth_rate using beginning_balance, ending_balance, and years. Capture as year_two_growth.
year_two_growth = calculate_compound_growth_rate(beginning_balance,ending_balance,years)

# Update beginning_balance and ending balance for year three, and then execute calculate_compound_growth_rate
beginning_balance = 47000.00
ending_balance = 60930.00
year_three_growth = calculate_compound_growth_rate(beginning_balance,ending_balance,years)


# Call calculate_compound_growth_rate using beginning_balance, ending_balance, and years. Capture as year_three_growth.


# Use Python round() function to round year_one_growth, year_two_growth, and year_three_growth. Capture these as new variables.
year_one_growth_rnd = round(year_one_growth,2)
year_two_growth_rnd = round(year_two_growth,2)
year_three_growth_rnd = round(year_three_growth,2)

# Print year_one_growth, year_two_growth, year_three_growth as percents using string formatting
print(f"Compound Annual Growth Rate for 2016: {year_one_growth_rnd}%")
print(f"Compound Annual Growth Rate for 2017: {year_two_growth_rnd}%")
print(f"Compound Annual Growth Rate for 2018: {year_three_growth_rnd}%")

# Challenge

# Create a global, empty list


# Define a function called


    # Populate growth_rates list using add() function

