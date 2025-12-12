# Greedy approach to select items
def greedy_algorithm(items, budget): 
    # Sort by calories/cost ratio
    sorted_items = sorted(items.items(), 
                         key=lambda x: x[1]['calories'] / x[1]['cost'], 
                         reverse=True)
    
    total_cost = 0
    selected = {}
    
    for name, info in sorted_items: # Try to add item if within budget
        if total_cost + info['cost'] <= budget:
            selected[name] = 1
            total_cost += info['cost']
    
    return selected

# DP approach to select items
def dynamic_programming(items, budget): 
    names = list(items.keys())
    n = len(names)
    dp = [[0] * (budget + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        name = names[i - 1]
        cost = items[name]['cost']
        calories = items[name]['calories']
        
        for w in range(budget + 1):
            dp[i][w] = dp[i - 1][w]
            if cost <= w:
                dp[i][w] = max(dp[i][w], dp[i - 1][w - cost] + calories)
    
    # Backtrack
    selected = {}
    w = budget
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            name = names[i - 1]
            selected[name] = 1
            w -= items[name]['cost']
    
    return selected


items = {
    "pizza": {"cost": 50, "calories": 300},
    "hamburger": {"cost": 40, "calories": 250},
    "hot-dog": {"cost": 30, "calories": 200},
    "pepsi": {"cost": 10, "calories": 100},
    "cola": {"cost": 15, "calories": 220},
    "potato": {"cost": 25, "calories": 350}
}

budget = 100

greedy_result = greedy_algorithm(items, budget)
greedy_calories = sum(items[item]['calories'] for item in greedy_result)
greedy_cost = sum(items[item]['cost'] for item in greedy_result)

dp_result = dynamic_programming(items, budget)
dp_calories = sum(items[item]['calories'] for item in dp_result)
dp_cost = sum(items[item]['cost'] for item in dp_result)

print(f"Greedy: {greedy_result}, Calories: {greedy_calories}, Cost: {greedy_cost}")
print(f"DP: {dp_result}, Calories: {dp_calories}, Cost: {dp_cost}")