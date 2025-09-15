import numpy as np
import random
import math

def waittingTime(n_simulation:int):
    '''
        A地铁每天8-9点之间随机到达一班，B地铁每天9点准时到达一班，
        你每天8-9点之间随机到地铁站，求你每天等地铁的时间的期望值
    '''
    
    res = []
    for _ in range(n_simulation):
        Xn = np.random.uniform(0,60,2)
        X = Xn[0]
        Y = Xn[1]
        T = 0
        if Y>X:
            T = 60-Y
        else:
            T = X-Y
        res.append(T)

    data_ = np.array(res)
    Time  = np.mean(data_)

    return Time


if __name__ == "__main__":

    N_sim = 10000000
    
    E = waittingTime(N_sim)
    print(f"平均等待时常：{E}min")



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
    print(r)

