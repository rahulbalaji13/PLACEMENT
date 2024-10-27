def find_combinations(stocks, target, quantities, idx, result):
    if target == 0:
        result.append(quantities.copy())
        return
    if target < 0 or idx == len(stocks):
        return

    stock_price = stocks[idx][1]
    for quantity in range(6):  # Quantity can be from 0 to 5
        if quantity * stock_price > target:
            break
        quantities[idx] = quantity
        find_combinations(stocks, target - quantity * stock_price, quantities, idx + 1, result)

def main():
    try:
        budget = int(input("Enter your maximum budget: "))
        if budget <= 0:
            print("Invalid input")
            return
    except ValueError:
        print("Invalid input")
        return

    try:
        num_stocks = int(input("Specify the number of stocks: "))
        if num_stocks <= 0:
            print("Invalid input")
            return
    except ValueError:
        print("Invalid input")
        return

    stocks = []
    for _ in range(num_stocks):
        stock_input = input("Enter stock name and price (e.g., 'StockName Price'): ").split()
        stock_name = stock_input[0]
        try:
            stock_price = int(stock_input[1])
            if stock_price <= 0:
                print("The stock prices should be at least greater than 0")
                return
            if stock_price > budget:
                print("One of the stock prices is higher than the target price")
                return
        except ValueError:
            print("Invalid input")
            return
        
        stocks.append((stock_name, stock_price))

    result = []
    find_combinations(stocks, budget, [0] * len(stocks), 0, result)

    if result:
        # Sort results by the numerical value of the combinations
        result.sort(key=lambda x: int(''.join(map(str, x))))
        for combination in result:
            print(" ".join(map(str, combination)))
        print(len(result))
    else:
        print(0)

if __name__ == "__main__":
    main()
