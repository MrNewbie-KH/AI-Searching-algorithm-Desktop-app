import Data

# method will take to cities one source second destination


def DFS(source, destination):
    visited = []
    stack = [[source]]
    n = 0
    while stack:
        path = stack.pop()
        node = path[-1]
        if node == destination:
            return path

        if node in visited:
            continue
        visited.append(node)

        neighbour_nodes = Data.GRAPH.get(node, [])

        for end_node in neighbour_nodes:
            if end_node == destination:
                path.append(end_node)
                return path
            path_new = path.copy()
            path_new.append(end_node)
            stack.append(path_new)
