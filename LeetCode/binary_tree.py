# To build tree nodes
class TreeNode(object):
     def __init__(self, x):
         self.val = x
         self.left = None
         self.right = None

class Solution(object):

    # Preorder traversal: Top->Bottom then Left->Right
    # First version with space complexity O(N)
    def preorderTraversal_1(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        
        stack, output = [root, ], []
        
        while stack:
            root = stack.pop()
            if root is not None:
                output.append(root.val)
                if root.right is not None:
                    stack.append(root.right)
                if root.left is not None:
                    stack.append(root.left)
        
        return output

    # Second version with space complexity O(1)
    def preorderTraversal_2(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        node, output = root, []
        while node:  
            if not node.left: 
                output.append(node.val)
                node = node.right 
            else: 
                predecessor = node.left 

                while predecessor.right and predecessor.right is not node: 
                    predecessor = predecessor.right 

                if not predecessor.right:
                    output.append(node.val)
                    predecessor.right = node  
                    node = node.left  
                else:
                    predecessor.right = None
                    node = node.right         

        return output

    # Inorder traversal: Left->Node->Right
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        
        stack, output = [root, ], []
        
        while stack:
            root = stack[-1]
            if root.left is None:
                root = stack.pop()
                output.append(root.val)
                if len(stack) > 0:
                    stack[-1].left = None
                if root.right is not None:
                    stack.append(root.right)             
            else:
                stack.append(root.left)
        
        return output

    # Postorder traversal: Bottom->Top then Left->Right
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root is None:
            return []
        
        stack, output = [root, ], []
        while stack:
            root = stack[-1]
            if root.left is not None:
                stack.append(root.left)
            elif root.right is not None:
                stack.append(root.right)
            else:
                root = stack.pop()
                output.append(root.val)
                if len(stack) > 0:
                    if root == stack[-1].left:
                        stack[-1].left = None
                    elif root == stack[-1].right:
                        stack[-1].right = None

        return output

    # Level order traversal: Left->Right level by level
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root is None:
            return []

        output = [[root.val]]
        old_level = [root]
        if (root.left == None) and (root.right == None):
            done = True
        else:
            done = False
        while done == False:
            new_level = []
            new_values = []
            done = True
            for node in old_level:
                if node.left != None:
                    new_level.append(node.left)
                    new_values.append(node.left.val)
                    done = False
                if node.right != None:
                    new_level.append(node.right)
                    new_values.append(node.right.val)
                    done = False
            if len(new_values) > 0:
                output.append(new_values)
            old_level = list(new_level)

        return output

    # Maximum depth of a tree
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        left_depth = self.maxDepth(root.left)
        right_depth = self.maxDepth(root.right)
        return (max(left_depth, right_depth) + 1)

    # Auxiliary function for isSymmetric
    def isMirror(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: bool
        """
        if (t1 == None and t2 == None):
            return True
        elif (t1 == None or t2 == None):
            return False
        else:
            return (t1.val == t2.val) and self.isMirror(t1.right, t2.left) and self.isMirror(t1.left, t2.right)

    # Is binary tree symmetric
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.isMirror(root, root)

    # Is there a path such that the sum of all node values is equal to input?
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if (root.left == None) and (root.right == None):
            return (root.val == sum)
        else:
            if root.left == None:
                isleft = False
            else:
                isleft = self.hasPathSum(root.left, sum - root.val)
            if root.right == None:
                isright = False
            else:
                isright = self.hasPathSum(root.right, sum - root.val)
            return (isleft or isright)

    # Count the number of uni-value subtrees
    def countUnivalSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if (root.right == None) and (root.left == None):
            return 1
        else:
            isLeft = False
            isRight = False
            if (root.left == None):
                nb_left = 0
                isLeft = True
            else:
                nb_left = self.countUnivalSubtrees(root.left)
                if (root.left.val == root.val):
                    isLeft = True
            if (root.right == None):
                nb_right = 0
                isRight = True
            else:
                nb_right = self.countUnivalSubtrees(root.right)
                if (root.right.val == root.val):
                    isRight = True
            if (isLeft == True) and (isRight == True):
                return nb_left + nb_right + 1
            else:
                return nb_left + nb_right

if __name__ == '__main__':

    s = Solution()

#    three = TreeNode(3)
#    two = TreeNode(2)
#    one = TreeNode(1)
#    two.left = three
#    one.right = two
#    result_1 = s.preorderTraversal_1(one)
#    print('Preorder traversal:')
#    print(result_1)
#    print('\n')
#    result_2 = s.preorderTraversal_2(one)
#    print('Preorder traversal:')
#    print(result_2)
#    print('\n')
#    result = s.inorderTraversal(one)
#    print('Inorder traversal:')
#    print(result)
#    print('\n')
#    result = s.postorderTraversal(one)
#    print('Postorder traversal:')
#    print(result)
#    print('\n')

#    three = TreeNode(3)
#    nine = TreeNode(9)
#    twenty = TreeNode(20)
#    fifteen = TreeNode(15)
#    seven = TreeNode(7)
#    three.left = nine
#    three.right = twenty
#    twenty.left = fifteen
#    twenty.right = seven
#    result = s.levelOrder(three)
#    print('Level order traversal:')
#    print(result)
#    print('\n')
#    result = s.maxDepth(three)
#    print('Maximum depth of a tree:')
#    print(result)
#    print('\n')

#    one = TreeNode(1)
#    twoL = TreeNode(2)
#    twoR = TreeNode(2)
#    threeL = TreeNode(3)
#    threeR = TreeNode(3)
#    fourL = TreeNode(4)
#    fourR = TreeNode(4)
#    one.left = twoL
#    one.right = twoR
#    twoL.left = threeL
#    twoR.right = threeR
#    twoL.right = fourL
#    twoR.left = fourL
#    result = s.isSymmetric(one)
#    print('Is first tree symmetric?')
#    print(result)
#    print('\n')
#    twoL.left = None
#    twoR.left = None
#    twoL.right = threeL
#    twoR.right = threeR
#    result = s.isSymmetric(one)
#    print('Is second tree symmetric?')
#    print(result)
#    print('\n')

#    five = TreeNode(5)
#    four_a = TreeNode(4)
#    eight = TreeNode(8)
#    eleven = TreeNode(11)
#    thirteen = TreeNode(13)
#    four_b = TreeNode(4)
#    seven = TreeNode(7)
#    two = TreeNode(2)
#    one = TreeNode(1)
#    five.left = four_a
#    five.right = eight
#    four_a.left = eleven
#    eleven.left = seven
#    eleven.right = two
#    eight.left = thirteen
#    eight.right = four_b
#    four_b.right = one
#    result = s.hasPathSum(five, 22)
#    print('Has a tree a path with sum equal to 22?')
#    print(result)
#    print('\n')

    t1 = TreeNode(5)
    t2 = TreeNode(1)
    t3 = TreeNode(5)
    t4 = TreeNode(5)
    t5 = TreeNode(5)
    t6 = TreeNode(5)
    t1.left = t2
    t1.right = t3
    t2.left = t4
    t2.right = t5
    t3.right = t6
    result = s.countUnivalSubtrees(t1)
    print('Number of uni-value subtrees = {}'.format(result))
    print('\n')
