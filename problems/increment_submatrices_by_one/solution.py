# refer to the visualization at https://leetcode.com/problems/increment-submatrices-by-one/solutions/3052675/python3-sweep-line-range-addition-with-visualization-clean-concise/

class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        mat = [ [0]*n for _ in range(n) ]
        query_map = defaultdict(int)
        for query in queries:
            for r in range(query[0], query[2]+1):
                query_map[(r, query[1])] += 1
                if query[3]+1 < n:
                    query_map[(r, query[3]+1)] -= 1

        for r in range(n):
            mat[r][0] = query_map[(r, 0)]
            for c in range(1, n):
                mat[r][c] = mat[r][c-1] + query_map[(r, c)]
        
        return mat