# What is Dynamic Programming

Dynamic programming is a technique of breaking down a problem into smaller problems, solving each sub-problems once, storing the solutions of these sub-problems, and eventually finding a solution to the original problem. 

We break down a big problem into smaller problems. Typically, the smaller problems are similar to the parent problem only difference being the scale. Thus, these sub-problems can also be divided further smaller sub-problems until we achieve problems that cannot be further divided. You can imagine we have a tree of a problem and their sub-problems. We start with solving the “leaf” level problems and then move on to their “parent” problems and so on. We save the results as we solve sub-problems for future reference. Thereby avoiding working on the same sub-problem if encountered again. 

This approach is like the divide and conquers algorithm where a problem is divided into sub-problems and recursively solving sub-problems and combining their solution to find the solution to the real problem.

# Dynamic Programming Characteristics

It is important to know when to use dynamic programming algorithms. There are two major characteristics to identify whether dynamic programming is the right fit. 

1. Optimal Substructure  

The problem should have optimal substructure properties. It means that the optimal solution can be evaluated from the optimal solutions of its sub-problems. This will also help you define the base case of the recursive algorithm. 

Consider an example of the Fibonacci series. We define the nth number as the sum of the previous 2 numbers. 

2. Fib(n) = Fib(n-1) + Fib(n-2)  

We can see that a problem of size “n” can be broken down into sub-problems of size “n-1” and “n-2”. We also know solutions of base cases, i.e., f(0) as 0 and f(1) 1.   as 1.   

3. Overlapping subproblems 

The other necessary property is overlapping sub-problems. A problem is said to have overlapping sub-problem properties if the sub-problems can be seen recursively visiting the same sub-problems. In such cases, we can improve the performance of an algorithm by storing the results of each sub-problem once it is calculated.

As seen above, in the case of Fibonacci dynamic programming numbers tree representation, several sub-problems like fib(4), fib(3), fib(2), and so on can be seen occurring multiple times. 

## Fibonacci example

As mentioned above Dynamic Programming is mainly an optimization over plain recursion. Wherever we see a recursive solution that has repeated calls for same inputs, we can optimize it using Dynamic Programming. The idea is to simply store the results of subproblems, so that we do not have to re-compute them when needed later. This simple optimization reduces time complexities from exponential to polynomial.

For example, if we write simple recursive solution for Fibonacci Numbers, we get exponential time complexity and if we optimize it by storing solutions of subproblems, time complexity reduces to linear.

### Exponential Runtime with plain Recursion 

int fib(int n) {
    if (n <= 1) 
        return n;
    return fib(n-1) + fib(n-2)
}

### Linear Runtime wiht Dynamic Programming 

f[0] = 0
f[1] = 1

for (i = 2; i <= n; i++) {
    f[i] = f[i -1] + f[i -2]
}

return f[n]

# Greedy Algorithms vs Dynamic Programming

Greedy Algorithms are similar to dynamic programming in the sense that they are both tools for optimization.

However, greedy algorithms look for locally optimum solutions or in other words, a greedy choice, in the hopes of finding a global optimum. Hence greedy algorithms can make a guess that looks optimum at the time but becomes costly down the line and do not guarantee a globally optimum.

Dynamic programming, on the other hand, finds the optimal solution to subproblems and then makes an informed choice to combine the results of those subproblems to find the most optimum solution.

# Dynamic Programming Techniques

There are two dynamic programming methods of implementation. 

### Top-Down Approach

This approach solves the bigger problem by recursively solving smaller sub-problems. As we solve the sub-problems, we store the result for later use. This way, we don’t need to solve the same sub-problem more than once. This method of saving the intermediate results is called Memoization (not memorization). 

### Bottom-Up Approach

The bottom-up method is an iterative version of the top-down approach. If we remove the recursion, there is no stack overflow issue and no overhead of the recursive functions. This approach starts with the smallest and works upwards to the largest sub-problems. Thus when solving a particular sub-problem, we already have results of smaller dependent sub-problems. The results are stored in an n-dimensional (n=>0) table. Thus, you can imagine when we arrive at the original problem, we have solved all its sub-problems. Now we just use the result set to find the best solution. This method is called Tabulation. 


