"""
集合的线性表实现
以及散列表实现
"""


## 集合s和t的交r，s,t元素从小到大
r = []
i = 0
j = 0
while i < len(s) and j < len(t):
    if s[i] < t[j]:
        i += 1
    elif t[j] < s[i]:
        j += 1
    else:
        r.append(s[i])
        i += 1
        j += 1
