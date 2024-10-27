def page_turns(n, p):
    """
    Calculate the minimum number of page turns required to reach page p 
    from either the front or the back of a book with n pages.
    
    Args:
    n (int): Total number of pages in the book.
    p (int): The target page the student wants to reach.

    Returns:
    int: Minimum number of page turns.
    """
    # Calculate turns from the front
    front_turns = p // 2

    # Calculate turns from the back
    if n % 2 == 0:
        back_turns = (n - p + 1) // 2
    else:
        back_turns = (n - p) // 2

    # Return the minimum of the two
    return min(front_turns, back_turns)

# Example usage
if __name__ == "__main__":
    n = int(input("Enter the total number of pages (n): "))
    p = int(input("Enter the target page (p): "))

    # Ensure valid input
    if 1 <= n <= 1000 and 1 <= p <= n:
        result = page_turns(n, p)
        print(result)
    else:
        print("Invalid input. Please ensure 1 <= n <= 1000 and 1 <= p <= n.")
