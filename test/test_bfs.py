# write tests for bfs
import pytest
from search.graph import Graph
import networkx as nx

#Created with aid by ChatGPT

def test_bfs_traversal():
    """
    TODO: Write your unit test for a breadth-first
    traversal here. Create an instance of your Graph class 
    using the 'tiny_network.adjlist' file and assert 
    that all nodes are being traversed (ie. returns 
    the right number of nodes, in the right order, etc.)
    """
    tiny_graph = Graph('data/tiny_network.adjlist')
    tiny_start = list(tiny_graph.graph.nodes())[0]

    naive_bfs = tiny_graph.bfs(tiny_start)
    actual_bfs = list(nx.bfs_tree(tiny_graph.graph, tiny_start).nodes())
    
    #Assert full traversal
    assert len(naive_bfs) == len(tiny_graph.graph.nodes())

    #Assert order is correct
    assert naive_bfs == actual_bfs

    #Test empty graph errors
    empty_graph = Graph('data/empty_network.adjlist')
    with pytest.raises(ValueError):
        empty_graph.bfs(tiny_start)
        pass

    #Test that fake starts error
    with pytest.raises(ValueError):
        tiny_graph.bfs('fakeStart')
        pass


    #Repeat test with big graph
    big_graph = Graph('data/citation_network.adjlist')
    big_start = list(big_graph.graph.nodes())[0]

    naive_bfs = big_graph.bfs(big_start)
    actual_bfs = list(nx.bfs_tree(big_graph.graph, big_start).nodes())
    

    #Assert full traversal
    assert len(naive_bfs) == len(actual_bfs)

    #Assert order is correct
    assert naive_bfs == actual_bfs


def test_bfs():
    """
    TODO: Write your unit test for your breadth-first 
    search here. You should generate an instance of a Graph
    class using the 'citation_network.adjlist' file 
    and assert that nodes that are connected return 
    a (shortest) path between them.
    
    Include an additional test for nodes that are not connected 
    which should return None. 
    """

    #Test BFS-search on tiny graph
    tiny_graph = Graph('data/tiny_network.adjlist')
    tiny_start = list(tiny_graph.graph.nodes())[0]
    tiny_end = list(tiny_graph.graph.nodes())[-1]

    naive_bfs = tiny_graph.bfs(tiny_start, tiny_end)
    actual_bfs = nx.shortest_path(tiny_graph.graph, tiny_start, tiny_end)

    #Assert order is correct
    assert naive_bfs == actual_bfs


    #Repeat test with big graph
    big_graph = Graph('data/citation_network.adjlist')
    big_island = list(big_graph.graph.nodes())[0]
    big_start = list(big_graph.graph.nodes())[-3]
    big_end = list(big_graph.graph.nodes())[-1]


    assert big_graph.bfs(big_island, big_end) == None
    
    
    naive_bfs = big_graph.bfs(big_start, big_end)
    actual_bfs = nx.shortest_path(big_graph.graph, big_start, big_end)
    
    #Assert length is correct, node choice may differ
    assert len(naive_bfs) == len(actual_bfs)


