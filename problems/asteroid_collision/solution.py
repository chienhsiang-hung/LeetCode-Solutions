class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        i = 0

        def pos(i):
            return i > 0

        new_asteroids=[]; the_state=[]
        while i < len(asteroids):
            if not new_asteroids:
                new_asteroids.append(asteroids[i])
                the_state.append(pos(asteroids[i]))
            else:
                # when + + or - - or - +
                if (
                    (current_state:=pos(asteroids[i])) == the_state[-1] or 
                    (not the_state[-1] and current_state)
                ):
                    new_asteroids.append(asteroids[i])
                    the_state.append(current_state)
                # + and - only
                else:
                    # collide
                    if abs(asteroids[i]) == abs(new_asteroids[-1]):
                        new_asteroids.pop()
                        the_state.pop()
                    # be eaten
                    elif abs(asteroids[i]) > abs(new_asteroids[-1]):
                        new_asteroids.pop()
                        the_state.pop()
                        continue # do not update i
                    # eat
                    else:
                        pass
            
            i += 1
        
        return new_asteroids
            
        