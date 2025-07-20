import collections
from collections import defaultdict, deque

class Node:
    __slots__ = ('name', 'children', 'rep')
    def __init__(self, name):
        self.name = name
        self.children = {}
        self.rep = None

class Solution:
    def deleteDuplicateFolder(self, paths: List[List[str]]) -> List[List[str]]:
        root = Node("")
        for path in paths:
            node = root
            for folder in path:
                if folder not in node.children:
                    node.children[folder] = Node(folder)
                node = node.children[folder]
        
        rep_count = defaultdict(int)
        stack = deque()
        stack.append((root, iter(sorted(root.children.items(), key=lambda x: x[0]))))
        
        while stack:
            node, children_iter = stack[-1]
            try:
                child_name, child_node = next(children_iter)
                stack.append((child_node, iter(sorted(child_node.children.items(), key=lambda x: x[0]))))
            except StopIteration:
                stack.pop()
                children_reps = []
                for name, child in sorted(node.children.items(), key=lambda x: x[0]):
                    children_reps.append((name, child.rep))
                rep = tuple(children_reps)
                node.rep = rep
                if children_reps:
                    rep_count[rep] += 1
        
        dup_reps = set(rep for rep, count in rep_count.items() if count >= 2)
        
        to_delete = set()
        stack = [root]
        while stack:
            node = stack.pop()
            for name, child in node.children.items():
                if child.rep in dup_reps and child.rep:
                    q = deque([child])
                    while q:
                        n = q.popleft()
                        to_delete.add(n)
                        for next_name, next_child in n.children.items():
                            q.append(next_child)
                else:
                    stack.append(child)
        
        results = []
        stack = collections.deque()
        stack.append((root, []))
        while stack:
            node, path = stack.pop()
            for name, child in node.children.items():
                if child in to_delete:
                    continue
                new_path = path + [name]
                results.append(new_path)
                stack.append((child, new_path))
        
        return results