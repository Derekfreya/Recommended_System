import numpy as np
import networkx as nx

class Derek_Rank():
    def __init__(self):
        self.m, self.w = self.matrix()
        self.Iter100_Rank()
        self.While_Rank()
        self.Nw_Rank()

    # 计算转移矩阵m及权重w
    def matrix(self):
        m = np.zeros((len(node), len(node)))
        w = np.array([1 / len(node)] * len(node)).reshape(len(node), 1)
        for n in node:
            col = node.index(n)
            l = [x for x in edge if x[0] == n]
            for e in l:
                row = node.index(e[1])
                m[row, col] += 1 / len(l)
        return m, w

    # 迭代100次后的排序
    def Iter100_Rank(self, d = 0.85):
        a, b = self.w, self.w
        for x in range(100):
            Simple_w = np.dot(self.m, a)
            Random_w = (1 - d) / len(node) + np.dot(self.m, b)
            a, b = Simple_w, Random_w
        Simple_dict, Random_dict = {}, {}
        for i in range(len(node)):
            Simple_dict[node[i]], Random_dict[node[i]] = Simple_w[i, 0], Random_w[i, 0]
        print('迭代100次的Simple算法PR值及排序为:', sorted(Simple_dict.items(), key = lambda x : x[1], reverse = True))
        print('\n迭代100次的Random算法PR值及排序为:', sorted(Random_dict.items(), key = lambda x : x[1], reverse = True))

    # 根据迭代差异值v，终止迭代次数后计算结果
    def While_Rank(self, d = 0.85, v = 0.00001):
        n = 0
        m = 0
        a, b = self.w, self.w
        while True:
            Simple_w = np.dot(self.m, a)
            n += 1
            if abs(Simple_w[0, 0] - a[0, 0]) < v:
                break
            a = Simple_w
        while True:
            Random_w = (1 - d) / len(node) + np.dot(self.m, b)
            m += 1
            if abs(Random_w[0, 0] - b[0, 0]) < v:
                break
            b = Random_w
        Simple_dict, Random_dict = {}, {}
        for i in range(len(node)):
            Simple_dict[node[i]], Random_dict[node[i]] = Simple_w[i, 0], Random_w[i, 0]
        print('\n迭代%s次的Simple算法的PR值及排序为:' % n, sorted(Simple_dict.items(), key = lambda x : x[1], reverse = True))
        print('\n迭代%s次的Simple算法的PR值及排序为:' % n, sorted(Random_dict.items(), key = lambda x : x[1], reverse = True))

    #使用nx工具包计算结果
    def Nw_Rank(self):
        G = nx.DiGraph()
        for e in edge:
            G.add_edge(e[0], e[1])
        simple = nx.pagerank(G, alpha = 1)
        random = nx.pagerank(G, alpha = 0.85)
        print('\n工具包Simple算法PR值及排序是:', sorted(simple.items(), key = lambda x : x[1], reverse = True))
        print('\n工具包Random算法PR值及排序是:', sorted(random.items(), key = lambda x : x[1], reverse = True))

if __name__ == "__main__":
    node = ['A', 'B', 'C', 'D', 'E', 'F']
    edge = [('A', 'B'), ('A', 'D'), ('A', 'E'), ('A', 'F'), ('B', 'C'), ('C', 'E'), ('D', 'A'), ('D', 'C'), ('D', 'E'), ('E', 'B'), ('E', 'C'), ('F', 'D')]
    dr = Derek_Rank()
