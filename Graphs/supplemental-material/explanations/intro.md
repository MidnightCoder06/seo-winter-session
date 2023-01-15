
Core defintion 
- A graph is used to represent relationships between entities
    * An entity can be anything (a person, a computer, etc...)

Key terms:
- Vertex: the entity 
- Edge: represents a relationship between an entity 

Examples:

A professional graph would have humans as entities and the edges are their professional relationships. LinkedIn is built on a professional graph.

A social graph would have humans are entities and the edges are friends, parents, ect...
Facebook is built on a social graph.

In a location graph the edges would be locations and the edges are a way to get from one location to another - such as roads, rail and air. Google Maps is built on a location graph.

The internet is an example of an information graph. The entities are compputers. The Edges are ways to send information / data from one computer to another. For example the cables connecting data on the sea floor. Google takes advantage of this.

Supporting Google Drive: https://drive.google.com/drive/u/0/folders/1CEOm47-mfGQZNNJQH50BHhVbFmMdyVzw

View the following PDFs in order 

1. Intro.pdf
2. Directed-vs-Undirected.pdf


Graph traversal has the same traversal algorithms we already covered with trees. DFS & BFS.

There are two differences:
* In a tree, there is only one path from the root to a specific node.
    * In a graph multiple paths can lead from one node to another
* A graph can also have cycles, so the same node can be visited multiple times.

This makes graph traversal slighly more complicated - you need to avoid getting caught in an infinite loop.
In order to avoid infinite looping in a graph we need to keep track of the nodes previously visited.

For BFS since there is no "top" node you traverse level from the first node visited.

For the example the BFS traversal for the below graph would be 1,2,3,4,5 if 1 was visited first.  1,3,2,4,5 and 1,3,2,5,4 are also valid results.

1 - 2  \
|   |   4
3 - 5  /
