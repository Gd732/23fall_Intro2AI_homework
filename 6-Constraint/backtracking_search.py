s1 = 'SEND'
s2 = 'MORE'
s3 = 'MONEY'

# 将两个字符串进行相加
def add(a1, a2):
    l = len(a1)
    result = [None] * l
    carry = 0
    # 从末位开始加起
    for i in reversed(range(l)):
        if a1[i] is None or a2[i] is None:
            carry = 0
            continue
        result[i] = a1[i] + a2[i] + carry
        if result[i] >= 10:
            result[i] -= 10
            carry = 1
        else:
            carry = 0
    if a1[0] is None or a2[0] is None:
        return [None] + result
    return [carry] + result

# 根据mapping给定的映射，将当前字符串内的字母换成数字
def replace(string, mapping):
    return [mapping.get(string[i], None) for i in range(len(string))]
def matches(result1, result2):
    for i, v1 in enumerate(result1):
        v2 = result2[i]
        # result1和result2不匹配
        if v2 != v1 and v2 is not None and v1 is not None and \
            not(i+1 < len(result2) and result2[i+1] is None and v1 == v2 + 1):
                return False
    return True

# 计算某字符在当前的mapping下可能取值的总数
def value_count(mapping, c):
    m = dict(mapping)
    count = 0
    for i in get_possible_values(mapping):
        m[c] = i
        if is_valid(m):
            count += 1
    return count

# 在当前mapping下，选择可能选项最少的字符
def get_variable_with_least_choices(mapping):
    min_count = 10000
    result = None
    for c in chars:
        if c not in mapping:
            count = value_count(mapping, c)
            if count < min_count:
                min_count = count
                result = c
    return result

def get_possible_values(mapping):
    vals = [mapping[key] for key in mapping]
    for i in range(10):
        if i not in vals:
            yield i
            
def is_valid(mapping):
    if mapping.get(s3[0], None) == 0:
        return False
    summ = add(replace(s1, mapping), replace(s2, mapping))
    return matches(replace(s3, mapping), summ)

# 返回按评价函数h得到的得分降序排列
def get_best_ordering(mapping, c):
    # 评价函数——返回该字符当前取值下，下一步选择字符的取值个数
    def h(i):
        m = dict(mapping)
        m[c] = i
        return value_count(m, get_variable_with_least_choices(m))
    ordering = list(get_possible_values(mapping))
    ordering.sort(key=h)
    return reversed(ordering)

def solver(mapping):
    if not is_valid(mapping):
        return False
    print(mapping)

    mapping = dict(mapping)
    if len(mapping) == len(chars):
        print(mapping)
        exit()
    c = get_variable_with_least_choices(mapping)
    for i in get_best_ordering(mapping, c):
        mapping[c] = i
        solver(mapping)

if __name__ == "__main__":
    chars = list(set(s1+s2+s3))
    print("字母为：", chars)
    print(solver({}))