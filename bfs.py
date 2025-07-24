import matplotlib.pyplot as plt
import networkx as nx
from collections import deque
import time


class BFSVisualizer:
    
    def __init__(self):
    # Track performance metrics
        self.metrics = {
            'algorithm': 'BFS',
            'nodes_visited': 0,
            'time': 0,
            'path_length': 0
        }

    def visualize(self, graph, start, end, speed=1.0):
        """bFS visualizaton with adjustable speed"""
        G = nx.Graph(graph)
        pos = nx.spring_layout(G, seed=42)
        visited = set()
        queue = deque([(start, [start])])
        visited.add(start)
        
        start_time = time.time()
        
        fig = plt.figure("BFS Visualization")
        plt.ion()
        
        while queue:
            current, path = queue.popleft()
            
            # draw grap nodes and edges
            plt.clf()
            nx.draw_networkx_nodes(G, pos, node_size=700, node_color='lightblue')
            nx.draw_networkx_edges(G, pos, width=1, alpha=0.3)
            nx.draw_networkx_labels(G, pos)
            
            # highlights visited nodes, current node, and queue
            nx.draw_networkx_nodes(G, pos, nodelist=visited, node_color='yellow')
            nx.draw_networkx_nodes(G, pos, nodelist=[current], node_color='red')
            
            q_nodes = [n for n,_ in queue]
            nx.draw_networkx_nodes(G, pos, nodelist=q_nodes, node_color='green')
            
            
            if current == end:
                #found target, draw path
                path_edges = list(zip(path[:-1], path[1:]))
                nx.draw_networkx_edges(G, pos, edgelist=path_edges, width=3, edge_color='red')
                self.metrics.update({
                    'nodes_visited': len(visited),
                    'time': time.time() - start_time,
                    'path_length': len(path)
                })
                plt.title(f"BFS Complete (Path Length: {len(path)})", fontsize=12)
                plt.pause(speed)
                break
                
                     # explores the neighbors
            for neighbor in graph[current]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append((neighbor, path + [neighbor]))
            
            plt.title(f"BFS Visiting Node {current}", fontsize=12)
            plt.pause(speed)
        
        plt.ioff()
        return self.metrics