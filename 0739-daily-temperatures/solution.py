class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        if len(temperatures) == 1: return [0]
        index_stack = [0]

        res = [0] * len(temperatures)
        for i in range(1, len(temperatures)):
            if temperatures[i] <= temperatures[index_stack[-1]]:
                index_stack.append(i)
                continue
            while index_stack and temperatures[i] > temperatures[index_stack[-1]]:
                j = index_stack.pop()
                res[j] = i - j
            index_stack.append(i)
        return res
                 
