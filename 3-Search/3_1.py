import numpy as np

# 倒满A-7L
def func1(AB):
    a = AB[0]; b = AB[1]
    if a < 7:
        a = 7
    else:
        # print('Wrong Input for func1')
        return None, None
    return np.array([a, b]), 1
# 倒满B-5L
def func2(AB):
    a = AB[0]; b = AB[1]
    if b < 5:
        b = 5
    else:
        # print('Wrong Input for func2')
        return None, None
    return np.array([a, b]), 2
# 倒空A-7L
def func3(AB):
    a = AB[0]; b = AB[1]
    if a > 0:
        a = 0
    else:
        # print('Wrong Input for func3')
        return None, None
    return np.array([a, b]), 3
# 倒空B-5L
def func4(AB):
    a = AB[0]; b = AB[1]
    if b > 0:
        b = 0
    else:
        # print('Wrong Input for func4')
        return None, None
    return np.array([a, b]), 4
# A倒入B
def func5(AB):
    a = AB[0]; b = AB[1]
    if a > 0 and b < 5:
        d = 5 - b
        if a <= d:
            b = b + a; a = 0
        elif a > d:
            a = a - d; b = b + d
    else:
        # print('Wrong Input for func5')
        return None, None
    return np.array([a, b]), 5
# B倒入A
def func6(AB):
    a = AB[0]; b = AB[1]
    if a < 7 and b > 0:
        d = 7 - a
        if b <= d:
            a = a + b; b = 0
        elif b > d:
            b = b - d; a = a + d
    else:
        # print('Wrong Input for func6')
        return None, None
    return np.array([a, b]), 6

def main():
    funcs = list((func1, func2, func3, func4, func5, func6))

    AB = np.array([0, 0])
    tree_layers = [[AB]] # 存储树
    tree_opt_layers = [[0]] # 操作树
    prev_node = {((0, 0))} # 存储已经出现过的节点类型
    layer_num = 0 
    while True:
        break_flag = False
        layer = []; opt_layer = []
        node_num = len(tree_layers[-1])
        for nodes in range(node_num):
            for idx in range(len(funcs)):
                AB_tmp, ftype = funcs[idx](tree_layers[layer_num][nodes])
                if AB_tmp is not None:
                    if tuple(AB_tmp) not in prev_node:
                        layer.append(AB_tmp)
                        opt_layer.append(ftype)
                    prev_node.add(tuple(AB_tmp))
                    if AB_tmp[0] == 4 or AB_tmp[1] == 4:
                        break_flag = True
        tree_layers.append(layer)
        tree_opt_layers.append(opt_layer)
        layer_num += 1
        if break_flag == True:
            break
    print("历经的各层节点为:", tree_layers)
    print("历经的各层节点所对应的上一步操作为:", tree_opt_layers)
    print("树的深度为", len(tree_layers))
    
if __name__ == "__main__":
    main()