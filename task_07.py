import random

# Monte Carlo simulation to estimate probabilities of sums when rolling two dice
def monte_carlo_dice(num_simulations=1000000):
    sums_count = {i: 0 for i in range(2, 13)} # Possible sums from 2 to 12
    
    # Simulate dice rolls
    for _ in range(num_simulations):
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        sums_count[dice1 + dice2] += 1
    
    probabilities = {k: v / num_simulations * 100 for k, v in sums_count.items()}
    return probabilities

# Analytical probabilities
analytical = {
    2: 2.78, 3: 5.56, 4: 8.33, 5: 11.11, 6: 13.89,
    7: 16.67, 8: 13.89, 9: 11.11, 10: 8.33, 11: 5.56, 12: 2.78
}

monte_carlo = monte_carlo_dice()

print("Sum | Monte Carlo | Analytical | Difference")
print("-" * 50)
for s in range(2, 13):
    mc = monte_carlo[s]
    an = analytical[s]
    diff = abs(mc - an)
    print(f"{s:3} | {mc:11.2f}% | {an:10.2f}% | {diff:6.2f}%")