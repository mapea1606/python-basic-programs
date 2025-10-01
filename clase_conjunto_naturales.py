import sys

# Class to represent a set of the first 100 natural numbers
# and find a missing number.
class PrimerosCienNaturales:
    # Initializes the set with numbers from 1 to 100.
    def __init__(self):
        self.numbers = list(range(1, 101))

    # Extracts a number from the set if it exists and is valid.
    def extract(self, number_to_remove: int):
        # Validates that the number to extract is an integer between 1 and 100.
        if not isinstance(number_to_remove, int) or not (1 <= number_to_remove <= 100):
            raise ValueError("The number to extract must be an integer between 1 and 100.")
        
        try:
            self.numbers.remove(number_to_remove)
            print(f"The number {number_to_remove} has been extracted successfully.")
        except ValueError:
            print(f"The number {number_to_remove} is not found in the original list.")

    # Calculates and returns the number missing from the set.
    def find_missing(self) -> int:
        # Gauss sum for the first 100 natural numbers.
        expected_sum = 100 * (100 + 1) // 2
        
        # Sum of the numbers in the modified list.
        actual_sum = sum(self.numbers)
        
        missing_number = expected_sum - actual_sum
        return missing_number

# The program starts its execution here
print("Missing number calculator for a set of 100.")
print("The program will keep asking for a number until a valid value is entered.")

while True:
    try:
        user_input = input("Enter the number to extract (from 1 to 100): ")
        
        # Converts the input to an integer
        number_to_extract = int(user_input)
        
        # Instantiates the class
        finder = PrimerosCienNaturales()
        
        # Extracts the number and validates the input
        finder.extract(number_to_extract)
        
        # Calculates the missing number
