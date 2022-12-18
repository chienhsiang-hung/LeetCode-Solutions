class Solution:
    def smallestValue(self, n: int) -> int:
        input_ = n
        prime = []
        i = 2
        while i <= n:

            # check the i itself, if it's prime
            j = 2
            i_is_prime = True
            while j*j <= i:
                if i % j == 0:
                    i_is_prime = False
                    break
                j += 1
            if i_is_prime:
                if n % i == 0:
                    prime.append(i)
                    n /= i
                    continue
            i += 1

        n = sum(prime)
        if n == input_:
            return n
        
        j = 2
        n_is_prime = True
        while j*j <= n:
            if n % j == 0:
                n_is_prime = False
                break
            j += 1
        if n_is_prime:
            return n
        else:
            return self.smallestValue(n)
                     
                    
                