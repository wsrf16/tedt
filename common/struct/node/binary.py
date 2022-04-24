

class TreeNode(object):
    """ Definition of a binary tree node."""

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    @staticmethod
    def new(obj: object):
        return None if obj is None else TreeNode(obj)

class TreeNodeUtil(object):
    @staticmethod
    def convert2(lst: list):
        root = TreeNode(lst[0])
        task = [root]

        i: int = 0
        while task:
            node = task.pop(0)
            if node is None:
                continue

            i += 1
            if i < len(lst):
                if lst[i] is not None:
                    node.left = TreeNode(lst[i])
                    task.append(node.left)
                else:
                    node.left = None

            i += 1
            if i < len(lst):
                if lst[i] is not None:
                    node.right = TreeNode(lst[i])
                    task.append(node.right)
                else:
                    node.right = None
        TreeNodeUtil.iterator(root, lambda x: print(x.val))
        return root


    @staticmethod
    def convert(lst: list):
        task = []
        i = 0
        root = TreeNode.new(lst[i])
        task.append(root)

        while task:
            node = task.pop(0)
            if node is not None:
                if i + 1 < len(lst):
                    node.left = TreeNode.new(lst[i + 1])
                    task.append(node.left)
                if i + 2 < len(lst):
                    node.right = TreeNode.new(lst[i + 2])
                    task.append(node.right)
            i += 2
        TreeNodeUtil.iterator(root, lambda x: print(x.val))
        return root

    @staticmethod
    def iterator(root: TreeNode, handle):
        queue = [root]

        while queue:
            node = queue.pop(0)
            handle(node)

            if node.left is not None:
                queue.append(node.left)

            if node.right is not None:
                queue.append(node.right)

    @staticmethod
    def flatten(node: TreeNode):
        task = []
        task.append(node)
        result = [node.val]
        while task:
            node = task.pop(0)
            task.append(node.left)
            if node.left is not None:
                result.append(node.left.val)
            else:
                result.append(None)

            task.append(node.right)
            if node.right is not None:
                result.append(node.right.val)
            else:
                result.append(None)
        return result



