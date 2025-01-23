import networkx as nx

class Graph:
    """
    Class to contain a graph and your bfs function
    
    You may add any functions you deem necessary to the class
    """
    def __init__(self, filename: str):
        """
        Initialization of graph object 
        """
        self.graph = nx.read_adjlist(filename, create_using=nx.DiGraph, delimiter=";")

    def bfs(self, start, end=None):
        """
        TODO: write a method that performs a breadth first traversal and pathfinding on graph G

        * If there's no end node input, return a list nodes with the order of BFS traversal
        * If there is an end node input and a path exists, return a list of nodes with the order of the shortest path
        * If there is an end node input and a path does not exist, return None

        """

        # Created with aid by ChatGPT

        if self.graph is None or len(self.graph) == 0:
            raise ValueError("The graph is empty.")
        if start not in self.graph:
            raise ValueError(f"Start node '{start}' is not in the graph.")
        if end and end not in self.graph:
            raise ValueError(f"End node '{end}' is not in the graph.")

        # Queue for BFS traversal
        queue = [start]
        visited = [start]
        parent = {start: None}  # For reconstructing the path

        while queue:
            current = queue.pop(0)

            # If we are looking for a path and found the end node
            if end and current == end:
                path = []
                while current:
                    path.append(current)
                    current = parent[current]
                return path[::-1]  # Return the reversed path

            for neighbor in self.graph[current]:
                if neighbor not in visited:                    
                    queue.append(neighbor)
                    visited.append(neighbor)
                    parent[neighbor] = current

        # If an end node was provided but not reached, return None
        if end:
            return None

        # If no end node was provided, return the BFS traversal order
        return visited




