import numpy as np
import random


def f(n_simulation:int)->float:
    '''
        Suppose in a society, everyone values daughters over sons, 
        and every couple follows this rule when having children: 
        if they have a daughter, they stop having more children; 
        if they have a son, they continue having children until they have a daughter. 
        Will the gender ratio (of men to women) in this society become imbalanced?
    '''
    
    total_boy = 0
    total_children = 0
    for _ in range(n_simulation):
        children = []
        x = np.random.randint(2) # 0 or 1, 0:boy, 1:girl
        children.append(x)

        while x!=1:
            x = np.random.randint(2)
            children.append(x)

        # children = [0 0 0 ... 1]

        total_boy += len(children) - 1;
        total_children += len(children)

        
    P  = total_boy/ total_children
    return P

if __name__ == "__main__":

    N_sim = 10000000

    P = f(N_sim)
    print(f"boy's ratio = {P}")



