from collections import defaultdict

class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        ABs = {'A': 0, 'B': 0}
        A_pos = []
        pos_guess = defaultdict(int)
        # find A
        for s, g in zip(secret, guess):
            if s == g:
                ABs['A'] += 1
                A_pos.append(True)
            else:
                A_pos.append(False)
                pos_guess[g] += 1

        # find B
        for i, guessed in enumerate(A_pos):
            if not guessed:
                if pos_guess[ secret[i] ] > 0:
                    pos_guess[ secret[i] ] -= 1
                    ABs['B'] += 1
        
        return f"{ABs['A']}A{ABs['B']}B"