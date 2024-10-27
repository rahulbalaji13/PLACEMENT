# Function to find common elements in three sorted arrays
def find_common_elements(arr1, arr2, arr3):
    # Converting arrays to sets and finding intersection
    common_elements = set(arr1) & set(arr2) & set(arr3)

    # If there are common elements, sort them and print
    if common_elements:
        print(' '.join(map(str, sorted(common_elements))))
    else:
        print("No Elements")

# Input function to get arrays from user
def get_input():
    # Taking input for the arrays
    arr1 = list(map(int, input("Enter elements of first array (space-separated): ").split()))
    arr2 = list(map(int, input("Enter elements of second array (space-separated): ").split()))
    arr3 = list(map(int, input("Enter elements of third array (space-separated): ").split()))

    # Call function to find common elements
    find_common_elements(arr1, arr2, arr3)

# Driver function
if __name__ == "__main__":
    get_input()
                                                                                                                            
