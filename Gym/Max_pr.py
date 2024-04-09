# This code calculates a person's personal record (PR) in weightlifting based 
# on the weight they can lift and the number of repetitions (reps) they can perform with that weight.

# Define a function to calculate the PR
def calculate_pr(weight, reps):
  # Check if the weight and reps are valid
  if weight <= 0 or reps <= 0:
    print("Error: The weight and reps must be greater than 0.")
    return None

  # Calculate the PR using the Epley formula
  pr = weight * (35 / (37 - reps))

  return pr

# Prompt the user to input the weight
while True:
  weight_str = input("Please input the weight in kilos:")
  
  # Check if the weight is a valid number
  try:
    weight = float(weight_str)
    break  # Exit the loop if the weight is valid
  except ValueError:
    print("Error: The weight must be a numeric value.")

# Prompt the user to input the number of reps
while True:
  reps_str = input(f"Please input the amount of reps you can achieve with a weight of {weight}kg:")
  
  # Check if the reps are a valid number
  try:
    reps = int(reps_str)
    break  # Exit the loop if the reps are valid
  except ValueError:
    print("Error: The reps must be a whole number.")

# Calculate the PR
pr = calculate_pr(weight, reps)

# Print the calculated PR to the console
if pr is not None:
  print(f'Your max pr should be around {pr}kg')