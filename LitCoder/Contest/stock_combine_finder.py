def get_stock_combinations(prices, target, max_quantity=5):
    combinations = []

    def find_combinations(current_combination, current_sum, index):
        if current_sum == target:
            combinations.append(current_combination[:])
            return
        if current_sum > target or index >= len(prices):
            return
        
        for quantity in range(0, max_quantity + 1):
            current_combination[index] = quantity
            find_combinations(current_combination, current_sum + prices[index] * quantity, index + 1)

    find_combinations([0] * len(prices), 0, 0)
    return combinations


def main():
    try:
        # Get the maximum budget
        budget = int(input("Enter your maximum budget: "))
        if budget <= 0:
            print("Invalid input")
            return
        
        # Get the number of stocks
        num_stocks = int(input("Specify the number of stocks: "))
        
        prices = []
        stock_names = []
        
        # Get each stock's name and price
        for _ in range(num_stocks):
            stock_input = input("Enter stock name and price (separated by space): ").strip().split()
            if len(stock_input) != 2:
                print("Invalid input")
                return
            
            stock_name = stock_input[0]
            try:
                price = int(stock_input[1])
            except ValueError:
                print("Invalid input")
                return
            
            if price <= 0:
                print("The stock prices should be at least greater than 0")
                return
            
            if price > budget:
                print("One of the stock prices is higher than the target price")
                return
            
            stock_names.append(stock_name)
            prices.append(price)

        # Find all valid combinations
        combinations = get_stock_combinations(prices, budget)

        # Sort combinations in ascending order
        combinations.sort()

        # Output the combinations
        for combo in combinations:
            print(' '.join(map(str, combo)))

        # Output the count of combinations
        print(len(combinations))

    except ValueError:
        print("Invalid input")


if __name__ == "__main__":
    main()
