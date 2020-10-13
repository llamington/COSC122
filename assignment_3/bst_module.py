"""Module for finding test results of quarantined people using a BST."""
import sys
from classes3 import Name, BstNode, bst_nested_repr
from tools import read_test_data
sys.setrecursionlimit(10**6)

# note you might want to import other things here for testing
# but your submission should only include the import line above.



def bst_store_pair(root, key, value):
    """
    Stores the key, value pair in the BST tree that stars at the given root.
    This function updates an existing tree so:
      - the root must be an existing BstNode.
      - if root is None an exception is raised.
    Returns the number of key comparisons used.
    Assumes the key is unlikely to already be in the tree and shouldn't check
    for the key being in the current node first, in a similar fashion to the
    binary search from assignment 1. You must figure out which key comparison
    is done first. The simple BST tests will help you figure it out.
    If the key already exists then the value in that node should be updated
    to the given value. This means that keys in the bst will be unique.
    NOTE: You shouldn't use recursion here as it will eventually cause
    Python to blow-up when testing large, worst case, data sets.
    """
    comparisons = 0
    if root is None:
        raise ValueError("I need to have something to add to!")
    # ---start student section---
    in_position = False
    current_node = root
    while not in_position:
        comparisons += 1
        if key < current_node.key:
            # Insert to the left
            if current_node.left is None:
                current_node.left = BstNode(key, value)
                in_position = True
            else:
                current_node = current_node.left
        else:
            # Insert to the right
            comparisons += 1
            if current_node.key == key:
                current_node.value = value
            elif current_node.right is None:
                current_node.right = BstNode(key, value)
                in_position = True
            else:
                current_node = current_node.right
    # ===end student section===
    return comparisons



def get_value_from_tree(root, key):
    """ Returns the value associated with the given key,
    or None if the key is not present in the tree.
    Your search should only check that the root contains the key
    after ruling out that the key can't be in a sub tree.
    That is check if you need to search one of the sub trees first.
    The tests expect a specific comparison to be first, you will
    need to figure out which one it is :)
    Returns the value/None and the number of key comparisons used.
    NOTE: You shouldn't use recursion here as it will eventually cause
    Python to blow-up when testing large, worst case, data sets.
    """
    comparisons = 0
    value = None
    # ---start student section---

    is_found = False
    is_in_subtree = False

    comparisons += 1
    # perform initial comparison without checking key equality
    if key < root.key:
        if root.left:
            comparisons += 1
            is_in_subtree = True if min_key_in_bst(root.left) <= key < root.key else False
            current_node = root.left
    else:
        if root.right:
            comparisons += 1
            is_in_subtree = True if min_key_in_bst(root.right) >= key > root.key else False
            current_node = root.right

    if not is_in_subtree:
        comparisons += 1
        if root.key == key:
            is_found = True
            value = root.value


    while not is_found and current_node:
        comparisons += 1
        if key <= current_node.key:
            comparisons += 1
            if key == current_node.key:
                value = current_node.value
                is_found = True
            else:
                current_node = current_node.left
        else:
            current_node = current_node.right

    # ===end student section===
    return value, comparisons



def min_key_in_bst(root):
    """ Returns the minimum key value in the bst starting at root.
    Returns None if root is None
    Try to do this non-recursively and then try it recursively for fun.
    """
    result = None
    # ---start student section---
    result = root.key
    current_node = root
    while current_node.left is not None:
        current_node = current_node.left
        result = current_node.key
    # ===end student section===
    return result




def max_key_in_bst(root):
    """ Returns the maximum key value in the bst starting at root.
    Returns None if root is None.
    Try to do this non-recursively and then try it recursively for fun.
    """
    result = None
    # ---start student section---
    result = root.key
    current_node = root
    while current_node.right is not None:
        current_node = current_node.right
        result = current_node.key
    # ===end student section===
    return result




def num_nodes_in_tree(root):
    """ Returns the number of nodes in the tree starting at root.
    If the root is None then the number of nodes is zero.
    """
    num_nodes = 0
    # ---start student section---
    num_nodes += 1
    if root.left:
        num_nodes += num_nodes_in_tree(root.left)
    if root.right:
        num_nodes += num_nodes_in_tree(root.right)
    # ===end student section===
    return num_nodes


