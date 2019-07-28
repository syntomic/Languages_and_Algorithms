from SStack import SStack # pylint: disable=import-error

def check_parens(text):
    """括号配对检查函数，text是被检查的正文串"""
    parens = "()[]{}"
    open_parens = "([{"
    opposite = {")" : "(", "]" : "[", "}" : "{"} # 表示配对关系的字典
 
    def parentheses(text):
        """括号生成器，每次调用返回text里的下一括号及其位置"""
        i, text_len = 0, len(text)
        while True:
            while i < text_len and text[i] not in parens:
                i += 1
            if i >=text_len:
                return
            yield text[i], i
            i += 1

    st = SStack() # 保存括号的栈

    for pr, i in parentheses(text):
        if pr in open_parens:
            st.push(pr)
        elif st.pop() != opposite[pr]:
            print("Unmatching is found at", i, "for", pr)
            return False
    
    if not st.is_empty():
        while not st.is_empty():
            print("Unmatching for " + st.pop())
        
        return False

    print("All parentheses are correctly matched")
    return True

if __name__ == "__main__":
    print(check_parens("a[{(b)"))


