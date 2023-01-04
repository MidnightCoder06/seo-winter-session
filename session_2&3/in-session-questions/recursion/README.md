* recursive frame stacks is one way we can measure space complexity of tree problems
* stackoverflow website terms comes from this 


The term Recursion can be defined as the process of defining something in terms of itself.

It's when a function calls itself.

A complicated function can be split down into smaller sub-problems utilizing recursion.

What is a recursive function 
-->  It means that a function calls itself. This has the benefit of meaning that you can loop through data to reach a result.

```

def fn():
    # ...
    fn()
    # ...

```

```

def fn():
    # ...
    if condition:
        # stop calling itself
    else:
        fn()
    # ...

```

* base case
* recursive case

The base case is the condition to stop the recursion. 
The recursive case is the part where the function calls on itself



https://www.programiz.com/python-programming/online-compiler/ 

```

def countdown(n):
    print(n)
    if n == 0:
        return
    else:
        countdown(n - 1)

>>> countdown(5)
5
4
3
2
1
0

```

Notice how countdown() fits the paradigm for a recursive algorithm described above:

The base case occurs when n is zero, at which point recursion stops.
In the recursive call, the argument is one less than the current value of n, so each recursion moves closer to the base case.


Here’s one possible non-recursive implementation for comparison:

```

def countdown(n):
    while n >= 0:
        print(n)
        n -= 1

>>> countdown(5)
5
4
3
2
1
0

```