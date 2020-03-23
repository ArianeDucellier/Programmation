def isValidBST(TreeNode):
    """
    """
    ok = True
    level = 0
    while 2 ** (level + 2) <= len(TreeNode):
        for i in range(0, 2 ** level):
            key = TreeNode[2 ** level - 1 + i]
            node1 = TreeNode[2 ** (level + 1) - 1 + 2 * i]
            node2 = TreeNode[2 ** (level + 1) - 1 + 2 * i + 1]
            if (node1 != None) and (node1 >= key):
                ok = False
            if (node2 != None) and (node2 <= key):
                ok = False
        level = level + 1
    return ok

def inorderSuccessor(TreeNode, p):
    """
    """
    answer = None
    level = 0
    begin = 0
    while 2 ** (level + 1) <= len(TreeNode):
        next_begin = 0
        for i in range(begin, 2 ** level):
            key = TreeNode[2 ** level - 1 + i]
            if key != None:
                if key <= p:
                    next_begin = 2 * i + 1
                if key > p:
                    if answer == None:
                        answer = key
                    else:
                        if key < answer:
                            answer = key
        begin = next_begin
        level = level + 1
    return answer
        