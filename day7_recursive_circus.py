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
        if parent not in reverse_tree:
            reverse_tree[parent] = ''
        if len(entry) == 2:
            children_str = entry[1]
            children = children_str.split(", ")
            tree[parent] = children
            for child in children:
                reverse_tree[child] = parent
    return (tree, reverse_tree, node_weights)

def get_tower_weights(tree, root, node_weights, tower_weights):
    if len(tree[root]) == 0:
        tower_weights[root] = node_weights[root]
    else:
        for c in tree[root]:
            get_tower_weights(tree, c, node_weights, tower_weights)
        tower_weights[root] = node_weights[root] + sum(tower_weights[c] for c in tree[root])

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
sample_tree, sample_reverse_tree, sample_node_weights = build_tree(sample_tree_input)
sample_root = find_root(sample_reverse_tree)
assert sample_root == "tknk"
sample_tower_weights = defaultdict(int)
get_tower_weights(sample_tree, sample_root, sample_node_weights, sample_tower_weights)

def is_balanced_node(tree, tower_weights, n):
    children = tree[n]
    if len(children) == 0:
        return True
    child_weights = [tower_weights[c] for c in children]
    weight_set = set(child_weights)
    return len(weight_set) == 1

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


def fix_tree(tree, tower_weights, root):
    if is_balanced_node(tree, tower_weights, root):
        node_to_fix = root
        return node_to_fix
    child_weights = [tower_weights[c] for c in tree[root]]
    i_diff, w_diff = find_different_index(child_weights)
    node_diff = tree[root][i_diff]
    return fix_tree(tree, tower_weights, node_diff)


child_weights = [sample_tower_weights[c] for c in sample_tree[sample_root]]
i_diff, w_diff = find_different_index(child_weights)
node_to_fix = fix_tree(sample_tree, sample_tower_weights, sample_root)
fix_weight = w_diff + sample_node_weights[node_to_fix]
assert fix_weight == 60

if __name__ == "__main__":
    file_in = open("day7.input.txt")
    INPUT = file_in.readlines()
    tree, reverse_tree, node_weights = build_tree(INPUT)
    root = find_root(reverse_tree) 
    print(root)
    tower_weights = defaultdict(int)
    get_tower_weights(tree, root, node_weights, tower_weights)
    child_weights = [tower_weights[c] for c in tree[root]]
    i_diff, w_diff = find_different_index(child_weights)
    node_to_fix = fix_tree(tree, tower_weights, root)
    print("Node to fix", node_to_fix)
    fix_weight = w_diff + node_weights[node_to_fix]
    print(fix_weight)

