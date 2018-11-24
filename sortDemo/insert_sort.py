# 直接插入排序
def insert_sort(alist):
    #从第二个位置，即下标为1的元素开始向前插入
    for i in range(1,len(alist)):
        # 从第i个元素开始向前比较，如果小于前一个元素，则交换位置
        for j in range(i,0,-1):
            if alist[j] < alist[j-1]:
                alist[j],alist[j-1] = alist[j-1],alist[j]


# 折半插入排序
def insert_sort2(alist):
    #从第二个位置，即下标为1的元素开始排序
    for i in range(1,len(alist)):
        low = 0
        high = i-1
        while low <= high:
            # 折半查找
            m = int((low+high)/2)
            # 插入点在高半区
            if alist[m] <= alist[i]:
                low = m+1
            else:
                #插入点在低半区
                high = m-1
        for j in range(i,high+1,-1):
            if alist[j] < alist[j-1]:
                alist[j], alist[j - 1] = alist[j - 1], alist[j]


# 2-路插入排序
def insert_sort3(alist):
    blist = [0]*len(alist)
    first = last = 0
    blist[0] = alist[0] #先确定第一个位置，并以此为判断依据
    n = len(alist)
    for i in range(1,n): #  从第二个数开始插入排序
        if alist[i] < blist[first]:#如果待插数字比尾部数字还大，则插在尾部的
            first = (first-1+n) % n #数字后面，并把尾部指针向后移动一位
            blist[first] = alist[i]
        elif alist[i] >  blist[last]:#如果待插数字比头部数字还小，则插在头部的
            last = (last+1+n)%n      #数字后面，并把头部指针向前移动一位
            blist[last] = alist[i]
        elif blist[0] <= alist[i]:   # 如果比头部数字大，比尾部数字小 则比较该数字是否比辅助数组的第一个数大
            k = (last+1+n)%n         # 如果大的话，从final_num往前找，找到位置后插进去，否则与上述步骤相反
            while blist[(k-1+n)%n] > alist[i]:
                blist[(k+n)%n] = blist[(k-1+n)%n]
                k = (k-1+n)%n
            blist[(k+n)%n] = alist[i]
            last = (last+1+n)%n
        else:
          k = (first-1+n)%n
          while alist[i] > blist[(k+1+n)%n]:
              blist[(k+n)%n] = blist[(k+1+n)%n]
              k = (k+1+n)%n
          blist[(k+n)%n] = alist[i]
          first = (first-1+n)%n

    for i in range(0,len(alist)):# 根据辅助数组确定新序列
        alist[i] = blist[(i+first)%len(alist)]


# 希尔排序
def shell_sort(alist):
    n = len(alist)
    # 初始步长
    gap = int(n / 2)
    while gap > 0:
        # 按步长进行插入排序
        for i in range(gap, n):
            j = i
            # 插入排序
            while j>=gap and alist[j-gap] > alist[j]:
                alist[j-gap], alist[j] = alist[j], alist[j-gap]
                j -= gap
        # 得到新的步长
        gap = int(gap / 2)

alist = [54,232,23,50,86,26,37]
# insert_sort3(alist)
shell_sort(alist)
print(alist)








