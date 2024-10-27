def encrypt_data(number):
    # Check if input is a valid integer
    if not number.isdigit():
        print("Enter only integer value")
        return

    # Convert the input to an integer
    number = int(number)

    # Check if input is positive
    if number <= 0:
        print("Enter positive 4-digit integer")
        return

    # Convert integer to string to check its length
    num_str = str(number)

    # Check if input is exactly 4 digits long
    if len(num_str) < 4:
        print("Provided input is less than 4, enter four digit integers")
        return
    elif len(num_str) > 4:
        print("Provided input is more than 4, enter four digit integers")
        return

    # Convert string to list of digits
    digits = [int(digit) for digit in num_str]

    # Encrypt each digit by adding 5 and taking remainder modulo 10
    encrypted_digits = [(digit + 5) % 10 for digit in digits]

    # Swap first and third digits, and second and fourth digits
    encrypted_digits[0], encrypted_digits[2] = encrypted_digits[2], encrypted_digits[0]
    encrypted_digits[1], encrypted_digits[3] = encrypted_digits[3], encrypted_digits[1]

    # Convert the list of digits back to an integer
    encrypted_number = int(''.join(map(str, encrypted_digits)))

    # Output the encrypted integer
    print(encrypted_number)

# Accept input from the user
user_input = input("Enter a 4-digit integer: ")
encrypt_data(user_input)
                                                                                                                            
