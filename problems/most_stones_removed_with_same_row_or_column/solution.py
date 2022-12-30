# it's basically the same as num of provinces one
# len(stones) - num of provinces

from collections import defaultdict
class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        visited = defaultdict(bool)
        graph = defaultdict(set)
        for stone in stones: # build graph
            graph[f'r{stone[0]}'].add(tuple(stone))
            graph[f'c{stone[1]}'].add(tuple(stone))

        def dfs(stone: tuple):
            if visited[stone]:
                return
            visited[stone] = True
            # row
            for next_stone in graph[f'r{stone[0]}']:
                dfs(tuple(next_stone))
            # col
            for next_stone in graph[f'c{stone[1]}']:
                dfs(tuple(next_stone))

        provinces = 0
        for stone in stones:
            if visited[tuple(stone)]:
                continue
            provinces += 1
            dfs(tuple(stone)) # update visited
        
        return len(stones) - provinces
        