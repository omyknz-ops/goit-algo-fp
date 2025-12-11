import uuid
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque


class Node:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None
        self.color = "skyblue"
        self.id = str(uuid.uuid4())


# DFS - using STACK
def dfs(root):
    stack = [root]
    result = []
    
    while stack:
        node = stack.pop()           # LIFO - last in, first out
        result.append(node)
        
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    
    return result


# BFS - using QUEUE
def bfs(root):
    queue = deque([root])
    result = []
    
    while queue:
        node = queue.popleft()       # FIFO - first in, first out
        result.append(node)
        
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    
    return result


# Generate colors from dark to light
def generate_colors(n):
    colors = []
    for i in range(n):
        ratio = i / max(n - 1, 1)
        r = int(26 + (168 - 26) * ratio)
        g = int(58 + (212 - 58) * ratio)
        b = int(92 + (240 - 92) * ratio)
        colors.append(f'#{r:02x}{g:02x}{b:02x}')
    return colors


# Build tree from array
def build_tree(arr, index=0):
    if index >= len(arr):
        return None
    node = Node(arr[index])
    node.left = build_tree(arr, 2 * index + 1)
    node.right = build_tree(arr, 2 * index + 2)
    return node


# Draw tree
def draw_tree(root, title):
    def add_edges(graph, node, pos, x=0, y=0, layer=1):
        if node:
            graph.add_node(node.id, color=node.color, label=node.val)
            if node.left:
                graph.add_edge(node.id, node.left.id)
                pos[node.left.id] = (x - 1/2**layer, y - 1)
                add_edges(graph, node.left, pos, x - 1/2**layer, y - 1, layer + 1)
            if node.right:
                graph.add_edge(node.id, node.right.id)
                pos[node.right.id] = (x + 1/2**layer, y - 1)
                add_edges(graph, node.right, pos, x + 1/2**layer, y - 1, layer + 1)
    
    tree = nx.DiGraph()
    pos = {root.id: (0, 0)}
    add_edges(tree, root, pos)
    
    colors = [tree.nodes[n]['color'] for n in tree.nodes]
    labels = {n: tree.nodes[n]['label'] for n in tree.nodes}
    
    plt.figure(figsize=(10, 6))
    plt.title(title, fontsize=14, fontweight='bold')
    nx.draw(tree, pos=pos, labels=labels, arrows=False,
            node_size=2500, node_color=colors, font_color='white', font_weight='bold')
    plt.show()  # Display on screen


# Visualize traversal
def visualize(root, traversal_func, title):
    nodes = traversal_func(root)
    colors = generate_colors(len(nodes))
    
    for i, node in enumerate(nodes):
        node.color = colors[i]
    
    order = " → ".join(str(n.val) for n in nodes)
    print(f"{title}: {order}")
    draw_tree(root, f"{title}\nOrder: {order}")


# ===== MAIN =====
if __name__ == "__main__":
    arr = [0, 4, 1, 5, 10, 3]
    
    print(f"Array: {arr}\n")
    
    # DFS
    root1 = build_tree(arr)
    visualize(root1, dfs, "DFS (Stack)")
    
    # BFS
    root2 = build_tree(arr)
    visualize(root2, bfs, "BFS (Queue)")