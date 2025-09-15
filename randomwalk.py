import numpy as np
import random

def simulation_randomwalk_ring(n_simulation, n_pos):
    ''' n_pos个圆围城一个环，从某个圆开始，随机走动，期望走多少次能全部走到？
        n_simulation：模拟次数
        return ： 模拟走的次数平均值
    '''
    N_count = []
    ele = [1, 0, -1]
    prob = [1/4, 1/2, 1/4]
    for _ in range(n_simulation):
        res = set() # 记录已经填充的点，若填满，lenght = n_pos
        t = 0
        res.add(0)
        count = 0

        while (len(res) <n_pos):
            roll = np.random.choice(ele,p=prob)
            count += 1
            t += roll
            pos = t % n_pos # mod n_pos 取余数，结果为0 1 2 ... n_pos-1
            res.add(pos)

        N_count.append(count)
    
    ave = sum(N_count) / n_simulation
    return ave

def simulation_randomwalk_line(n_simulation, p, n):
    ''' 1维随机走动，从x=0出发期望走多少次能全部走到 |x| = n处？
        n_simulation：模拟次数
        return ： 模拟走的次数平均值
    '''
    elements = [1, 0, -1] #每一步 +1 or 不动 or -1
    probs = [p/2, 1-p, p/2] #每一步的概率, p的概率移动，1-p的概率不动

    N_count = [] #记录每次模拟得到步数N  理论值为n^2/p
    for _ in range(n_simulation):
        x = 0
        count = 0

        while (abs(x) <n):
            roll = np.random.choice(elements, p=probs)
            count += 1
            x += roll

        N_count.append(count)
    
    ave = sum(N_count) / n_simulation
    return ave

def simulation_randomwalk_asym(n_simulation, p, n):
    ''' 1维随机走动，向右一步的概率为p > 1/2, 从x=0出发期望走多少次能全部走到 x = n处？
        n_simulation：模拟次数
        return ： 模拟走的次数平均值 理论值：n/(2p - 1)
    '''
    elements = [1, -1] #每一步 +1 或 -1
    probs = [p, 1 - p] #每一步的概率

    N_count = [] #记录每次模拟得到步数N
    for _ in range(n_simulation):
        x = 0
        count = 0

        while (x < n):
            roll = np.random.choice(elements,p=probs)
            count += 1
            x += roll

        N_count.append(count)
    
    ave = sum(N_count) / n_simulation
    return ave

def simulation_randomwalk1(n_simulation, x0:int, a:int, b:int):
    '''
    从x0出发，到达a或b处。到达a的概率以及到达a或b的期望步数
    '''
    Res_1 = [] #记录每次的到达位置，0/1
    Res_2 = [] #记录每次的步数 步数
    for _ in range(n_simulation):
        x = x0
        count = 0

        while (a< x <b):
            roll = np.random.choice([-1,1])
            count += 1
            x += roll
        p=0
        if(x==a):
            p=1
        Res_1.append(p)
        Res_2.append(count)
    p_a = sum(Res_1)/n_simulation
    EN = sum(Res_2)/n_simulation
    return p_a, EN

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
    #ave = simulation_randomwalk_ring(N_sim,10)
    #print(f"expectation value : {ave}")

    #ave = simulation_randomwalk_line(N_sim, 1/2, 5)
    #print(f"expectation value : {ave}")

    # ave = simulation_randomwalk_asym(N_sim, 3/4, 5)
    # print(f"expectation value : {ave}")

    #res = simulation_randomwalk1(N_sim, 3, 0, 10)
    #print(f"{res[0]}, {res[1]}")

    EN = goodPoint(N_sim,100)
    print(f"good point expectation = {EN}")
