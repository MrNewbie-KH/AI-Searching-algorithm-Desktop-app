import Data

# method will take to cities one source second destination


def BFS(source, destination):
    visited = []
    queue = [[source]]
    while queue:
        path = queue.pop(0)
        node = path[-1]
        if node in visited:
            continue
        visited.append(node)
        if node == destination:
            return path
        else:
            neighbour_nodes = Data.GRAPH.get(node, [])
            for end_node in neighbour_nodes:
                path_new = path.copy()
                path_new.append(end_node)
                queue.append(path_new)
