# '11' + '11' -> 6 ('110')
# '111' + '111' -> ('10')

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i = pre = 0
        sum_list = []
        while i < len(a) and i < len(b):
            current_b = int(a[len(a)-1-i]) + int(b[len(b)-1-i]) + pre
            if pre: pre -= 1
            if current_b > 1:
                pre += 1
                current_b -= 2
            sum_list.append(str(current_b))
            i += 1
        
        while i < len(a):
            current_b = int(a[len(a)-1-i]) + pre
            if pre: pre -= 1
            if current_b > 1:
                pre += 1
                current_b -= 2
            sum_list.append(str(current_b))
            i += 1

        while i < len(b):
            current_b = int(b[len(b)-1-i]) + pre
            if pre: pre -= 1
            if current_b > 1:
                pre += 1
                current_b -= 2
            sum_list.append(str(current_b))
            i += 1

        if pre:
            sum_list.append('1')
        
        return ''.join(sum_list[::-1])