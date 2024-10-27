def peopleAwareOfSecret(n, delay, forget):
    # Array to keep track of how many new people discover the secret each day
    dp = [0] * (n + 1)
    
    # The first person discovers the secret on day 1
    dp[1] = 1

    for day in range(1, n + 1):
        if dp[day] > 0:
            # Calculate the day when the new person will start sharing the secret
            share_day = day + delay
            # Calculate the day when the person forgets the secret
            forget_day = day + forget
            
            # Only add the new person if the share_day is within bounds
            if share_day <= n:
                dp[share_day] += dp[day]
            # Subtract the forgotten people from the total from the forget_day onwards
            if forget_day <= n:
                dp[forget_day] -= dp[day]

    # Total people who know the secret at the end of day n
    total_people = 0
    for day in range(1, n + 1):
        total_people += dp[day]

    return total_people

# Accepting user input
if __name__ == "__main__":
    n = int(input("Enter the number of days: "))
    delay = int(input("Enter the delay day: "))
    forget = int(input("Enter the forgetting day: "))
    
    result = peopleAwareOfSecret(n, delay, forget)
    print(result)
