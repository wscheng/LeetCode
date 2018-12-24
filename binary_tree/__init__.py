class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def string_to_tree_node(tree_str):
    tree_str = tree_str.strip()
    # remove [ ]
    tree_str = tree_str[1:-1]
    all_val = [int(x) if x != 'null' else None for x in tree_str.split(',')]
    len_all_val = len(all_val)
    if len_all_val == 0:
        return None
    front = 0
    pointer = 0
    all_node = [TreeNode(all_val[0])]
    # print(all_val)
    while pointer < len_all_val:
        root = all_node[front]
        pointer += 1
        if pointer < len_all_val and all_val[pointer] is not None:
            # print(pointer, all_val[pointer])
            root.left = TreeNode(all_val[pointer])
            all_node.append(root.left)
        pointer += 1
        if pointer < len_all_val and all_val[pointer] is not None:
            # print(pointer, all_val[pointer])
            root.right = TreeNode(all_val[pointer])
            all_node.append(root.right)
        front += 1
    return all_node[0]
