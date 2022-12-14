from collections import defaultdict, deque


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ''

        window_map = defaultdict(int)
        t_map = dict()
        for tt in t:
            if tt not in t_map:
                t_map[tt] = 1
            else:
                t_map[tt] += 1
        tmp_t_map = t_map.copy()

        output = ''
        word_q = deque()
        start_record = False
        for ss in s:
            if ss in t_map: start_record = True
            if start_record:
                word_q.append(ss)
                window_map[ss] += 1
                if ss in tmp_t_map:
                    tmp_t_map[ss] -= 1
                    if tmp_t_map[ss] == 0: del tmp_t_map[ss]

                    # end of current round, start a new round
                    if not tmp_t_map:
                        # record the words
                        if len(output) > len(current_word:=''.join(word_q)) or output == '':
                            output = current_word

                        if len(output) == 1: # means len(t)==1
                            return output

                        window_map[word_q[0]] -= 1
                        tmp_t_map[ word_q.popleft() ] = 1

                while word_q[0] not in t_map or (
                    window_map[ word_q[0] ] > t_map[ word_q[0] ]
                    if word_q[0] in t_map
                    else False
                ):
                    window_map[ word_q.popleft() ] -= 1
                    
                    if not word_q: break

        return output
            