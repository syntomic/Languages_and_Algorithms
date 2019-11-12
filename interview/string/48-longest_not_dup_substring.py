from collections import Counter
Counter()

def length_of_longest_substring(s):
    """
    最长不含重复字符的子字符串
    :type s: str
    :rtype: int
    """
    start = 0
    max_length = 0
    used_char = {}
    len_ = len(s)

    for i in range(len_):
        if s[i] in used_char and start <= used_char[s[i]]:
            start = used_char[s[i]]+1
        else:
            max_length = max(max_length, i-start+1)

        used_char[s[i]]=i
    
    return max_length

def length_of_longest_substring_2(s):
    cur_len = 0
    max_len = 0
    len_ = len(s)

    position = [-1] * 26

    for i in range(len_):
        pre_index = position[ord(s[i]) - ord('a')]

        if pre_index < 0 or i - pre_index > cur_len:
            cur_len += 1
        else:
            if cur_len > max_len:
                max_len = cur_len

            cur_len = i - pre_index

        position[ord(s[i]) - ord('a')] = i

    if cur_len > max_len:
        max_len = cur_len

    return max_len      

if __name__=="__main__":
    print(length_of_longest_substring('arabcacfr'))
    print(length_of_longest_substring('abcabcbb'))
    print(length_of_longest_substring('bbbbb'))
    print(length_of_longest_substring('pwwkew'))
    print(length_of_longest_substring_2('arabcacfr'))
    print(length_of_longest_substring_2('abcabcbb'))
    print(length_of_longest_substring_2('bbbbb'))
    print(length_of_longest_substring_2('pwwkew'))