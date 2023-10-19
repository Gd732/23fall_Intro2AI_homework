class Node:
    def __init__(self, value = 0, is_max = True):
        self.value = value # 当前节点的值
        self.is_max = is_max # 当前节点属于max层还是min层
        self.childs = None # 当前节点的孩子
    
    def setChildLeaf(self, childs):
        is_MAX = not self.is_max
        tmp = []
        for child in childs:
            tmp.append(Node(value = child, is_max = is_MAX))
        self.childs = tmp
    
    def setChildNonLeaf(self, childs):
        if self.childs is None:
            self.childs = childs
            return
        else:
            for child in childs:
                self.childs.append(child)

# 输入为整棵树的根节点
def minimax(node):
    if node.childs is None:
        return node.value
    
    if node.is_max: # 若为max层, 则从其孩子节点中选取最大的节点
        best_value = -float('inf')
        for child in node.childs:
            best_value = max(best_value, minimax(child))
    else: # 若为min层, 则从其孩子节点中选取最小的节点
        best_value = float('inf')
        for child in node.childs:
            best_value = min(best_value, minimax(child))
    return best_value

def alpha_beta(node, alpha, beta):
    # min层修改beta,max层修改alpha
    # 若min层的子节点的值小于其beta, 则更新beta; 若max层的资质点的值大于其alpha, 则更新alpha
    # 若min层子节点的值大于其alpha, 则剪枝; 若max层子节点的值大于其beta,也剪枝
    if node.childs is None:
        return node.value
    if node.is_max:
        best_value = -float('inf')
        for child in node.childs:
            value = alpha_beta(child, alpha, beta)
            best_value = max(best_value, value)
            alpha = max(alpha, best_value)
            if alpha >= beta:
                break
    else:
        best_value = float('inf')
        for child in node.childs:
            value = alpha_beta(child, alpha, beta)
            best_value = min(best_value, value)
            beta = min(beta, best_value)
            if alpha >= beta:
                break
            
    return best_value

def init_tree():
    node21 = Node(is_max=True)
    node21.setChildLeaf([7, 6])
    node22 = Node(is_max=True)
    node22.setChildLeaf([8, 5])
    node23 = Node(is_max=True)
    node23.setChildLeaf([2, 3])
    node24 = Node(is_max=True)
    node24.setChildLeaf([0, -2])
    node25 = Node(is_max=True)
    node25.setChildLeaf([6, 2])
    node26 = Node(is_max=True)
    node26.setChildLeaf([5, 8])
    node27 = Node(is_max=True)
    node27.setChildLeaf([9, 2])
    node11 = Node(is_max=False)
    node11.setChildNonLeaf([node21, node22, node23])
    node12 = Node(is_max=False)
    node12.setChildNonLeaf([node24, node25])
    node13 = Node(is_max=False)
    node13.setChildNonLeaf([node26, node27])
    node0 = Node(is_max=True)
    node0.setChildNonLeaf([node11, node12, node13])
    return node0

if __name__ == '__main__':
    node0 = init_tree()
    print("minimax方法找到的最优值为", minimax(node0))
    print("alpha-beta剪枝方法找到的最优值为", alpha_beta(node0, -float('inf'), float('inf')))
    

