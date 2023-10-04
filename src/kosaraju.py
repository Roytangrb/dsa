"""Kosaraju's algorithm to find SCCs in directed graphs"""


from collections import defaultdict


class Kosaraju:
    """Usage: scc_components = Kosaraju(n, edges).find_sccs()

    Args:
        n (int): number of vertices, assuming labelled from 0 ~ n - 1.
        edges (Iterable[list[int] | tuple[int, int]]): (u, v) edges from u to v.
    Returns:
        list[list[int]]: 2d list of components. E.g. [[0, 1, 2], [3], [4]].
    """

    n: int
    adj: defaultdict[int, list]
    radj: defaultdict[int, list]

    def __init__(self, n: int, edges: list[list[int]]) -> None:
        self.n = n
        self.adj = defaultdict(list)
        self.radj = defaultdict(list)
        for u, v in edges:
            # construct graph to compute finished time for each node
            self.add_edge(self.adj, u, v)
            # construct transposed graph to find SCCs
            self.add_edge(self.radj, v, u)

    def add_edge(self, graph: defaultdict[int, list], u: int, v: int) -> None:
        """Add an edge from u to v"""
        graph[u].append(v)

    def find_sccs(self) -> list[list[int]]:
        stack = []
        visited = [False] * self.n
        # compute finished time, push to stack when no more nodes could be visited
        for i in range(self.n):
            self._dfs1(i, visited, stack)

        # second dfs on transposed graph in finished time descending order
        visited = [False] * self.n
        scc_componets = []
        while stack:
            node = stack.pop()
            if not visited[node]:  # prevent empty component in outputs
                component = []
                self._dfs2(node, visited, component)
                scc_componets.append(component)

        return scc_componets

    def _dfs1(self, node: int, visited: list[bool], stack: list[int]) -> None:
        if visited[node]:
            return

        visited[node] = True
        for neighbor in self.adj[node]:
            self._dfs1(neighbor, visited, stack)

        stack.append(node)

    def _dfs2(self, node: int, visited: list[bool], component: list[int]) -> None:
        if visited[node]:
            return

        visited[node] = True
        for neighbor in self.radj[node]:
            self._dfs2(neighbor, visited, component)

        component.append(node)


# Tests
if __name__ == "__main__":
    testcases = (
        (4, [[0, 1], [1, 2], [2, 0], [3, 0]], [[3], [1, 2, 0]]),
        (5, [[0, 1], [1, 2], [2, 3], [3, 4], [4, 0]], [[1, 2, 3, 4, 0]]),
        (1, [], [[0]]),
    )

    for n, edges, expected in testcases:
        actual = Kosaraju(n, edges).find_sccs()
        assert actual == expected, f"{expected=}, {actual=}"

    print(f"{__file__}: passed")
