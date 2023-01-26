# '()' Y
# '({()[]})' Y

# (, {, [ should come first 
# not '({)}'
class Solution:
    def isValid(self, s: str) -> bool:
        bracket_map = {
            '(': ')', '{': '}', '[': ']'
        }

        closes = []
        for bracket in s:
            if bracket not in bracket_map and not closes:
                return False

            elif bracket in bracket_map:
                closes.append(bracket_map[bracket])

            else:
                if bracket != closes.pop(): return False
        
        return not closes