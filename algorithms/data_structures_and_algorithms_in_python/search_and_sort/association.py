class Assoc:
    """关联类"""
    def __init__(self, key, value):
        self.key = key
        self.value = value
    
    def __lt__(self, other):        # 有些操作可能需要考虑序
        return self.key < other.key

    def __le__(self, other):
        return self.key <= other.key
    
    def __str__(self):              # 定义字符串表示形式便于输出和交互
        return "Assoc({},{})".format(self.key, self.value)
