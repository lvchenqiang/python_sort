
##败者树实现内部归并
a0 = [10,15,16]
a1 = [9,18,20]
a2 = [20,22,40]
a3 = [6,15,25]
a4 = [12,37,48]


def merging_sorting(data):  # 生成一个归并序列，把每一路中的元素挨个排入compare数组中
    k = len(data)
    compare = []
    for i in range(0, k):
        compare.append(data[i][0])
        #data[i].remove(data[i][0])
    # print(compare)

    def adjust(loserTree, dataArray, n, s):  # 败者树的核心代码
        t = int((s + n) / 2)
        while t > 0:  # 从败者树的尾部开始进行比较
            if dataArray[s] > dataArray[loserTree[t]]:  # 和败者结点比较
                s, loserTree[t] = loserTree[t], s  # 如果比某个败者结点大，说明该结点失败了，将s结点存入败者树，把败者树的现在的胜结点拿去和其父节点比较。
            t = int(t/2)
        loserTree[0] = s

    def createLoserTree(loserTree, dataArray, n):
        for i in range(n):
            loserTree.append(0)
            dataArray.append(i-n)  # 这里是为了生成败者树用的，

        for i in range(n):
            adjust(loserTree, dataArray, n, n-1-i)

    loserTree = []
    dataArray = []
    createLoserTree(loserTree, dataArray, k)

    for i in range(k):
        dataArray[i] = compare[i]  # 将数据替换成待排数据
        adjust(loserTree, dataArray, k, i)  # 此步执行完毕，败者树才完全创建初始化完毕，正式开始排序归并

    result = []
    while True:
        if data[loserTree[0]][0] > 9999:
            break
        result.append(data[loserTree[0]][0])  # 添加到 result 中，这是我们需要的结果
        data[loserTree[0]].remove(data[loserTree[0]][0])  # 从data 中删除头一个元素
        if data[loserTree[0]] == []:
            data[loserTree[0]].append(10000)
        compare[loserTree[0]] = data[loserTree[0]][0]  # 将下一个元素添加到 compare数组中
        adjust(loserTree, compare, k, loserTree[0])

    return result


print(merging_sorting([a0,a1,a2,a3,a4]))
