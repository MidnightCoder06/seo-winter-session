You're given a list of edges representing an unweighted, directed graph with at least one node.

Write a function that returns a boolean representing whether the given graph contains a cycle.

For the purposes of this question, a cycle is defined as any of number of vertices, including just one vertex, that are connected in a closed chain.

The given list is what's called an adjacency list, and it represents a graph.
The number of vertices in the graph is equal to the length of edges, where each index `i` in edge contains vertex `i`'s outbound edges, in no particular order.

Each individual edge is represented by a positive integer that denotes an index (a destination vertex) in the list that this vertex is connceted to.

Note that these edges are directed, meaning that you can only travel from a particular vertex to its destination, not the other way around (unless the destination vertex itself has an outbound edge to the original vertex).

Also note that this graph may contain self-loops. A self-loop is an edge that has the same destination and origin; in other words, its an edge that connects a vertex to itself. A self-loop is considered a cycle.

Sample Input:

edges = [
    [1,3],
    [2,3,4],
    [0],
    [],
    [2,5],
    []
]


Sample Output:

True

There are multiple cycles, here are a few:

* 0 -> 1 -> 2 -> 0
* 0 -> 1 -> 4 -> 2 -> 0
* 1 -> 2 -> 0 -> 1



Time:
0(v + e)


Space:
0(v) 
where v is the number of vertices of the input graph and e is number of edges of the input graph