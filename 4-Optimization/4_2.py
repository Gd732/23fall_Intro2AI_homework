import numpy as np

# 令A~E的标号为1~5
linked_A = [2, 3, 4]
linked_B = [1, 5]
linked_C = [1, 4, 5]
linked_D = [1, 3, 5]
linked_E = [2, 3, 4]
linked_list = list((linked_A, linked_B, linked_C, linked_D, linked_E))

distance = []
distance.append([1, 2, 20])
distance.append([1, 3, 10])
distance.append([1, 4, 15])
distance.append([2, 5, 30])
distance.append([3, 4, 25])
distance.append([3, 5, 5])
distance.append([4, 5, 40])

def innerSort(state):
    sorted_state = state
    for i in range(len(state)):
        sorted_state[i]=np.array((min(state[i]), max(state[i])))
    return sorted_state

def calPrice(state):
    price = 0
    for i in range(len(state)):
        for j in range(len(distance)):
            if list(state[i]) == list(distance[j][:2]):
                price += distance[j][2]
    return price

def find_path(ini_state, searched_node, state_rec, price_rec, tabu_list):
    for idx in range(len(ini_state)):
            for n in range(2):
                # print("----")
                cur_node = ini_state[idx][n]
                # print(linked_list[cur_node-1])
                if cur_node in searched_node:
                    pass
                else:
                    searched_node.append(cur_node)
                    for i in range(len(linked_list[cur_node-1])):
                        cur_state = np.copy(ini_state)
                        cur_state[idx][n^1] = linked_list[cur_node-1][i]
                        cur_state = innerSort(cur_state)
                        if not np.array_equal(cur_state, ini_state):
                            _, counts = np.unique(cur_state, axis=0, return_index=False, return_counts=True)
                            # print("count=", counts)
                            if np.array_equal(counts, np.ones(len(cur_state))):
                                state_rec.append(cur_state)
                                # print("cur", cur_state)
                                price_rec.append(calPrice(cur_state))
                                # print(calPrice(cur_state))
    min_price = min(price_rec)
    min_price_idx = price_rec.index(min(price_rec))
    min_price_path = state_rec[min_price_idx]
    
    tabu_list.append((min_price, min_price_path))


if __name__ == "__main__":
    ini_state = np.array(([1, 3], [3, 4], [3, 5], [2, 5]))
    ini_state = innerSort(ini_state)
    ini_price = calPrice(ini_state)


    searched_node = []
    price_rec = []
    state_rec = []
    tabu_list = []
    tabu_duration = 3 # 禁忌时长设置为3
    lowest_price = 0
    find_path(ini_state, searched_node, state_rec, price_rec, tabu_list)

    while True:
        min_price = min(price_rec)
        min_price_idx = price_rec.index(min(price_rec))
        min_price_path = state_rec[min_price_idx]
        ini_state = state_rec[min_price_idx]
        ini_state = innerSort(ini_state)
        ini_price = calPrice(ini_state)
        
        searched_node = []
        price_rec = []
        state_rec = []
        find_path(ini_state, searched_node, state_rec, price_rec, tabu_list)
        if tabu_list[-1][0] >= min_price and min_price_idx+tabu_duration<len(tabu_list):
            print("min_price = ", min_price)
            print("min_path = \n", min_price_path)
            break


