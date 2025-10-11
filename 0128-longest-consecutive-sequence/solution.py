'''
[100,4,200,1,3,2]
{100}
{100,4}
{100,4,200}
{100,4,200,1}
{100,4,200,1,3}: 3, 4
2: 
'''
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        par_dict = dict()
        size_dict = dict()

        def find_p(n):
            if par_dict[n] == n:
                return n
            return find_p(par_dict[n])

        best_size = 1 if nums else 0
        for n in nums:
            if n in par_dict:
                continue
            par_dict[n] = n
            size_dict[n] = 1

            if n-1 in par_dict:
                p = find_p(n-1)
                par_dict[n] = p
                size_dict[p] += size_dict[n]
                best_size = max(best_size, size_dict[p])
            if n+1 in par_dict:
                p = find_p(n)
                par_dict[n+1] = p 
                size_dict[p] += size_dict[n+1]
                best_size = max(best_size, size_dict[p])
        
        return best_size
            
                
