import numpy as np
import random


def f(n_simulation:int, n:int, k:int)->float:
    '''
        A flips n+k coins, and B flips n coins. 
        Find the probability that the number of heads 
        obtained by Person A is greater than that obtained by Person B.
    '''
    
    res = []
    for _ in range(n_simulation):
        An = np.random.randint(2,size = n+k)
        Bn = np.random.randint(2,size = n)
        nA = sum(An)
        nB = sum(Bn)
        
        p = 0
        if(nA>nB):
            p = 1
        else:
            p=0

        res.append(p)

    P  = sum(res)/n_simulation
    return P

if __name__ == "__main__":

    N_sim = 1000000

    P = f(N_sim, 10,1)
    print(f"The probability that the number of heads of A is greater = {P}")

