def reverse_sentence(s):
    """翻转单词顺序"""
    temp = s.split()

    if len(temp) == 0:
        return s
        
    return ' '.join(temp[::-1])

def left_rotate_string(s, n):
    """左旋转字符串"""
    if s is None:
        return

    if s==' ':
        return s

    if len(s)<=n:
        return s

    return s[n:]+s[:n]

if __name__ == "__main__":
    s = 'I am a student'
    print(reverse_sentence(s))

    s_1 = "abcdefg"
    print(left_rotate_string(s_1, 2))