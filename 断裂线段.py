import numpy as np
import random


def f(n_simulation:int, n:int):
    '''
        (0,1)的区间上均匀分布随机取n-1个点，分成n段，其中的长度的最大值和最小值的期望
    '''
    
    res_max = []
    res_min = []
    for _ in range(n_simulation):
        random_floats = np.random.uniform(0, 1, n-1)
        random_floats.sort()

        Len = []
        Len.append(random_floats[0])
        
        for i in range(1,n-1):
            si = random_floats[i] - random_floats[i-1]
            Len.append(si)

        Len.append(1-random_floats[n-2])   

        Lmax = max(Len)
        Lmin = min(Len)

        res_max.append(Lmax)
        res_min.append(Lmin)
        
    E_max = sum(res_max)/n_simulation
    E_min = sum(res_min)/n_simulation
    
    return E_max,E_min


def H(n):
    sum = 0 
    for i in range(1,n+1):
        sum += 1/i

    return sum


if __name__ == "__main__":

    N_sim = 1000000
    n = 4 
    P = f(N_sim, n)
    print(f"E_max = {P[0]},\nE_min = {P[1]}")
    print(f"E_max = {H(n)/n},Emin = {1/n**2}")
    

# 标准库随机数
    random.random() # 0-1内随机浮点数
    random.uniform(3,5) # 3-5范围内均匀分布的随机浮点数

    random.randint(1,6) #1-6范围内的随机整数
    random.randrange(10) # 0-9范围内的随机整数
    # 生成 [5, 15) 的随机整数，即 [5, 14]
    random.randrange(5, 15)
    # 生成 [0, 100) 中步长为5的随机数，比如 0, 5, 10, ..., 95
    random.randrange(0, 100, 5)

    random.gauss(0,1) # N(0,1)标准正态

# numpy库随机数
    # 生成 [0, 10) 的随机整数，即 [0, 9]，1个数字
    random_int = np.random.randint(0, 10)
    # 生成 5 个 [1, 100] 范围内的随机整数
    random_ints = np.random.randint(1, 101, size=5)

    # 生成 1 个 [0.0, 1.0) 的随机浮点数
    random_floats = np.random.uniform(0, 1)

    # 生成 [3.0, 7.0] 范围内的 3 个随机浮点数
    random_floats = np.random.uniform(3.0, 7.0, 3)
    # 生成正态分布的随机数 N(mu,sigma)
    normal_data = np.random.normal(0, 1)

    r = np.random.choice([1,2,3,4,5,6]) #从给定范围随机选一个数

