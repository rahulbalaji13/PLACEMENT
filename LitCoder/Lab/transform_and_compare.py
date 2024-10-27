def can_transform(start: str, end: str) -> bool:
    """
    Determine if the starting string can be transformed into the ending string by a sequence of valid moves.
    A move consists of replacing either "XL" with "LX" or "RX" with "XR".

    Args:
    start (str): The starting string.
    end (str): The target ending string.

    Returns:
    bool: True if the transformation is possible, False otherwise.
    """
    # If the lengths of the strings are not equal, transformation is impossible
    if len(start) != len(end):
        return False

    # Remove all 'X' characters and compare the remaining strings
    # They must match in terms of order of 'L' and 'R' characters
    if start.replace('X', '') != end.replace('X', ''):
        return False

    # Check the positions of 'L' and 'R' after removing 'X' characters
    # 'L' can only move to the left and 'R' can only move to the right.
    L_positions_start = [i for i, c in enumerate(start) if c == 'L']
    L_positions_end = [i for i, c in enumerate(end) if c == 'L']
    R_positions_start = [i for i, c in enumerate(start) if c == 'R']
    R_positions_end = [i for i, c in enumerate(end) if c == 'R']

    # Ensure that each 'L' in the start string is not to the right of where it is in the end string
    for i, j in zip(L_positions_start, L_positions_end):
        if i < j:
            return False

    # Ensure that each 'R' in the start string is not to the left of where it is in the end string
    for i, j in zip(R_positions_start, R_positions_end):
        if i > j:
            return False

    return True


# Input from the user
if __name__ == "__main__":
    start = input("Enter the starting string: ")
    end = input("Enter the ending string: ")
    
    result = can_transform(start, end)
    
    if result:
        print("true")
    else:
        print("false")
                                                                                                                            
