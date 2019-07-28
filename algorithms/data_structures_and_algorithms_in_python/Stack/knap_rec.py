def knap_rec(weight, wlist, n):
    """简单背包问题"""
    if weight == 0:
        return True
    if weight < 0 or (weight > 0 and n < 1):
        return False
    if knap_rec(weight - wlist[n-1], wlist, n-1):
        print("Item" + str(n) + ":", wlist[n-1])
        return True
    if knap_rec(weight, wlist, n-1):
        return True
    else: return False

if __name__ == "__main__":
    knap_rec(10, [1,2,3,5,4], 4)