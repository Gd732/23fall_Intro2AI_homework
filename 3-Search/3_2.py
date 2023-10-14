import numpy as np

def judge_linked(x, y):
    xt = x; yt = y
    if x > y:
        xt = y; yt = x
    for idx in range(len(distance)):
        if distance[idx][0] == xt and distance[idx][1] == yt:
            return distance[idx][2]
    return None

def find_path(begin, target):
    prev_path_len = 0
    path = [begin]
    prev_node = {begin}
    while True:
        layer = []
        prices_g = []
        prices_h = []
        prices_f = []
        for node in range(1, 21):
            l = judge_linked(path[-1], node)
            if l and node not in prev_node:
                layer.append(node)
                prices_g.append(l)
                prices_h.append(h_dis[node]+prev_path_len)
                prices_f = list(np.array(prices_g) + np.array(prices_h))
        if target in layer:
            path.append(target)
            break
        idx_f_min = prices_f.index(min(prices_f))
        path.append(layer[idx_f_min])
        for i in range(len(layer)):
            prev_node.add(layer[i])
        prev_path_len += judge_linked(path[-2], path[-1])
        
    return path

def print_path(node_dict, path):
    for i in range(len(path)):
        print(node_dict[str(path[i])], end="")
        if i != len(path)-1:
            print("->", end="")
    print('\n', end="")


if __name__ == "__main__":
    # 共有20个城市, 以列表从上到下进行标号
    # 两地点之间的距离,共有22条连接线
    distance = []
    distance.append([1, 20, 75])
    distance.append([13, 20, 71])
    distance.append([13, 16, 151])
    distance.append([16, 20, 140])
    distance.append([1, 17, 118])
    distance.append([10, 17, 111])
    distance.append([10, 11, 70])
    distance.append([4, 11, 75])
    distance.append([3, 4, 120])
    distance.append([3, 15, 146])
    distance.append([3, 14, 138])
    distance.append([14, 15, 97])
    distance.append([15, 16, 80])
    distance.append([6, 16, 99])
    distance.append([6, 2, 211])
    distance.append([2, 14, 101])
    distance.append([2, 7, 90])
    distance.append([2, 18, 85])
    distance.append([8, 18, 98])
    distance.append([5, 8, 86])
    distance.append([18, 19, 142])
    distance.append([9, 19, 92])
    distance.append([9, 12, 87])

    h_dis = np.array([0, 366, 0, 160, 242, 161, 176, 77, 151, 
                    226, 244, 241, 234, 380, 100, 193, 253, 
                    329, 80, 199, 374])
    NodeName = {"1":"Arad", "2":"Bucharest", "3":"Craiova", 
                "4":"Drobeta", "5":"Eforie", "6":"Fagaras", 
                "7":"Giurgiu", "8":"Hirsova", "9":"Lasi", 
                "10":"Lugoj", "11":"Mehadia", "12":"Neamt", 
                "13":"Oradea", "14":"Pitesti", "15":"Rimnicu Vilcea", 
                "16":"Sibiu", "17":"Timisoara", "18":"Urziceni", 
                "19":"Vaslui", "20":"Zerind"}
    path = find_path(10, 2)
    print_path(NodeName, path)


