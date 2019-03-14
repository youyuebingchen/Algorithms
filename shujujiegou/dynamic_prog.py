import numpy as np

# 动态规划算法的核心是记住已经求过的解，记住求解的方式有两种：①自顶向下的备忘录法 ②自底向上。
# 递归方法
def fib(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    else:
        return fib(n-2)+fib(n-1)

class Dp1(object):  # 动态规划类
    def __init__(self, n):  # 初始化
        self.mark = [0 for _ in range(n + 1)]  # 定义一个一维数组，初始化全部为0，长度为台阶数。用来当作“备忘录”。
        print(self.dp(n))  # 开始递归

    def dp(self, n):  # 递归的方法
        self.m = 0  # m的含义是当前n个台阶有m种跳法
        if self.mark[n] != 0:  # 先从备忘录寻找n，若存在mark[n]不等于0,则代表曾经计算过，n个台阶有mark[n]种跳法
            self.m = self.mark[n]  # 若备忘录有，则直接得到n层台阶的答案
        elif n <= 0:  # 从这里开始的四行是用来判断“边界问题”
            if n == 0:  # 若刚好跳完台阶，则这样算一种方法
                self.m = 1  # m变成1,代表是一种可行方法
            else:  # 有可能跳的台阶超过实际台阶数
                self.m = 0  # m为0,代表不可行
        elif n > 0:  # 这里两行是用于规划转移方程式（其实这里很简单），青蛙只有两种可能，跳一层或者跳两层。
            self.m = self.dp(n-2) + self.dp(n - 1)  # 当前n层台阶的解个数 等于 n-1层台阶的解 + n-2层台阶的解
        self.mark[n] = self.m  # 把m放入备忘录，下次若是再次是n层台阶，则不用计算直接取备忘录的数。（优化）
        print(self.mark)
        return self.m  # 返回

def solve(vlist,wlist,totalWeight,totalLength):
    resArr = np.zeros((totalLength+1,totalWeight+1),dtype=np.int32)
    for i in range(1,totalLength+1):
        for j in range(1,totalWeight+1):
            if wlist[i] <= j:
                resArr[i,j] = max(resArr[i-1,j-wlist[i]]+vlist[i],resArr[i-1,j])
            else:
                resArr[i,j] = resArr[i-1,j]
    return resArr[-1,-1]



def fib_up_to_low(n):
    meno = [0 for i in range(n+1)]
    m = 0
    if meno[n] != 0:
        m =meno[n]
    elif n <= 0:
        if n == 0:
            m = 1
        else:
            m = 0
    elif n >0:
        m = fib_up_to_low(n-2) + fib_up_to_low(n-1)
    meno[n] =  m
    return m
# if __name__ == '__main__':
#     # for i in range(0,10):
#     #     print(i,fib_up_to_low(10))
#     arr = np.zeros((3,4))
#     print(arr)

def solve2(vlist,wlist,totalWeight,totalLength):
    resArr = np.zeros((totalWeight)+1,dtype=np.int32)
    for i in range(1,totalLength+1):
        for j in range(totalWeight,0,-1):
            if wlist[i] <= j:
                resArr[j] = max(resArr[j],resArr[j-wlist[i]]+vlist[i])
    return resArr


# 动态规划
def max_sublist(alist):
    maxlist = []
    max = 0
    n = len(alist)+1
    for i in range(0,n):
        for j in range(i,n):
            sonlist = alist[i:j]
            sum1 = sum(sonlist)
            if sum1 >= max:
                max  = sum1
                maxlist = sonlist
    return max,maxlist

# 贪心算法

def max_sublist_tanxin(alist):
    max = 0
    max_list = []
    sum = 0
    n = len(alist)
    min_index = 0
    for i in range(n):
        sum += alist[i]
        if sum > max:
            max = sum
            max_index = i+1 # 此处i + 1是因为切片是左闭右开的
        if sum < 0:
            sum = 0
            min_index = i+1  # 此处 i+1是从下一个开始算最小值开始指标
    return max,alist[min_index:max_index]

def min_sublist_tanxin(alist):
    min_index = 0
    max_index = 0
    sum = 0
    min = 0
    n = len(alist)
    for i in range(n):
        sum += alist[i]
        if sum < min:
            min = sum
            max_index = i + 1
        if sum >0:
            sum  = 0
            min_index = i + 1
    return min,alist[min_index:max_index]

def max_are(alist):
    min_index = 0
    max_index = 0
    are = 0
    max_are = 0
    n = len(alist)
    for i in range(n):
        max_index = i + 1

        are = (max_index-min_index) *min(alist[min_index:max_index-1])
        if are >= max_are:
            max_are = are
        else:
            min_index += 1

if __name__ == '__main__':
    # v = [0,60,100,120]
    # w = [0,1,2,3]
    # weight = 5
    # n = 3
    # result = solve2(v,w,weight,n)
    # print(result)
    a = [2,-3,2,-2,2,1]
    min,list= min_sublist_tanxin(a)
    print(min,list)