def mathcing_KMP(t, p, pnext):
    """KMP串匹配，主函数"""
    j, i = 0, 0
    n, m = len(t), len(p)
    while j < n and i < m:           # i == m 说明找到匹配
        if i == -1 or t[j] == p[i]:  # 考虑p中下一对字符
            j, i = j + 1, i + 1
        else:                        # 从pnext取得p的下一字符位置
            i = pnext[i]
    if i == m:                       # 找到匹配，返回其下标
        return j - i
    return -1

def gen_pnext(p):
    """生成针对p中各位置i的下一检查位置表，用于KMP算法"""
    i, k, m = 0, -1, len(p)
    pnext = [-1] * m
    while i < m - 1:                    # 生成下一个pnext元素值
        if k == -1 or p[i] == p[k]:
            i, k = i + 1, k + 1
            if p[i] == p[k]:
                pnext[i] = pnext[k]
            else:
                pnext[i] = k
        else:
            k = pnext[k]                 # 退回更短时间前缀
    return pnext

if __name__ == '__main__':
    p = 'abcac'
    pnext = gen_pnext(p)
    t = 'ababcabcacbab'
    print(pnext)
    print(mathcing_KMP(t, p, pnext))
