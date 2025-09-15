import numpy as np
import random


def goodPoint(n_simulation:int, n:int)->float:
    '''
        好点问题模拟，n个0-1范围内的均匀分布随机点，其中好点个数的期望值。

    '''
    def neighbor(Xn, j)->int:
        # 找Xn[j]的邻居的index
        if j==0:
            return 1
        elif j == len(Xn)-1:
            return j-1
        elif Xn[j] - Xn[j-1] < Xn[j+1]-Xn[j]:
            return j-1
        else:
            return j+1
    def isGood(Xn, j)->bool:
        if neighbor(Xn,neighbor(Xn,j)) == j:
            return True
        else:
            return False

    res = []
    for _ in range(n_simulation):
        Xn = np.random.uniform(0,1,n)
        # 原地排序
        Xn.sort()
        count = 0
        for i in range(n):
            if isGood(Xn,i):
                count += 1
        res.append(count)
    
    EN  = sum(res)/n_simulation
    return EN

if __name__ == "__main__":

    N_sim = 1000

    EN = goodPoint(N_sim,100)
    print(f"good point expectation = {EN}")





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

