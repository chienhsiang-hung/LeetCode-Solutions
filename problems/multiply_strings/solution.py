class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        multiply_list = [0] * (len(num1) + len(num2))
        position = len(multiply_list) -1

        if num1 == '0' or num2 == '0':
            return '0'

        for n1 in num1[::-1]:
            tmp_pos = position
            for n2 in num2[::-1]:
                tmp_num = multiply_list[tmp_pos] + int(n1)*int(n2)
                multiply_list[tmp_pos] = tmp_num % 10
                multiply_list[tmp_pos-1] += tmp_num // 10
                tmp_pos -= 1
            position -= 1

        output = ''
        for num in multiply_list:
            output += str(num)
        
        if output[0] == '0':
            return output[1:] if output[1:] else '0'
        return output