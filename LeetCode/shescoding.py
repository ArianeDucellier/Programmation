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

    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) < 2:
            return 0
        profit = 0
        buy = prices[0]
        for i in range(1, len(prices)):
            new_profit = prices[i] - buy
            if new_profit > profit:
                profit = new_profit
            if prices[i] < buy:
                buy = prices[i]
        return profit

    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        count_list = [0] * 101
        for num in nums:
            count_list[num] += 1

        sum_list = [0] * 101
        sum_list[0] = count_list[0]
        for i in range(1, len(count_list)):
            sum_list[i] = sum_list[i - 1] + count_list[i]

        output_list = []
        for num in nums:
            if num == 0:
                output_list.append(0)
            else:
                output_list.append(sum_list[num - 1])

        return output_list

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

def test_maxProfit():
    """
    Input: [7,1,5,3,6,4]
    Output: 5
    Input: [7,6,4,3,1]
    Output: 0
    """
    s = Solution()
    print('Best time to buy and sell:')
    result = s.maxProfit([7,1,5,3,6,4])
    print(result)
    result = s.maxProfit([7,6,4,3,1])
    print(result)
    print('\n')

def test_smallerNumbersThanCurrent():
    """
    Input: [5,0,10,0,10,6]
    Output: [2,0,4,0,4,3]
    """
    s = Solution()
    print('How many numbers are smaller than the current numbers')
    result = s.smallerNumbersThanCurrent([5,0,10,0,10,6])
    print(result)
    print('\n')

if __name__ == '__main__':

#    test_sumOfLeftLeaves()
#    test_maxProfit()
    test_smallerNumbersThanCurrent()
    
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#class Solution(object):
#    def minDepth(self, root):
#        """
#        :type root: TreeNode
#        :rtype: int
#        """
#        public class Main {
#    public static void main(String[] args) {
#        System.out.println("Hello World!");
#    }
#
#    public static int minDepth(TreeNode root){
#        if(root==null) return 0;
#        if((root.left==null and root.right==null) return 1;
#        else return Math.min(minDepth(root.left),minDepth(root.right))+1;
#    }
#}
           
#def minDepth(root):
#    
#    if root == None:
#        return 0
#    
#    que = queue.Queue()
#    que.add((root,1))
#    while(not que.empty()):
#        node,level = que.get()
#        if node.right == None and node.left == None:
#            return level
#        if node.left != None:
#            que.add((node.left,level+1))
#        if node.right != None:
#            que.add((node.right,level+1))


    
#def bottomUp(root):
#    """
#    """
#    if root == None:
#        return []
#    output = [[root.val]]
#    mylist = [(root, 1)]
#    while(mylist):
#        (node, level) = mylist.pop(0)
#        if len(output) == level:
#            if ((node.left != None) and (node.right != None)):
#                output.append([])
#                mylist.append([])
#        if node.left != None:
#            output[-1].append(node.left.value)
#            mylist.append((node.left, level + 1))
#        if node.right != None:
#            output[-1].append(node.right.value)
#            mylist.append((node.right, level + 1))
#    return output.reverse()

# https://leetcode.com/problems/binary-tree-level-order-traversal-ii/

#output = [[3]]
#mylist = [(node3, 1)]
#pop node = node3 , level = 1 mylist []
#output = [[3], []]
#output = [[3], [9]] mylist = [(node9, 2)]
#output = [[3], [9, 20]] mylist = [(node9, 2), (node20, 2)]
#pop node = node9 , level = 2 mylist = [(node20, 2)]
#pop node = node20, level = 2
#output = [[3], [9, 20], []]
           
#var levelOrderBottom = function(root) {
#    if(!root){ return []};
#    const levels = [];
#    let next = [root];
#    while(next.length){
#        levels.unshift(next.map(node => node.val));
#        let current = next;
#        next = [];
#        current.forEach(node => {
#            next.push(node.left);
#            next.push(node.right);
#        });
#        next = next.filter(node => node);
#    }
#    return levels;
#};

