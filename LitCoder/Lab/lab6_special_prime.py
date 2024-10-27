import math

def is_prime(n):
    """
    Check if a number is prime.

    Args:
    n (int): The number to check for primality.

    Returns:
    bool: True if n is a prime number, False otherwise.
    """
    if n <= 1:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(5, int(math.sqrt(n)) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True

def is_special_prime(num):
    """
    Check if a number is a special prime. A special prime must satisfy that:
    - The number itself is prime.
    - All the prefixes of its digits are prime (i.e., each time you add a new digit from left to right).

    Args:
    num (int): The number to check if it's a special prime.

    Returns:
    bool: True if num is a special prime, False otherwise.
    """
    str_num = str(num)
    
    for i in range(1, len(str_num) + 1):
        if not is_prime(int(str_num[:i])):
            return False
    return True

def find_largest_special_prime(limit):
    """
    Find the largest special prime less than a given limit.

    Args:
    limit (int): The upper limit (exclusive) for searching the special prime.

    Returns:
    int: The largest special prime less than limit, or -1 if none is found.
    """
    for num in range(limit - 1, 1, -1):
        if is_prime(num) and is_special_prime(num):
            return num
    return -1

if __name__ == "__main__":
    """
    Main module to take user input and find the largest special prime.
    """
    user_input = int(input("Enter the upper limit: "))
    result = find_largest_special_prime(user_input)
    print(f"The largest special prime less than {user_input} is: {result}")
                                                                                                                            
