import queue

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def print_linkedList(my_list):
    node = my_list
    while node != None:
        print(node.next.val)
        node = node.next

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

    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        node = head
        previous = None
        while node != None:
            following = node.next
            node.next = previous
            previous = node
            node = following
        return previous

    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if  head == None:
            return False
        if head.next ==  None:
            return False
        fast = head
        slow = head
        
        while (fast != None) and (fast.next != None):
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        all_paths = []
        if not root:
            return all_paths
        path = ""
        
        def find_paths(root, path):
            if not root:
                all_paths.append(path)
                return
            else:
                if not path:
                    path = str(root.val)
                else:
                    path += "->" + str(root.val)
            if not root.left and  not root.right:
                all_paths.append(path)
                return

            if root.left:
                find_paths(root.left, path)
            if root.right:
                find_paths(root.right, path)
        
        find_paths(root, path)
        return all_paths

    def compute_tilt(self, root):
        """
        :type root: TreeNode
        :rtype: (int, float)
        """
        if root == None:
            return (0, 0)
        (sum1, tilt1) = self.compute_tilt(root.left)
        (sum2, tilt2) = self.compute_tilt(root.right)
        tilt_node = abs(sum1 - sum2)
        sum_node = root.val + sum1 + sum2
        return(sum_node, tilt_node + tilt1 + tilt2)

    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        (sum_tree, tilt_tree) = self.compute_tilt(root)
        return tilt_tree

    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """    
        if root == None:
            return 0
    
        que = queue.Queue()
        que.add((root,1))
        while (not que.empty()):
            node,level = que.get()
            if node.right == None and node.left == None:
                return level
            if node.left != None:
                que.add((node.left,level+1))
            if node.right != None:
                que.add((node.right,level+1))

    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        p1 = 0
        p2 = len(nums) - 1
        while (p1 != p2):
            if nums[p1] == 0:
                del nums[p1]
                nums.append(0)
                p2 = p2 - 1
            else:
                p1 = p1 + 1
        return nums

    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        i = 0
        j = 1
        while j < len(nums):
            if nums[i] == nums[j]:
                j = j + 1
            else:
                i = i + 1
                nums[i] = nums[j]
                j = j + 1
        print(nums[0 : (i + 1)])
        return (i + 1)

    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        i = 0
        while i < len(s) / 2 :
            temp = s[i]
            s[i] = s[len(s) - i - 1]
            s[len(s) - i - 1] = temp
            i = i + 1
        return s

    def find_substrings(self, words):
        """
        """
        substrings = []
        for word1 in words:
            for word2 in words:
                if len(word1) < len(word2):
                    if word1 in word2:
                        substrings.append(word1)
                        break
        return substrings

    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        node.val = node.next.val
        node.next = node.next.next

    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow = head
        fast = head
        while (fast != None) and (fast.next != None):
            slow = slow.next
            fast = fast.next.next
        return slow

def test_sumOfLeftLeaves():
    """
    Input: [3,9,20,null,null,15,7]
    Output: 24
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
    Input: [8,1,2,2,3]
    Output: [4,0,1,1,3]
    Input: [6,5,4,8]
    Output: [2,1,0,3]
    Input: [7,7,7,7]
    Output: [0,0,0,0]
    """
    s = Solution()
    print('How many numbers are smaller than the current numbers')
    result = s.smallerNumbersThanCurrent([8,1,2,2,3])
    print(result)
    print('\n')
    result = s.smallerNumbersThanCurrent([6,5,4,8])
    print(result)
    print('\n')
    result = s.smallerNumbersThanCurrent([7,7,7,7])
    print(result)
    print('\n')

def test_reverseList():
    """
    Input: [1,2,3,4,5]
    Output: [5,4,3,2,1]
    Input: [1,2]
    Output: [2,1]
    Input: []
    Output: []
    """
    n1 = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(3)
    n4 = ListNode(4)
    n5 = ListNode(5)
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    s = Solution()
    result = s.reverseList(n1)
    while result != None:
        print(result.val)
        result = result.next
    n1 = ListNode(1)
    n2 = ListNode(2)
    n1.next = n2
    result = s.reverseList(n1)
    while result != None:
        print(result.val)
        result = result.next
    result = s.reverseList(None)
    print(result)

def test_hasCycle():
    """
    Input: [3,2,0,-4], pos = 1
    Output: true
    Input: [1,2], pos = 0
    Output: true
    Input: [1], pos = -1
    Output: false
    """
    s = Solution()
    print("Does the linked list have a cycle?")
    n1 = ListNode(3)
    n2 = ListNode(2)
    n3 = ListNode(0)
    n4 = ListNode(-4)
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n2
    result = s.hasCycle(n1)
    print(result)
    n1 = ListNode(1)
    n2 = ListNode(2)
    n1.next = n2
    n2.next = n1
    result = s.hasCycle(n1)
    print(result)
    n1 = ListNode(1)
    result = s.hasCycle(n1)
    print(result)

def test_binaryTreePaths():
    """
    Input: [1, 2, 3, None, 5, None, None]
    Output: ["1->2->5", "1->3"]
    """
    s = Solution()
    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    n5 = TreeNode(5)
    n2.right = n5
    n1.left = n2
    n1.right = n3
    result = s.binaryTreePaths(n1)
    print(result)

def test_findTilt():
    """
    Input: [1,2,3]
    Output: 1
    Input: [4,2,9,3,5,null,7]
    Output: 15
    Input: [21,7,14,1,1,2,2,3,3]
    Output: 9
    """
    s = Solution()
    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    n1.left = n2
    n1.right = n3
    result = s.findTilt(n1)
    print(result)
    n4 = TreeNode(4)
    n2 = TreeNode(2)
    n9 = TreeNode(9)
    n3 = TreeNode(3)
    n5 = TreeNode(5)
    n7 = TreeNode(7)
    n2.left = n3
    n2.right = n5
    n9.right = n7
    n4.left = n2
    n4.right = n9
    result = s.findTilt(n4)
    print(result)
    n21 = TreeNode(21)
    n7 = TreeNode(7)
    n14 = TreeNode(14)
    n1l = TreeNode(1)
    n1r = TreeNode(1)
    n2l = TreeNode(2)
    n2r = TreeNode(2)
    n3l = TreeNode(3)
    n3r = TreeNode(3)
    n1l.left = n3l
    n1l.right = n3r
    n7.left = n1l
    n7.right = n1r
    n14.left = n2l
    n14.right = n2r
    n21.left = n7
    n21.right = n14
    result = s.findTilt(n21)
    print(result)

def test_minDepth():
    """
    """
    return(0)
    
def test_moveZeroes():
    """
    Input: [0,1,0,3,12]
    Output: [1,3,12,0,0]
    """
    s = Solution()
    result = s.moveZeroes([0,1,0,3,12])
    print(result)

def test_removeDuplicates():
    """
    Input: [1,1,2]
    Output: 2, [1,2]
    Input: [0,0,1,1,1,2,2,3,3,4]
    Output: 5, [0,1,2,3,4]
    """
    s = Solution()
    result = s.removeDuplicates([1,1,2])
    print(result)
    result = s.removeDuplicates([0,0,1,1,1,2,2,3,3,4])
    print(result)

def test_reverseString():
    """
    Input: ["h","e","l","l","o"]
    Output: ["o","l","l","e","h"]
    Input: ["H","a","n","n","a","h"]
    Output: ["h","a","n","n","a","H"]
    """
    s = Solution()
    result = s.reverseString(["h","e","l","l","o"])
    print(result)
    result = s.reverseString(["H","a","n","n","a","h"])
    print(result)

def test_find_substrings():
    """
    """
    s = Solution()
    substrings = s.find_substrings(["mass","as","hero","superhero"])
    print(substrings)

def test_deleteNode():
    """
    Input: head = [4,5,1,9], node = 5
    Output: [4,1,9]
    Input: head = [4,5,1,9], node = 1
    Output: [4,5,9]
    Input: head = [1,2,3,4], node = 3
    Output: [1,2,4]
    Input: head = [0,1], node = 0
    Output: [1]
    Input: head = [-3,5,-99], node = -3
    Output: [5,-99]
    """
    s = Solution()
    four = ListNode(4)
    five = ListNode(5)
    one = ListNode(1)
    nine = ListNode(9)
    one.next = nine
    five.next = one
    four.next = five
    result = s.deleteNode(five)
    print_linkedList(four)

if __name__ == '__main__':

#    test_sumOfLeftLeaves()
#    test_maxProfit()
#    test_smallerNumbersThanCurrent()
#    test_reverseList()
#    test_hasCycle()
#    test_binaryTreePaths()
#    test_findTilt()
#    test_moveZeroes()
#    test_removeDuplicates()
#    test_reverseString()
#    test_find_substrings()
    test_deleteNode()

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

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        # find color to match
        color = image[sr][sc]
        
        if color == newColor:
            return image
    
        # change the color to newColor
        image[sr][sc] = newColor
    
        # check all 4 adjacent sides
        # top
        # if its valid (within the bounds, equal to 'color')
        if sr > 0 and image[sr - 1][sc] == color:
            # recursive call on this row, col
            image = self.floodFill(image, sr - 1, sc, newColor)
        
        # bottom
        if sr + 1 < len(image) and image[sr + 1][sc] == color:
            image = self.floodFill(image, sr + 1, sc, newColor)
        
        # left
        if sc > 0 and image[sr][sc - 1] == color:
            image = self.floodFill(image, sr, sc - 1, newColor)
        
        # right
        if sc + 1 < len(image[0]) and image[sr][sc + 1] == color:
            image = self.floodFill(image, sr, sc + 1, newColor)
            
        # return grid
        return image
        