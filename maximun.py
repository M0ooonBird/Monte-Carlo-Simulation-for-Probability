import numpy as np
import random
import math

def expectation_max_min(n_simulation:int, n:int):
    '''
        n个IID的U(0,1)随机数，求最大值和最小值的期望、方差、相关系数
        最大、最小值期望的理论值为 n/(n+1), 1/(n+1)
        方差的理论值为n/((n+1)^2 (n+2))
        相关系数理论值为1/n
    '''
    
    res_Z = []
    res_Y = []
    res_YZ = []
    for _ in range(n_simulation):
        Xn = np.random.uniform(0,1,n)
        a = max(Xn)
        b = min(Xn)

        res_Z.append(a)
        res_Y.append(b)
        res_YZ.append(a*b)

    data_max = np.array(res_Z)
    data_min = np.array(res_Y)
    data_YZ  = np.array(res_YZ)

    E_max  = np.mean(data_max)
    E_min  = np.mean(data_min)
    E_YZ = np.mean(data_YZ)

    # 样本方差
    var_max = np.var(data_max,ddof=1)
    var_min = np.var(data_min,ddof=1)
    corr = (E_YZ - E_max*E_min) / math.sqrt(var_max * var_min)

    return E_max,var_max, E_min, var_min, corr

if __name__ == "__main__":

    N_sim = 10000000
    n = 3
    E = expectation_max_min(N_sim, n)
    print(f"最大值期望：{E[0]}, 最大值方差：{E[1]}, 最小值期望：{E[2]}, 最小值方差:{E[3]}")
    print(f"最大值期望理论：{n/(n+1)}, 最小值期望理论：{1/(n+1)}, 方差理论:{n/((n+2)*(n+1)**2)}")
    print(f"相关系数：{E[4]}")



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

