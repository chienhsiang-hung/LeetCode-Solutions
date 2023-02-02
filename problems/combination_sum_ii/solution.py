# APPROACH I
# candidates = [10,1,2,7,6,1,5,7,2], target = 8
# [10]
# [10,1]
# [10,1,2]
# [10,1,2]+[7] => [[1,7]]
# [10,1,2,7]+[6] => [[2,6]]
# [10,1,2,7,6]+[1] => [[1,1,6]]
# [10,1,2,7,6,1]+[5] => [[1,2,5]]
# [10,1,2,7,6,1,5]+[7]
# [10,1,2,7,6,1,5,7]+[2]

# APPROACH II
# candidates = [10,1,2,7,6,1,5,7,2], target = 8
# 10:
# 1: [[1]]
# 2: [[1,2], [2]]
# 7: [[1,7], [7]] => [1,7]
# 6: [[1,6], [2,6]] => [2,6]
# 1: [[1,1], [1,1,2], [1,2], [1,7]...]

# Update APPROACH II
# candidates = [10,1,2,7,6,1,5,7,2], target = 8
# => [1,1,2,2,5,6,7,7,10], t=8
# 1: [1]
# 1: [1,1], [1]x
# 2: [1,2], [1,1,2], [2]
# 2: [1,2]x, [1,1,2]x, [1,2,2], [1,1,2,2], [2,2]
# loop:
#   when it's dup: add one before only and not self as one
#   when it's equal to target, add to output and del

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates = sorted(candidates)
        ans = []
        layers = []
        def solve(i, target=target):
            '''
            return [(_list, sum(_list))...], last_num
            '''
            if i == 0:
                if candidates[i] == target:
                    ans.append([candidates[i]])
                    return []
                layers.append((
                    [candidates[i]], candidates[i]
                ))
                return [(
                    [candidates[i]], candidates[i]
                )]
            
            last_layer = solve(i-1)
            current_layer = []
            # dup situation
            if candidates[i] == candidates[i-1]:
                if last_layer:
                    for _list, _sum in last_layer:
                        if (condi:=_sum+candidates[i]) == target:
                            ans.append(_list+[candidates[i]])
                        elif condi > target:
                            continue
                        else:
                            current_layer.append(
                                (_list+[candidates[i]], _sum+candidates[i])
                            )
                    layers.extend(current_layer)
                return current_layer
            
            # not dup situation
            if layers:
                for _list, _sum in layers:
                    if (condi:=_sum+candidates[i]) == target:
                        ans.append(_list+[candidates[i]])
                    elif condi > target:
                        continue
                    else:
                        current_layer.append(
                            (_list+[candidates[i]], _sum+candidates[i])
                        )
            # check self as one
            if candidates[i] == target:
                ans.append([candidates[i]])
                return current_layer
            layers.extend((
                current_layer + [
                    ([candidates[i]], candidates[i])
                ]
            ))
            return current_layer + [
                ([candidates[i]], candidates[i])
            ]
        
        solve(len(candidates)-1)
        return ans