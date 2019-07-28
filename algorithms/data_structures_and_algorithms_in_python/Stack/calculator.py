from SStack import SStack # pylint: disable=import-error


class ESStack(SStack):
    """扩充的栈类，增加一个检查深度的方法"""
    def depth(self):
        return len(self._elems)

    
def suf_exp_evaluator(exp):
    """后缀表达式求值"""
    operators = "+-*/"
    st = ESStack()

    for x in exp:
        if x not in operators:
            st.push(float(x))
            continue

        if st.depth() < 2: # x必为运算符，栈元素不够时引发异常
            raise SyntaxError("Short of oprand(s).")
        a = st.pop()
        b = st.pop()

        if x == "+":
            c = b + a
        elif x == "-":
            c = b - a
        elif x == "/":
            c = b / a
        elif x == "*":
            c = b * a
        else:
            break

        st.push(c)

    if st.depth() == 1:
        return st.pop()
    raise SyntaxError("Extra operand(s).")

def suffix_exp_evaluator(line):
    return suf_exp_evaluator(line.split())

def suffix_exp_calculator():
    """方便用户使用，交互式驱动函数"""
    while True:
        try:
            line = input("Suffix Expression: ")
            if line == "end": return
            res = suffix_exp_evaluator(line)
            print(res)
        except Exception as ex:
            print("Error:", type(ex), ex.args)

# 中缀表达式求值可以先转化为后缀表达
# 或者采用两个栈运算

if __name__ == "__main__":
    suffix_exp_calculator()
    # 3 5 - 6 17 4 * + * 3 /