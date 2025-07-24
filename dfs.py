import matplotlib.pyplot as plt
import networkx as nx
import time

class DFSVisualizer:
    # Track performance metrics
    def __init__(self):
        self.metrics = {
            'algorithm': 'DFS',
            'nodes_visited': 0,
            'time': 0,
            'path_length': 0
        }

    def visualize(self, graph, start, end, speed=1.0):
        #DFS visualization with adjustable speed"""
        G = nx.Graph(graph)
        pos = nx.spring_layout(G, seed=42)
        visited = set()
        stack = [(start, [start])]
        shortest_path = None
        
        start_time = time.time()
        
        fig = plt.figure("DFS Visualization")
        plt.ion()
        
        while stack:
            current, path = stack.pop()
            visited.add(current)
            
            plt.clf()
            nx.draw_networkx_nodes(G, pos, node_size=700, node_color='lightblue')
            nx.draw_networkx_edges(G, pos, width=1, alpha=0.3)
            nx.draw_networkx_labels(G, pos)
            
            nx.draw_networkx_nodes(G, pos, nodelist=visited, node_color='yellow')
            nx.draw_networkx_nodes(G, pos, nodelist=[current], node_color='red')
            
            if current == end:
                # Check for shortest DFS path (not guaranteed in pure DFS)
                if not shortest_path or len(path) < len(shortest_path):
                    shortest_path = path
                    path_edges = list(zip(path[:-1], path[1:]))
                    nx.draw_networkx_edges(G, pos, edgelist=path_edges, width=3, edge_color='red')
                    self.metrics.update({
                        'nodes_visited': len(visited),
                        'time': time.time() - start_time,
                        'path_length': len(path)
                    })
                    plt.title(f"DFS Complete (Path Length: {len(path)})", fontsize=12)
                    plt.pause(speed)
            
             # explore neighbors in reversed order
            for neighbor in reversed(graph[current]):
                if neighbor not in visited:
                    stack.append((neighbor, path + [neighbor]))
            
            plt.title(f"DFS Visiting Node {current}", fontsize=12)
            plt.pause(speed)
        
        plt.ioff()
        return self.metrics