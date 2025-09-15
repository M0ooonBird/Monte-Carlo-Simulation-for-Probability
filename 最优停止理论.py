import numpy as np

def f(n:int):
    '''
        有n个样品，依次供你选择，你该怎么选才能尽可能选到最优的？
        最大化概率Pk = k(1/k + 1/k+1 + ... +1/n-1)/n, k 从1到n-1
        对于给定的n，返回能取最大值的k
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
    