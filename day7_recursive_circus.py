"""
Day 7: Recursive Circus
"""
import re
from collections import defaultdict
NODE_PATTERN = re.compile("([a-z]+) \((\d+)\)")

def build_tree(lines):
    reverse_tree = defaultdict(str)
    tree = defaultdict(list)
    node_weights = {}
    for line in lines:
        line = line.strip()
        if line == '':
            continue
        entry = line.split(" -> ")
        parent_weight = entry[0]
        m = NODE_PATTERN.search(parent_weight)
        parent = m.group(1)
        weight = int(m.group(2))
        node_weights[parent] = weight
        if len(entry) == 2:
            children_str = entry[1]
            children = children_str.split(", ")
            tree[parent] = children
            for child in children:
                reverse_tree[child] = parent
    return (tree, reverse_tree, node_weights)

def find_root(tree, node=None):
    # Get some node from the tree
    if node is None:
        node = next(iter(tree))
    parent = tree[node]
    if parent == '':
        return node
    else:
        return find_root(tree, parent)

sample_tree_str="""pbga (66)
xhth (57)
ebii (61)
havc (66)
ktlj (57)
fwft (72) -> ktlj, cntj, xhth
qoyq (66)
padx (45) -> pbga, havc, qoyq
tknk (41) -> ugml, padx, fwft
jptl (61)
ugml (68) -> gyxo, ebii, jptl
gyxo (61)
cntj (57)"""

sample_tree_input = sample_tree_str.split("\n")
# print(sample_tree_input)
sample_tree, sample_reverse_tree, sample_node_weights = build_tree(sample_tree_input)
# print("Sample tree: ", sample_tree)
assert find_root(sample_reverse_tree) == "tknk"

def node_weight(tree, node_weights, n):
    w = node_weights[n]
    return w + sum(node_weight(tree, node_weights, c) for c in tree[n])

def all_same(l):
    if len(l) == 0:
        return True
    v_first = l[0]
    for v in l:
        if v != v_first:
            return False
    return True

def is_balanced_node(tree, node_weights, n):
    children = tree[n]
    if len(children) == 0:
        return True
    child_weights = [node_weight(tree, node_weights, c) for c in children]
    return all_same(child_weights)

def find_different_index(l):
    if len(l) <= 1:
        return None
    if len(l) == 2:
        return l.index(max(l))
    counts = defaultdict(int)
    for x in l:
        counts[x] += 1
    wrong_weight = 0
    right_weight = 0
    for k in counts:
        if counts[k] == 1:
            wrong_weight = k
        if counts[k] > 1:
            right_weight = k
    wrong_index = l.index(wrong_weight)
    return (wrong_index, right_weight - wrong_weight)


def fix_tree(tree, node_weights, root, diff_weight=None):
    if diff_weight is None:
        child_weights = [node_weight(tree, node_weights, c) for c in tree[root]]
        i_diff, w_diff = find_different_index(child_weights)
        diff_weight = w_diff
    if is_balanced_node(tree, node_weights, root):
        w_fix = node_weights[root] + diff_weight
        print("Found node to fix, weight should be: ", w_fix)
        return w_fix
    child_weights = [node_weight(tree, node_weights, c) for c in tree[root]]
    i_diff, w_diff = find_different_index(child_weights)
    node_diff = tree[root][i_diff]
    print(child_weights, i_diff, node_diff)
    return fix_tree(tree, node_weights, node_diff, diff_weight)

assert fix_tree(sample_tree, sample_node_weights, 'tknk') == 60

def find_unbalanced_node(tree, node_weights):
    for node in tree:
        if not is_balanced_node(tree, node_weights, node):
            return node
    return None

if __name__ == "__main__":
    file_in = open("day7.input.txt")
    INPUT = file_in.readlines()
    tree, reverse_tree, node_weights = build_tree(INPUT)
    root = find_root(reverse_tree) 
    print(root)
    print(fix_tree(tree, node_weights, root))

