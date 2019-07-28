def max_in_windows(num, size):
    if not num or size <= 0:
        return []

    res = []

    if len(num) >= size and size >= 1:
        deque=[]

        for i in range(size):
            while deque and num[i] >= num[deque[-1]]:
                deque.pop()
            deque.append(i)
        
        for i in range(size,len(num)):
            res.append(num[deque[0]])

            while (deque and num[i] >= num[deque[-1]]):
                deque.pop()

            if deque and deque[0]<=i-size:
                deque.pop(0)

            deque.append(i)

        res.append(num[deque[0]])

    return res

if __name__ == "__main__":
    nums = [2, 3, 4, 2, 6, 2, 5, 1]
    size = 3
    print(max_in_windows(nums, size))