def match(re, text):
    """
    匹配'.'和'*'的正则表达式(字符串所有字符匹配整个模式)
    返回：
        bool:True or False
    """
    def match_here(re, i, text, j):
        """检查从text[j]开始的正文是否与re[i]开始的模式匹配"""
        while True:
            if i == rlen:
                return True
            if i + 1 < rlen and re[i+1] == '*':
                return match_star(re[i], re, i+2, text, j)
            if j == tlen or (re[i] != '.' and re[i] != text[j]):
                return False
            i, j = i+1, j+1

    def match_star(c, re, i, text, j):
        """在text里跳过0个或多个c后检查匹配"""
        for n in range(j, tlen):
            if match_here(re, i, text, n):
                return True

            if text[n] != c and c != '.':
                break
        return False

    rlen, tlen = len(re), len(text)
    return True if match_here(re, 0, text, 0) else False

    """查找文本中匹配模式的字符，re.search(pattern, text)"""
    #for n in range(tlen):
    #   if match_here(re, 0, text, n):
    #        return text[n:]
    
    #return False

if __name__ == "__main__":
    re_1 = r'aa.a'
    re_2 = r'a.a'
    text = 'aaa'
    print(match(re_1, text))
    print(match(re_2, text))

    import re
    print(re.match(r'a.a', text))