import numpy as np

def f(n:int):
    '''
        设样品编号为1,2,...,n, 你依次看到样品，看到第k个时，你只能选择它或放弃它
        若放弃它，你就不能再选择它了，你只能继续看到第k+1个样品
        你想选到最大的样品，你该怎么选？
        理论上，选择前k个样品不选，第k+1个样品开始选，若后面有比它更大的就选它
        对于给定的n，选择k能使选到最大的样品的概率最大
        最大化概率P = k(1/k + 1/(k+1) + ... +1/(n-1))/n, k 从1到n-1
    '''
    
    res = []
    for k in range(1,n):
        sum = 0
        for i in range(k,n):
            sum += 1/(i)

        sum *= k
        res.append(sum)

    np_array = np.array(res)  # 将列表转换为 NumPy 数组
    max_index = np.argmax(np_array)  # 使用 argmax 获取最大值的索引
    max_value = np_array[max_index]/n  # 最大概率
    
    return max_index,max_value


if __name__ == "__main__":

    n = 5 # 样品数量
    max_index,max_value = f(n)
    print(f"n = {n}, max_k = {max_index}, k/n = {max_index/n}, max_prob = {max_value}")
    