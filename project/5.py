import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
import random

class TreeNode:
    """
    Клас, що представляє вузол бінарного дерева.
    """
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def insert(root, value):
    """
    Функція для вставки нового значення в бінарне дерево.
    """
    if root is None:
        return TreeNode(value)
    if value < root.value:
        root.left = insert(root.left, value)
    else:
        root.right = insert(root.right, value)
    return root

def generate_binary_tree(size=10):
    """
    Генерує випадкове бінарне дерево з унікальними значеннями.
    """
    values = random.sample(range(1, 100), size)
    root = None
    for v in values:
        root = insert(root, v)
    return root

def traverse_dfs(root):
    """
    Виконує обхід бінарного дерева в глибину (DFS) за допомогою стеку.
    """
    if root is None:
        return []
    stack, visited = [root], []
    while stack:
        node = stack.pop()
        visited.append(node.value)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return visited

def traverse_bfs(root):
    """
    Виконує обхід бінарного дерева в ширину (BFS) за допомогою черги.
    """
    if root is None:
        return []
    queue, visited = [root], []
    while queue:
        node = queue.pop(0)
        visited.append(node.value)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return visited

def build_graph(node, graph=None, pos=None, x=0, y=0, layer=1):
    """
    Побудова графа для візуалізації бінарного дерева.
    """
    if graph is None:
        graph = nx.DiGraph()
        pos = {}
    if node is not None:
        graph.add_node(node.value)
        pos[node.value] = (x, -y)
        if node.left:
            graph.add_edge(node.value, node.left.value)
            build_graph(node.left, graph, pos, x - 1 / (2 ** layer), y + 1, layer + 1)
        if node.right:
            graph.add_edge(node.value, node.right.value)
            build_graph(node.right, graph, pos, x + 1 / (2 ** layer), y + 1, layer + 1)
    return graph, pos

def visualize_traversal(root, traversal_order, title):
    """
    Візуалізація обходу бінарного дерева.
    """
    graph, pos = build_graph(root)
    
    colors = ["#%02x%02x%02x" % (int(18 + i * 5), int(150 + i * 10), int(240 - i * 10)) for i in range(len(traversal_order))]
    color_map = {value: colors[i] for i, value in enumerate(traversal_order)}
    
    plt.figure(figsize=(10, 6))
    nx.draw(graph, pos, with_labels=True, node_size=2000, node_color=[color_map[node] for node in graph.nodes], edge_color="gray", font_size=12, font_weight='bold')
    plt.title(title)
    plt.show()

if __name__ == "__main__":
    """
    Основна функція для генерації дерева, виконання обходів та візуалізації.
    """
    root = generate_binary_tree(10)
    dfs_order = traverse_dfs(root)
    bfs_order = traverse_bfs(root)
    
    visualize_traversal(root, dfs_order, "DFS Traversal Visualization")
    visualize_traversal(root, bfs_order, "BFS Traversal Visualization")
