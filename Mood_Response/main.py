# Task 1
#Objective: Create a Python program using a custom module that asks the user for their mood and then returns a response based on their mood.

# Import the custom module mood_responses
import mood_responses

# Ask the user for their mood
mood = input("How are you feeling today? ")

# Get the response based on the user's mood
response = mood_responses.mood_response(mood)

# Print the response
print(response)