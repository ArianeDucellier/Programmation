import numpy as np

def DFS(adj):
    """
    adj = square matrix (2D-numpy array)
    """
    N = np.shape(adj)[0]
    for i in range(0, N):
        for j in range(0, N):
            if adj[i, j] == 1:
                start = i
                break
    stack = [start]
    result = [start]
    adj[start, start] = 0
    while len(stack) > 0:
        last = stack[-1]
        neighbors = False
        for i in range(0, N):
            if adj[last, i] == 1:
                stack.append(i)
                if (i not in result):
                    result.append(i)
                adj[last, i] = 0
                adj[i, last] = 0
                adj[i, i] = 0
                neighbors = True
                break
        if neighbors == False:
            stack.pop()
    return result

class Solution:

    def numIslands(self, grid):
        """
        """
        if len(grid) == 0:
            return 0
        grid = np.array(grid)
        number = np.zeros((np.shape(grid)[0], np.shape(grid)[1]))
        for i in range(0, np.shape(grid)[0]):
            for j in range(0, np.shape(grid)[1]):
                if grid[i, j] == '0':
                    number[i, j] = 0
                else:
                    nb_islands = np.max(np.max(number))
                    if i == 0:
                        top = '0'
                    else:
                        top = grid[i - 1, j]
                        if top != '0':
                            number[i, j] = number[i - 1, j]
                    if j == 0:
                        left = '0'
                    else:
                        left = grid[i, j - 1]
                        if left != '0':
                            number[i, j] = number[i, j - 1]
                    if (top == '0') and (left == '0'):
                        number[i, j] = nb_islands + 1
        print(number)
        return int(np.max(np.max(number)))

def test_numIslands():
    """
    """
    s = Solution()
#    grid = [
#    ["1","1","1","1","0"],
#    ["1","1","0","1","0"],
#    ["1","1","0","0","0"],
#    ["0","0","0","0","0"]
#    ]
#    result = s.numIslands(grid)
#    print('First grid')
#    print(result)
#    print('\n')
#    grid = [
#    ["1","1","0","0","0"],
#    ["1","1","0","0","0"],
#    ["0","0","1","0","0"],
#    ["0","0","0","1","1"]
#    ]
#    result = s.numIslands(grid)
#    print('Second grid')
#    print(result)
#    print('\n')
    grid = [["1","1","1"],["0","1","0"],["1","1","1"]]
    result = s.numIslands(grid)
    print(result)

def test_DFS():
    """
    """
    adj = np.zeros((5, 5))
    for i in range(0, 5):
        adj[i, i] = 1
    adj[0, 1] = 1
    adj[1, 0] = 1
    adj[0, 2] = 1
    adj[2, 0] = 1
    adj[0, 3] = 1
    adj[3, 0] = 1
    adj[4, 1] = 1
    adj[1, 4] = 1
    adj[4, 2] = 1
    adj[2, 4] = 1
    adj[4, 3] = 1
    adj[3, 4] = 1
    result = DFS(adj)
    print(result)

if __name__ == '__main__':

#    test_numIslands()
    test_DFS()
