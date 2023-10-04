# Author: RT
# Date: 2023-10-04T03:42:58.509Z
# URL: https://leetcode.com/problems/count-visited-nodes-in-a-directed-graph/description/


from collections import Counter, defaultdict

from src.kosaraju import Kosaraju


class Solution:
    def countVisitedNodes(self, edges: list[int]) -> list[int]:
        n = len(edges)
        # O(V + E)
        sccs = Kosaraju(n, list(enumerate(edges))).find_sccs()

        rep = {}  # {[node_id]: [representative node_id]}
        rep_size = {}  # {[representative node_id]: size of scc}
        for scc in sccs:
            rep_size[scc[0]] = len(scc)
            for member in scc:
                rep[member] = scc[0]

        # build adj list for sccs
        scc_adj = defaultdict(set)
        for u, v in enumerate(edges):
            scc_adj[rep[u]].add(rep[v])

        # count nodes reachable from scc = count of current scc size +
        # sum of scc sizes connected sccs can reach. So we iterate scc
        # in topological order, i.e. reverse of Kosaraju dfs2 output
        scc_count = Counter(rep_size)
        for scc in reversed(sccs):
            rep_id = rep[scc[0]]
            scc_count[rep_id] += sum(
                (
                    scc_count[scc_rep_id]
                    for scc_rep_id in scc_adj[rep_id]
                    if scc_rep_id != rep_id  # avoid double counting the scc itself
                )
            )

        return [scc_count[rep[i]] for i in range(n)]
