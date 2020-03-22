def reverseString(s):
    n = len(s)
    for i in range(0, n):
        s.insert(i, s[-1])
        s.pop()
    print(s)

def letterCombination(digits):
    
    def helper(digits, list_combi):
        
        letters = [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i'], \
            ['j', 'k', 'l'], ['m', 'n', 'o'], ['p', 'q', 'r', 's'], \
            ['t', 'u', 'v'], ['w', 'x', 'y', 'z']]
        if (digits == ''):
            return (digits, list_combi)

        if (digits[-1] == '7' or digits[-1] == '9'):
            multi = 4
        else:
            multi = 3
        l = len(list_combi)
        list_combi = multi * list_combi
        k = 0
        for j in range(0, multi):
            for i in range(0, l):
                list_combi[k] = letters[int(digits[-1]) - 2][j % multi] + list_combi[k]
                k = k + 1
        if (len(digits) > 0):
            digits = digits[:-1]
        (digits, list_combi) = helper(digits, list_combi)
        return (digits, list_combi)

    return helper(digits, [''])[1]
