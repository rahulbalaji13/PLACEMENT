def preprocess_visitors(visitors):
    """
    Preprocess the visitors array to create a prefix sum array.
    
    Args:
    visitors (list of int): The daily number of visitors to the park.
    
    Returns:
    list of int: The prefix sum array.
    """
    prefix_sum = [0] * (len(visitors) + 1)
    for i in range(1, len(visitors) + 1):
        prefix_sum[i] = prefix_sum[i - 1] + visitors[i - 1]
    return prefix_sum

def total_visitors(prefix_sum, start, end):
    """
    Calculate the total number of visitors from start to end.
    
    Args:
    prefix_sum (list of int): The prefix sum array.
    start (int): The starting index of the range.
    end (int): The ending index of the range.
    
    Returns:
    int: The total number of visitors in the range [start, end].
    """
    return prefix_sum[end + 1] - prefix_sum[start]

def main():
    try:
        # Input the visitors array
        visitors_input = input("Enter the visitors array: ").strip()
        visitors = list(map(int, visitors_input.split()))
        
        # Input the number of queries
        num_queries = int(input("Enter the number of queries: ").strip())
        
        # Preprocess visitors to create the prefix sum array
        prefix_sum = preprocess_visitors(visitors)
        
        # Handle each query
        for _ in range(num_queries):
            query_input = input("Enter query (start end): ").strip()
            start, end = map(int, query_input.split())
            if 0 <= start < len(visitors) and 0 <= end < len(visitors) and start <= end:
                result = total_visitors(prefix_sum, start, end)
                print(result)
            else:
                print("Invalid query range")
                
    except ValueError:
        print("Input is not in correct format or missing.")

if __name__ == "__main__":
    main()
