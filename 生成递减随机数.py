import numpy as np
import random
import math

def E_min(n_simulation:int)->float:
    '''
        依次生成U(0,1)的随机数X_i，只要生成的数维持递减就继续生成，
        直到不再递减。求这样产生的最小的随机数的期望值E(X)
        以及生成随机数的数量的期望E(N)
    '''
    
    res_min = []
    res_N = []
    for _ in range(n_simulation):
        last = np.random.uniform(0,1) #x1
        new_samp = np.random.uniform(0,1) # x2

        count = 2
        while new_samp <= last:

            last = new_samp
            new_samp = np.random.uniform(0,1)
            count += 1

        res_min.append(last)
        res_N.append(count)
        
    Em = sum(res_min)/n_simulation
    EN = sum(res_N)/n_simulation
    return Em,EN

def f(k:int)->float:
    sum = 0
    for n in range(1,k):
        sum += 1/(n+1) *(1/math.factorial(n-1)-1/math.factorial(n))
    return sum


if __name__ == "__main__":

    N_sim = 2000000

    Emin, En = E_min(N_sim)
    print(f"E min = {Emin}, E num = {En}")
    print(f"{f(18)}")
