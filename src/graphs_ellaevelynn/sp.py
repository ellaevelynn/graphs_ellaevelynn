import sys
from .heapq import MinHeap

def dijkstra(graph, source):
    """
    Computes shortest path distances and paths from a source vertex.
    Returns: (dist_dict, path_dict)
    """
    nodes = set(graph.keys())
    for u in graph:
        nodes.update(graph[u].keys())

    dist = {node: sys.maxsize for node in nodes}
    parent = {node: None for node in nodes}
    dist[source] = 0

    heap = MinHeap()
    heap.push((0, source))

    visited = set()

    while not heap.is_empty():
        d, u = heap.pop()

        if u in visited:
            continue
        visited.add(u)

        if u in graph:
            for v, weight in graph[u].items():
                if dist[u] + weight < dist[v]:
                    dist[v] = dist[u] + weight
                    parent[v] = u
                    heap.push((dist[v], v))

    paths = {}
    for target in sorted(nodes):
        if dist[target] == sys.maxsize:
            paths[target] = []
            continue
        
        curr = target
        path = []
        while curr is not None:
            path.append(curr)
            curr = parent[curr]
        path.reverse()
        paths[target] = path

    return dist, paths


def bfs(graph, source):
    """
    Bonus Feature: Breadth-First Search traversal order starting from source.
    """
    visited = set([source])
    queue = [source]
    traversal = []

    while queue:
        u = queue.pop(0)
        traversal.append(u)
        if u in graph:
            for neighbor in graph[u]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
    return traversal