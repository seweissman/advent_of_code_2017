from collections import defaultdict


def connected_component(tree, root, component):
    if root in component:
        return
    else:
        component.add(root)
        for c in tree[root]:
            connected_component(tree, c, component)


def connected_components(tree):
    component = set()
    component_count = 0
    for n in tree:
        if n in component:
            continue
        component_count += 1
        connected_component(tree, n, component)
    return component_count


def parse_tree(s):
    s = s.strip()
    tree = defaultdict(list)
    nodes = s.split("\n")
    for node in nodes:
        n, cstr = node.split(" <-> ")
        n = int(n)
        children = [int(x) for x in cstr.split(", ")]
        tree[n] = children
    return tree


input = """0 <-> 2
1 <-> 1
2 <-> 0, 3, 4
3 <-> 2, 4
4 <-> 2, 3, 6
5 <-> 6
6 <-> 4, 5"""

tree = parse_tree(input)
component = set()
connected_component(tree, 0, component)
assert component == set([0, 2, 3, 4, 5, 6])

if __name__ == "__main__":
    with open("day12.input.txt") as f:
        input = f.read()
    tree = parse_tree(input)

    component = set()
    connected_component(tree, 0, component)
    print(len(component))
    print(connected_components(tree))
