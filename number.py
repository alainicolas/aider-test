import random

def generate_random_number():
  """Generates a random number between 1 and 12."""

  random_number = random.randint(1, 12)
  print(f"Your random number is: {random_number}")

if __name__ == "__main__":
  generate_random_number()
