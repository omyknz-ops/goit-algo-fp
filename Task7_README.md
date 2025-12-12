# Task 7: Monte Carlo Dice Simulation

## Problem
Simulate rolling two dice and calculate the probability of each possible sum (2-12).

## Method
Monte Carlo simulation with 1,000,000 dice rolls.

## Results

| Sum | Monte Carlo | Analytical | Difference |
|-----|-------------|------------|------------|
| 2   | 2.77%       | 2.78%      | 0.00%      |
| 3   | 5.57%       | 5.56%      | 0.01%      |
| 4   | 8.33%       | 8.33%      | 0.00%      |
| 5   | 11.12%      | 11.11%     | 0.01%      |
| 6   | 13.90%      | 13.89%     | 0.01%      |
| 7   | 16.66%      | 16.67%     | 0.01%      |
| 8   | 13.86%      | 13.89%     | 0.03%      |
| 9   | 11.11%      | 11.11%     | 0.00%      |
| 10  | 8.34%       | 8.33%      | 0.01%      |
| 11  | 5.56%       | 5.56%      | 0.00%      |
| 12  | 2.78%       | 2.78%      | 0.00%      |

## Analysis

### Why sum 7 is most probable
Sum of 7 has 6 possible combinations: (1,6), (2,5), (3,4), (4,3), (5,2), (6,1), giving it probability of 6/36 = 16.67%.

### Why sums 2 and 12 are least probable
Only one way to get each: (1,1) for sum 2 and (6,6) for sum 12, giving 1/36 = 2.78% probability.

### Distribution symmetry
The probabilities are symmetric around 7 because for each sum below 7, there's a corresponding sum above 7 with the same number of combinations (e.g., sum 6 and sum 8 both have 5 combinations).

## Conclusions

1. **Accuracy**: Monte Carlo results match analytical probabilities with maximum error of 0.03%, demonstrating high accuracy with 1 million simulations.

2. **Law of Large Numbers**: As the number of simulations increases, the experimental probabilities converge to the theoretical values.

3. **Method Validation**: The Monte Carlo simulation successfully reproduces theoretical probabilities, confirming the correctness of both the simulation approach and analytical calculations.

4. **Practical Application**: This method is valuable when analytical calculations are difficult or impossible, as it provides reliable approximations through simulation.