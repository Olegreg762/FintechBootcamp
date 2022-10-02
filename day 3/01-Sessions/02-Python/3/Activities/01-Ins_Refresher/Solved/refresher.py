# -*- coding: utf-8 -*-
"""
Python refresher activity.

This script showcases basic operations in Python such as variables,
conditionals, lists, dicts, for loops, and functions.
"""

# Variables
# Creates a variable with a string "Frankfurter"
title = "Frankfurter"
years = 23
hourly_wage = 65.40
expert_status = True


# Conditionals
# Declare variables and values for evaluation
x = 1
y = 10

# Checks if one value is equal to another
if x == 1:
  print("x is equal to 1")

# Lists
# Create a list of Pokemon
print("Creating a list of Pokemon...")
pokemon = ["Pikachu", "Charizard", "Bulbasaur", "Garydos", "Dragonite", "Onyx"]
print(pokemon)

# Loop over list
# Loop through a range of numbers (0 through 4)
for x in range(5):
  print(x)

# Dicts
# Initialize a dictionary
  trading_pnl = {
      "title": "Trading Log",
      "03-18-2022": -224,
      "03-19-2022": 352,
      "03-20-2022": 252,
      "03-21-2022": 354,
      "03-22-2022": -544,
      "03-23-2022": -650,
      "03-24-2022": 56,
      "03-25-2022": 123,
      "03-26-2022": -43,
      "03-27-2022": 254,
      "03-28-2022": 325,
      "03-29-2022": -123,
      "03-30-2022": 47,
      "03-31-2022": 321,
      "04-01-2022": 123,
      "04-02-2022": 133,
      "04-03-2022": -151,
      "04-04-2022": 613,
      "04-05-2022": 232,
      "04-06-2022": -311
  }

# Traverse/access nested objects
# List of Dicts
ceo_nested_dict = [
  {
      "name": "Warren Buffet",
      "age": 88,
      "occupation": "CEO of Berkshire Hathaway"
  },
  {
      "name": "Jeff Bezos",
      "age": 55,
      "occupation": "CEO of Amazon"
  },
  {
      "name": "Harry Markowitz",
      "age": 91,
      "occupation": "Professor of Finance"
  }
]

# Define a function
# Define a main function that accepts a string argument
def main(stock_ticker):
  print(stock_ticker + " is booming right now!")

stock_ticker = "SBUX"
main(stock_ticker)
