from collections import deque, defaultdict
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0: return 0

        # use defaultdict to record the visited for DP
        visited = defaultdict(lambda: False)

        new_coins = set() # use set to keep dup num from adding in
        level = 1
        for node in coins:
            if node < amount:
                if visited[node]:
                    continue
                new_coins.add(node)
                visited[node] = True
            elif node == amount:
                return level
        if not new_coins:
            return -1
        
        queue = deque([ new_coins ])
        # BFS
        while queue:
            level += 1
            current_floor = queue.popleft()
            coins = set()
            for node in current_floor:
                for next_coin in new_coins:
                    if (current_n := node+next_coin) == amount:
                        return level
                    elif current_n < amount:
                        if visited[current_n]:
                            continue
                        coins.add(current_n)
                        visited[current_n] = True
            if coins:
                queue.append(coins)
        return -1
            
        
            