# Steps to Solve Dynamic Programming Problems

1. Identify the sub-problem and write it down in words 

Too often, programmers will turn to writing code before thinking critically about the problem at hand. Not good. One strategy for firing up your brain before you touch the keyboard is using words, English or otherwise, to describe the sub-problem that you have identified within the original problem.

2. Sub-problem expressed as Mathematical recurrence 

Once you’ve identified a sub-problem in words, it’s time to write it out mathematically. Why? Well, the mathematical recurrence, or repeated decision, that you find will eventually be what you put into your code. Besides, writing out the sub-problem mathematically vets your sub-problem in words from Step 1. If it is difficult to encode your sub-problem from Step 1 in math, then it may be the wrong sub-problem!

There are two questions that I ask myself every time I try to find a recurrence:

What decision do I make at every step?
If my algorithm is at step i, what information would it need to decide what to do in step i+1? (And sometimes: If my algorithm is at step i, what information did it need to decide what to do in step i-1?)

3. Define memoization array strategy to fill it

We know that the problem has characteristics of overlapping sub-problems. We can use the memoization technique to cache the results of sub-problems for later use.

4. Coding the solution

While coding the algorithm, one can start with the initialization of the array (or cache) if required. Next, one should set the base case. Each problem can be solved in multiple ways using the dynamic programming approach. You need to think about which one suits you. 

### Which one is better?

The top-down approach is typically recursive. It has the overhead of recursive calls and therefore is slower than the bottom-up approach. 

One might find the top-down approach easier to implement because we use an array of some sort of lookup table to store results during recursion. While for the bottom-up approach we need to define the order of iteration and define an n-dimensional table for storing results. 

The top-down approach might also run into stack overflow conditions in the case of a very deep recursion tree. 


# Advantages of Dynamic Programming

* Dynamic programming can be used to obtain local as well as the total optimal solution. 
* Dynamic programming algorithms are generally compact code pieces as they are based on recursive functions. 
* Dynamic programming algorithms are often "easy" to debug. 

# Disadvantages of Dynamic Programming

* Dynamic programming uses recursion, which requires more memory in the call stack, and leads to a stack overflow condition in the runtime. 
* It takes memory to store the solutions of each sub-problem. There is no guarantee that the stored value will be used later in execution. 
High memory usage might lead to degraded performance. It depends on the dynamic programming algorithm and the programming language. For java, you can do Java certification to be able to use java efficiently. 

# Conclusion
One might find dynamic programming a bit intimidating initially. But if one understands the basics well, one can master dynamic programming problems. Having a strong programming foundation is key to getting comfortable with such problems. Applications of dynamic programming are common and relevant to everyday challenges, and mastering dynamic programming gives you the superpower to tackle them. 

# Frequently Asked Questions (FAQs)

1. Is dynamic programming used in real life?
There are numerous applications of dynamic programming in real life. Finding the shortest path between the source and multiple destinations. Git merge uses DP coding to find the longest common subsequence. There are other applications like image processing, optimal inventory management, production optimization, genetic algorithms, and matrix multiplication dynamic programming; the list is endless. 

2. What is the difference between recursion and dynamic programming?
Recursion is calling a function within itself. Sub-problems might have to be solved multiple times when a problem is solved using recursion. At the same time, Dynamic programming is a technique where you store the result of the previous calculation to avoid calculating the same once again. 

3. Which algorithm uses a dynamic programming approach? 
Algorithms that are aimed at solving optimization problems use a dynamic programming approach. Examples of dynamic programming algorithms are string algorithms like the longest common subsequence, longest increasing subsequence, and the longest palindromic substring. Optimizing the order for chain matrix multiplication. The Bellman-Ford algorithm for finding the shortest distance in a graph.