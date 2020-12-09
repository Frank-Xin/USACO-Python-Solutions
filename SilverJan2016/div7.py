'''
Problem: Subsequences Summing to Sevens

Source: http://www.usaco.org/index.php?page=viewproblem2&cpid=595

Solution: An interesting property of prefix sums is that if two prefix sums 
have the same remainder when divided by k, the difference in the indices will
be the length of the subarray that sums up to be a number divisible by k. Keeping
track of the largest difference as you loop through the input array will solve 
the problem.
'''

inp = open("div7.in", "r")
out = open("div7.out", "w")
N = int(inp.readline())
cumulative_sum = 0
mod_cows = {
    0: [],
    1: [],
    2: [],
    3: [],
    4: [],
    5: [],
    6: []
}
longest_subarray = 0

for i in range(N):
    cumulative_sum += int(inp.readline())
    remainder = cumulative_sum % 7
    mod_cows[remainder].append(i)
    if (len(mod_cows[remainder]) > 1):
        longest_subarray = max(longest_subarray, mod_cows[remainder][-1] - mod_cows[remainder][0])
        
print(longest_subarray, file=out)