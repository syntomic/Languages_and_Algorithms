def permutation_of_string(string):
    """字符串的排列"""
    list_ = []

    if len(string) <= 1:
        return string

    for i in range(len(string)):
        for j in map(lambda x: string[i]+x, permutation_of_string(string[:i]+string[i+1:])):
            if j not in list_:
                list_.append(j)

    return list_
            

if __name__ == "__main__":
    string = "aab"
    print(permutation_of_string(string))