

class Node:
    """环形链表节点类"""
    def __init__(self, no: int):
        self.no = no      # 节点编号
        self.next = None  # 指向下一个节点

class CircularLinkedList:
    """环形链表管理类"""
    def __init__(self):
        self.head = None  # 链表头节点
    
    def build_circle(self, n: int):
        """构建包含n个节点的环形链表"""
        if n < 1:
            raise ValueError("人数必须大于0")
        
        # 创建首节点（编号1）
        self.head = Node(1)
        current = self.head
        
        # 批量添加后续节点
        for i in range(2, n+1):
            new_node = Node(i)
            current.next = new_node
            current = new_node
        
        # 闭合环形链表
        current.next = self.head
        return self.head

def josephus_simulation(n: int, k: int = 2, start: int = 1) -> int:
    """
    环形链表模拟约瑟夫过程
    :param n: 总人数
    :param k: 报数步长
    :param start: 起始编号
    :return: 幸存者编号
    """
    # 1. 构建环形链表
    clist = CircularLinkedList()
    head = clist.build_circle(n)
    
    # 2. 定位起始节点
    start_node = head
    for _ in range(1, start):
        start_node = start_node.next
    
    # 3. 初始化辅助指针（指向起始节点的前驱）
    prev = start_node
    while prev.next != start_node:
        prev = prev.next
    
    # 4. 模拟淘汰过程
    current = start_node
    while current.next != current:  # 当不止一人时继续
        # 报数k-1步
        for _ in range(k-1):
            prev = current
            current = current.next
        
        # 淘汰当前节点
        prev.next = current.next
        current.next = None
        print(f"淘汰 {current.no} 号")
        current = prev.next
    
    # 5. 返回幸存者
    print(f"幸存者: {current.no} 号")
    return current.no

def josephus_simulation_vector(n:int)->int:
    ''' 用list / vector 来模拟，下标取余实现循环效果
        list初始各元素的值为编号，从1到n,如果被杀，值修改为-1
    '''
    #初始化list
    List_n = []
    for i in range(1,n+1):
        List_n.append(i)
    iter = 0  # 从Index=0 也即1号玩家开始

    #寻找下一个存活者(的index)
    def findNext(List,idx,n)->int: # 长度为n的List(循环) idx指标下一个>0的元素的指标
        if List[idx] < 0:
            raise ValueError("idx位置的元素必须大于0")
        
        iter = (idx + 1)%n
        while List[iter] <0 :
            iter = (iter + 1)%n

        return iter%n
    
    while True:
        next = findNext(List_n,iter,n) #下一个受害者
        if(next == iter):
            break
        List_n[next] = -1
        iter = findNext(List_n, iter, n) # 下一个执行者
    
    return List_n[iter]


# 测试示例

n = 100
print(f"n= {n},结果:", josephus_simulation_vector(n))
# print("n=100, k=2 结果:", josephus_simulation(100))
# print("n=7, k=3 结果:", josephus_simulation(7, 3))