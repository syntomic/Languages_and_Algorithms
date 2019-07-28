from collections import Counter

def first_not_repeating(string):
    """第一次只出现一次的字符"""
    count = Counter(string)
    for i in count.keys():
        if count[i] == 1:
            return i
## hash表
if __name__ == "__main__":
    string = "abaccdeff"
    print(first_not_repeating(string))