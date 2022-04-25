#Worked on by both Max Curl and Mikey Sison

from collections import defaultdict


def make_undirected_graph(edge_list):
    """ Makes an undirected graph from a list of edge tuples. """
    graph = defaultdict(set)
    for e in edge_list:
        graph[e[0]].add(e[1])
        graph[e[1]].add(e[0])
    return graph


def reachable(graph, start_node):
    """
    Returns:
      the set of nodes reachable from start_node
    """
    result = set([start_node])
    frontier = set([start_node])
    result.add(start_node)
    while len(frontier) != 0:
        x = frontier.pop()
        if x in graph:
            for value in graph[x]:
                if value not in result:
                    frontier.add(value)
                    result.add(value)
    return result


def test_reachable():
    graph = make_undirected_graph([('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'B')])
    assert sorted(reachable(graph, 'B')) == ['A', 'B', 'C', 'D']

    graph = make_undirected_graph([('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'B'), ('E', 'F'), ('F', 'G')])
    assert sorted(reachable(graph, 'A')) == ['A', 'B', 'C', 'D']
    assert sorted(reachable(graph, 'E')) == ['E', 'F', 'G']


def connected(graph):
    for key in graph.keys():
        if len(graph) == len(reachable(graph, key)):
            return True
        else:
            return False


def test_connected():
    graph1 = make_undirected_graph([('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'B')])
    assert connected(graph1) == True
    graph = make_undirected_graph([('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'B'), ('E', 'F'), ('F', 'G')])
    assert connected(graph) == False


def n_components(graph):
    """
    Returns:
      the number of connected components in an undirected graph
    """
    lengths = []
    result = []
    if connected(graph):
        return 1
    else:
        for key in graph.keys():
            lengths.append(len(reachable(graph, key)))
    for element in lengths:
        if element in result:
            continue
        else:
            result.append(element)
    return len(result)

def test_n_components():
    graph = make_undirected_graph([('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'B')])
    assert n_components(graph) == 1

    graph = make_undirected_graph([('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'B'), ('E', 'F'), ('F', 'G')])
    assert n_components(graph) == 2
