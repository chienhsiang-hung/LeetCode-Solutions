class Solution:
    def isHappy(self, n: int) -> bool:
        # a. 123
        # b. 1+4+9 = 14
        # b. 1+16 = 17
        # b. 1+49 = 50
        # b. 25
        # b. 4+25 = 29
        # b. 4+81 = 85
        # b. 64+25 =89

        replaced_n = 0
        replaced_n_list = [n]
        while True:
            for digit in str(n):
                replaced_n += int(digit)**2
            if replaced_n == 1:
                return True
            elif replaced_n in replaced_n_list:
                return False            
            replaced_n_list.append(replaced_n)
            n = replaced_n
            replaced_n = 0