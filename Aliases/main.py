# Task 2
# Objective: Create a custom module with funcitons for string manipulation. Import the module in main.py and use the functions.

# Expected outcome: The functions from the custom module are used in main.py.

# Import the custom module
import text_utils as tu

# Use the functions from the custom module
user_name = input("Enter your name: ").lower()

reversed_name = tu.reverse_string(user_name)

alias = tu.capitalize_string(reversed_name)

print(f"Your alias is: {alias}")