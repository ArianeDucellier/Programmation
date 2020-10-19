class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):

    # Auxiliary function for sumOfLeftLeaves
    def sumOfLeftLeaves_2(self, root, isLeft):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root.left != None:
            left_sum = self.sumOfLeftLeaves_2(root.left, True)
        else:
            left_sum = 0
        if root.right != None:
            right_sum = self.sumOfLeftLeaves_2(root.right, False)
        else:
            right_sum = 0
        if (root.left == None) and (root.right == None):
            if isLeft == True:
                leave = root.val
            else:
                leave = 0
        else:
            leave = 0
        return(left_sum + right_sum + leave)

    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        if (root.left == None) and (root.right == None):
            return 0
        return self.sumOfLeftLeaves_2(root, True)

def test_sumOfLeftLeaves():
    """
    Input: [1,null,2,3]
    Output: [1,2,3]
    """
    s = Solution()
    three = TreeNode(3)
    nine = TreeNode(9)
    twenty = TreeNode(20)
    fifteen = TreeNode(15)
    seven = TreeNode(7)
    three.left = nine
    three.right = twenty
    twenty.left = fifteen
    twenty.right = seven
    result = s.sumOfLeftLeaves(three)
    print('Sum of left leaves:')
    print(result)
    print('\n')

if __name__ == '__main__':

    test_sumOfLeftLeaves()
