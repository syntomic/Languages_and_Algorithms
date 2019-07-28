from LCList import LCList # pylint: disable=import-error

"""
假设n个人围坐一圈，从第k个人开始报数，报到第m个数的人退出。
然后从下一个人开始继续报数并按同样规则推出，直到所有人退出
按顺序输出各出列人的编号
"""

# 基于数组概念的解法
def josephus_A(n, k, m):
    people = list(range(1, n+1))

    i = k-1
    for num in range(n):
        count = 0
        while count < m:
            if people[i] > 0:
                count += 1
            if count == m:
                print(people[i], end="")
                people[i] = 0
            i = (i+1) % n
        if num < n-1:
            print(", ", end="")
        else:
            print("")
    return
# if m=1, then O(n), if m=n, then O(n^2logn)

# 基于顺序表的解
def josephus_L(n, k, m):
    people = list(range(1, n+1))

    num, i = n, k-1
    for num in range(n, 0, -1):
        i = (i + m-1) % num
        print(people.pop(i), end=(", " if num > 1 else "\n"))
    return
# O(n^2)

# 基于循环单链表的解
class Josephus(LCList):
    def turn(self, m):
        for i in range(m):
            self._rear = self._rear.next

    def __init__(self, n, k, m):
        LCList.__init__(self)
        for i in range(n):
            self.append(i+1)
        self.turn(k-1)
        while not self.is_empty():
            self.turn(m-1)
            print(self.pop(),
                  end = ("\n" if self.is_empty() else ", "))
#O(m*n)

if __name__ == "__main__":
    josephus_A(10, 2, 7)
    josephus_L(10, 2, 7)
    Josephus(10, 2, 7)