def bst_depth(root):
    """ The level of a node is the number of edges from the root to the node
        The depth is the maximum level of nodes in a tree.
        Remember, the level of a node is how many edges there are on a path
        from the root to the node.
        So, the depth of a tree starting at the root is:
        - zero if the root is None
        - zero if the root has no children
        - 1 + the max depth of the trees starting at the left and right child
    """
    depth = 0
    # ---start student section---
    depth += 1
    children = []
    children += [bst_depth(root.left)] if root.left else [] + [bst_depth(root.right)] if root.right else []
    # children += [bst_depth(root.right)] if root.right else []
    try:
        depth += max(children)
    except ValueError:
        pass
    # ===end student section===
    return depth


def bst_in_order(root, result_list=None):
    """ Returns a list containing (key, value) tuples
    from the bst, in the order of the keys.
    Basically does an in order traversal of the tree
    collecting (key, value) pairs as each node is visited.
    Returns an empty list if the root is None.
    This function shouldn't use any key comparisons!
    """
    if result_list is None:
        result_list = []
    # ---start student section---
    left_in_order = bst_in_order(root.left) if root.left else []
    right_in_order = bst_in_order(root.right) if root.right else []
    result_list = left_in_order + [(root.key, root.value)] + right_in_order
    # ===end student section===
    return result_list


def bst_result_finder(tested, quarantined):
    """This function takes two lists as input.
    tested contains (nhi, Name, result) tuples for people that have been tested
    quarantined contains the names of people in quarantine

    You cannot assume the lists are in any particular order, ie, you cannot
    assume that either list will be sorted.

    You can assume that there are no duplicate values in either list,
    ie, within each list any name only appears once.

    The function returns a list and an integer, ie, results, comparisons.
    The results list contains (name, nhi, result) tuples for each
    name in the quarantined list. If the name isn't in the tested list
    then the nhi and result should be set to None.
    The integer is the number of Name comparisons the function made.

    You must use a BST to store the tested data and
    use the get_value_from_tree function for looking up names
    in the tree. Using name for the key and a (nhi, result) tuple
    for the value makes sense.

    """
    comparisons = 0
    results = []
    # ---start student section---
    tested_bst = BstNode(tested[0][1], (tested[0][0], tested[0][2]))
    for nhi, t_name, result in tested[1:]:
        bst_store_pair(tested_bst, t_name, (nhi, result))
    result, q_comps = get_value_from_tree(tested_bst, quarantined[0])
    quarantined_bst = BstNode(quarantined[0], result if result else (None, None))
    for q_name in quarantined[1:]:
        result, q_comps = get_value_from_tree(tested_bst, q_name)
        if result:
            bst_store_pair(quarantined_bst, q_name, result)
        else:
            bst_store_pair(quarantined_bst, q_name, (None, None))
    results = [(key, value[0], value[1]) for key, value in bst_in_order(quarantined_bst)]
    # ===end student section===
    return results, comparisons




def smart_bst_result_finder_v1(tested, quarantined):
    """
    Note: this function is an optional bonus exercise
    and isn't worth any marks.
    
    This function has similar input/output as the
    original bst_result_finder but it utilises a much
    faster way of building the bst when the tested
    list is fully sorted by name. If the tested list
    is fully sorted by name then you should write
    an alternative method for adding all the records
    to the bst.
    
    If the tested list isn't fully sorted by name then
    the old/slow method is still used.
    You should leave the get_value_from_tree function
    the same, and use it as before...
    """
    comparisons = 0
    results = []
    # ---start student section---
    pass
    # ===end student section===
    return results, comparisons


def smart_bst_result_finder_v2(tested, quarantined):
    """ 
    Note: this function is a bonus extra questions and
    isn't worth any marks.
    
    This function has similar input/output as the
    original bst_result_finder but it utilises a much
    faster way of building the bst when the tested
    list is fully sorted by name.

    If the tested list was sorted and the quarantined list
    is also sorted then we can speed up the getting values
    from the tree in a way similar to the dual method from
    assignment 2. Doing this means you won't use the 
    normal get_value_from_tree function.

    If the tested list isn't fully sorted by name then
    the old method is still used for building the bst
    and for looking up quarantined names in the tree.

    """
    comparisons = 0
    results = []
    # ---start student section---
    pass
    # ===end student section===
    return results, comparisons


if __name__ == '__main__':
    # put your own simple tests here
    # you don't need to submit this code
    # print("Add some tests here...")
    # root = BstNode(1, 'hello')
    # bst_store_pair(root, 0, 'hi')
    # bst_store_pair(root, 4, 'hio')
    # bst_store_pair(root, -1, 'fasdf')
    # print(Name("Dee") < Name("Lee"))
    tested, quarantined, quarantined_results = read_test_data('test_data/test_data-1000n-50n-10-a.txt')
    results, comparisons = bst_result_finder(tested, quarantined)
    print(results)
    print(quarantined_results)
    pass
