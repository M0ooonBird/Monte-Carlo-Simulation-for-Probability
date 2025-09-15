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

