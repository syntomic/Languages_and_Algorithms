def print_probability_recursive(n):
    """
    把n个骰子扔在地上，所有骰子朝上一面的点数之和为s
    打印出s的所有可能出现的值的概率
    递归方法
    """
    if n < 1:
        return

    max_sum = n * 6
    prob = [0] * (max_sum - n + 1)

    def probability(n, prob):
        """每个和出现的次数"""
        for i in range(1, 7):
            probability_core(n, n, i, prob)


    def probability_core(origin, current, sum_, prob):
        """
        将n个骰子分成1和n-1两部分，递归计算和出现次数
        参数：
            origin:int 总共的骰子数
            current:int 当前的骰子数
            sum_:int 余下的骰子和
            prob:list[int] 每个和出现的次数
        """
        if current == 1:
            prob[sum_ - origin] += 1
        else: 
            for i in range(1, 7):
                probability_core(origin, current-1, i+sum_, prob)

    probability(n, prob)

    total = pow(6, n)

    for i in range(n, max_sum+1):
        ratio = prob[i - n] / total
        print("和为%d的概率为%.5f" % (i, ratio))
    

def print_probability_circle(n):
    """循环方法"""
    if  n < 1:
        return

    prob = []
    prob.append([0]*(6*n+1))
    prob.append([0]*(6*n+1))
    
    flag = 0

    for i in range(1,7):
        prob[flag][i]=1 
    
    for k in range(2, n+1):
        # 最小和为k
        for i in range(k):
            prob[1-flag][i]=0

        for i in range(k, 6*k+1):
            prob[1-flag][i] = 0

            # 和为i的次数等于前一个数组和为i-1,i-2,i-3,i-4,i-5,i-6项的和
            for j in range(1, min(i+1,7)):
                prob[1-flag][i] += prob[flag][i-j]
                
        flag = 1-flag
        
    
    total = pow(6,n)

    for i in range(n, 6*n+1):

        ratio = prob[flag][i]/total
        print("和为%d的概率为%.5f" % (i, ratio))


if __name__ == "__main__":
    print_probability_circle(3)
    print_probability_recursive(3)
    

    