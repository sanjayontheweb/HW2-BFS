![BuildStatus](https://github.com/sanjayontheweb/HW2-BFS/workflows/HW2-BFS/badge.svg?event=push)

# Assignment 2
Breadth-first search

# Assignment Overview
The purpose of this assignment is to get you comfortable working with graph structures and to implement a breadth-first search function to traverse the graph and find the shortest path between nodes.

# Assignment Description

* BFS works by first checking edge cases of the entered values. If the start, end, or graph are invalid it shall return a ValueError. It then proceeds to initialize a queue of nodes to visit, an array of visited nodes, and a dictionary to map each node to a parent. Then, it starts by visiting the provided start node, adding all neighbors to the queue that is to be visited and making their parent the original node in our dictionary. There is a brief check here that happens in case a search is being performed instead of a traversal. If the popped node is the specified end node, we use the dictionary to trace the parent lineage back to the start node and return the path. If this is a traversal, or if the end node is not reached, we simply loop back to the top and pop the next neighbor off the queue to repeat with its neighbors. Queues are FIFO, so we pop the first element.


# Getting Started
To get started you will need to fork this repository onto your own github. You will then work on the code base from your own repo and make changes to it in the form of commits. 

# Reference Information
## Test Data
Two networks have been provided in an adjacency list format readable by [networkx](https://networkx.org/), is a commonly used python package for working with graph structures. These networks consist of two types of nodes:
* Faculty nodes 
* Pubmed ID nodes

However, since these are both stored as strings, you can treat them as equivalent nodes when traversing the graph. The first graph ("citation_network.adjlist") has nodes consisting of all BMI faculty members, the top 100 Pubmed papers *cited by* faculty, and the top 100 papers that *cite* faculty publications. Edges are directed and and edge from node A -> B indicates that node A *is cited by* node B. There are 5120 nodes and 9247 edges in this network.

The second network is a subgraph of the first, consisting of only the nodes and edges along the paths between a small subset of faculty. There are 30 nodes and 64 edges.

# Completing the assignment
Make sure to push all your code to github, ensure that your unit tests are correct, and submit a link to your github through the google classroom assignment.

# Grading

## Code (6 points)
* Breadth-first traversal works correctly (3)
* Traces the path from one faculty to another (2)
* Handles edge cases (1)

## Unit tests (3 points)
* Output traversal for mini data set (1)
* Tests for at least two possible edge cases (1)
* Correctly uses exceptions (1)

## Style (1 points)
* Readable code with clear comments and method descriptions
* Updated README with description of your methods

