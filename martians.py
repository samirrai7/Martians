import random

# Initialize the cargo weights and their locations
weights = [300, 250, 163]
locations = [random.randint(1, 10) for _ in range(3)]

print("Welcome to the Martian Cargo Recovery Program!")
print("Your task is to find the locations of the 3 cargo boxes.")
print("Each time you guess wrong, the boxes relocate!")

while True:
    # Prompt the user for guesses
    guesses = []
    for i in range(3):
        guess = int(input(f"Enter your guess for box {i + 1} (1-10): "))
        guesses.append(guess)
    
    # Check if all guesses are correct
    if guesses == locations:
        print("Congratulations! You found all the cargo boxes!")
        print(f"Total weight recovered: {sum(weights)} kg")
        break
    else:
        print("Oops! Wrong guesses. The boxes have relocated.")
        # Randomize the locations again
        locations = [random.randint(1, 10) for _ in range(3)]
