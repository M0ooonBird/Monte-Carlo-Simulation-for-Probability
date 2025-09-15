import numpy as np
import random
import math

def probability(n_simulation:int, n:int):
    '''
        n个 人 坐n个对应的位置，1坐1号位，2坐2号位，...n坐n号位
        但1号喝醉了，他随机坐一个位置，后面的人依次找自己的位置，若自己的位置被占了，则也随机
        坐一个空余位置。最后一个人有多大的概率能坐到n号位？
    '''
    
    res = [] # 记录每次试验结果 0 1,若最后一人坐到自己的位置，记录1，否则记录0
    # n_simulation 次独立重复试验
    for _ in range(n_simulation):
        # 生成所有座位1-n
        seat = [i for i in range(1, n+1)]
        # 第一个人随机坐
        X1 = np.random.randint(1,n+1)
        seat.remove(X1)

        # 2号到n-1号
        for i in range(2,n):
            if i in seat: # i没有被占
                seat.remove(i)
            else:
                idx_i = np.random.randint(0,len(seat))
                Xi = seat[idx_i]
                seat.remove(Xi)
        # 判断最后剩的一个位置是否是n号
        if seat[0] == n:
            res.append(1)
        else:
            res.append(0)

    data_ = np.array(res)
    p  = np.mean(data_)

    return p

if __name__ == "__main__":

    N_sim = 100000
    n = 100
    E = probability(N_sim, n)
    print(f"n号坐到自己位置的的概率：{E}")
    print(f"理论值: {1/2}")
