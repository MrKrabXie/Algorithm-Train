class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def dfs_search(root, target):
    """
    Perform depth-first search (DFS) to find the target value in a tree.

    Parameters:
    root (TreeNode): The root node of the tree.
    target: The value to search for.

    Returns:
    TreeNode or None: The node containing the target value, or None if not found.
    """
    if not root:
        return None

    if root.val == target:
        return root

    left_result = dfs_search(root.left, target)
    if left_result:
        return left_result

    right_result = dfs_search(root.right, target)
    if right_result:
        return right_result

    return None

from collections import deque

def bfs_search(root, target):
    """
    Perform breadth-first search (BFS) to find the target value in a tree.

    Parameters:
    root (TreeNode): The root node of the tree.
    target: The value to search for.

    Returns:
    TreeNode or None: The node containing the target value, or None if not found.
    """
    if not root:
        return None

    queue = deque([root])

    while queue:
        node = queue.popleft()
        if node.val == target:
            return node

        if node.left:
            queue.append(node.left)

        if node.right:
            queue.append(node.right)

    return None
def bst_search(root, target):
    """
    Perform binary search tree (BST) search to find the target value in a BST.

    Parameters:
    root (TreeNode): The root node of the BST.
    target: The value to search for.

    Returns:
    TreeNode or None: The node containing the target value, or None if not found.
    """
    if not root:
        return None

    if root.val == target:
        return root

    if target < root.val:
        return bst_search(root.left, target)
    else:
        return bst_search(root.right, target)

if __name__ == '__main__':
    # 构建示例二叉树
    node4 = TreeNode(4)
    node5 = TreeNode(5)
    node2 = TreeNode(2, node4, node5)
    node3 = TreeNode(3)
    node1 = TreeNode(1, node2, node3)

    # 在二叉树中查找值为 3 的节点
    result_dfs = dfs_search(node1, 3)
    result_bfs = bfs_search(node1, 3)
    result_bst = bst_search(node1, 3)

    if result_dfs:
        print("DFS: Found node with value 3")
    else:
        print("DFS: Node with value 3 not found")

    if result_bfs:
        print("BFS: Found node with value 3")
    else:
        print("BFS: Node with value 3 not found")

    if result_bst:
        print("BST: Found node with value 3")
    else:
        print("BST: Node with value 3 not found")
