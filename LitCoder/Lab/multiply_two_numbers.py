def get_user_input():
    """
    Function to get valid integer input from the user.
    Returns:
        int: A valid integer entered by the user.
    """
    while True:
        try:
            # Try to get integer input from the user
            return int(input("Enter a number: "))
        except ValueError:
            # Handle the case where the input is not a valid integer
            print("Invalid input. Please enter a valid integer.")


def multiply_numbers(num1, num2):
    """
    Function to multiply two numbers.
    Args:
        num1 (int): The first number.
        num2 (int): The second number.
    Returns:
        int: The product of the two numbers.
    """
    return num1 * num2


def main():
    """
    Main function to execute the multiplication process.
    Gets input from the user, multiplies the numbers, and prints the result.
    """
    print("Multiplication of Two Numbers")
    
    # Get inputs from the user
    number1 = get_user_input()
    number2 = get_user_input()
    
    # Multiply the numbers
    result = multiply_numbers(number1, number2)
    
    # Display the result
    print(f"The product of {number1} and {number2} is: {result}")


# Ensure that the main function is executed when the script runs
if __name__ == "__main__":
    main()
                                                                                                                            
