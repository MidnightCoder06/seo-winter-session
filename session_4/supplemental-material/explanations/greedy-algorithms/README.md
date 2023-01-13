What is a greedy algorithm?


A greedy algorithm is an algorithmic paradigm that follows the problem-solving heuristic of making the locally optimal choice (i.e. a greedy choice) at each stage with the hope of finding a global optimum. In other words, a greedy algorithm makes the best choice at each step by considering only the current step, without worrying about the consequences of its choices on future steps.

Here are some characteristics of greedy algorithms:

- They are often "easy" to implement and understand.
- They are often faster than other algorithms, because they make a decision at each step without considering all the possible options.
- They can give an optimal solution for some problems, but not all problems.

Example:

Take a look at the image titled 'greedy-algo-sample.png' in this folder.
Let's say you have lots of bags of money. Each of the bags is either a $20, $10, or $5 bag.
A friend asks you for $35.
A greedy algorithm approach would be not do any complex thinking to find the optimal denominations to give but instead to just give bags with the highest total in descedning order (ordered by largest to smallest).
Give a $20 bag, then a $10 bag, then a $5 bag.

Only change the amount you're giving if giving the same amount would go above the amount asked.
