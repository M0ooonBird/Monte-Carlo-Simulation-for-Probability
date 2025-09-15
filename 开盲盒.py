import numpy as np
import random


def E_color(n_simulation:int, n:int, k:int)->float:
    '''
        每个盲盒有n种颜色，每种颜色等概率出现。
        开k个独立的盲盒，期望能开出多少种颜色？
    '''
    
    res = []
    for _ in range(n_simulation):
        color = set()

        for _i in range(k): #开k个盲盒
            c = np.random.randint(n) # 0,1,2,....,n-1
            color.add(c)

        n_color = len(color)
        res.append(n_color)
        
    E = sum(res)/n_simulation
    return E


def E_num(n_simulation:int, n:int)->float:
    '''
        每个盲盒有n种颜色，每种颜色等概率出现。
        平均需要开多少个盲盒，才能开出所有颜色？
    '''
    
    res = []
    for _ in range(n_simulation):
        color = set()

        count = 0
        while len(color) < n:
            c = np.random.randint(n) # 0,1,2,....,n-1
            color.add(c)
            count += 1
        
        res.append(count)
        
    E = sum(res)/n_simulation
    return E

if __name__ == "__main__":

    N_sim = 1000000
    n = 10  #盲盒种类
    k = 6   #开多少个盲盒

    P = E_color(N_sim, n, k)
    print(f"E color num = {P}")
    
    P = n*(1-((n-1)/n)**k)
    print(f"theoratical: {P}")

    Num = E_num(N_sim, n)
    print(f"平均开: {Num}个盲盒能开出所有颜色")


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

