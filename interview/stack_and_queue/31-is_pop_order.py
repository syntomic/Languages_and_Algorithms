def is_pop_order(push, pop):
    if push == [] or pop == []:
        return False
    
    stack = []

    for i in push:
        stack.append(i)

        while len(stack) and stack[-1] == pop[0]:
            stack.pop()
            pop.pop(0)
        
    if len(stack): 
        return False
    else:
        return True
            
if __name__ == "__main__":
    push = [1, 2, 3, 4, 5]
    pop_1 = [4, 5, 3, 2, 1]
    pop_2 = [4, 3, 5, 1, 2]
    print(is_pop_order(push, pop_1))
    print(is_pop_order(push, pop_2))