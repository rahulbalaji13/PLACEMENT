def single_digit_sum(n):
    """Calculate the cumulative sum of the digits of n until a single digit is obtained."""
    while n >= 10:
        n = sum(int(digit) for digit in str(n))
    return n

def replace_odds_with_letters(n):
    """Replace odd digits with corresponding letters, where 1=a, 3=c, etc."""
    if n % 2 == 1:  # Check if the number is odd
        return chr(n + 96)  # Convert to corresponding lowercase letter
    return str(n)  # Return the digit as string if it's even

def generate_pin(arr):
    """Generate a six-digit PIN based on the rules provided."""
    pin = ""
    
    for number in arr:
        digit_sum = single_digit_sum(number)  # Get single-digit sum
        pin += replace_odds_with_letters(digit_sum)  # Replace odds and build the PIN

    return pin

# Accepting input from the user
user_input = input("Enter space-separated numbers: ")
# Convert the input string into a list of integers
input_data = list(map(int, user_input.split()))

# Generate and display the output PIN
output = generate_pin(input_data)
print("Generated PIN:", output)
                                                                                                                            
