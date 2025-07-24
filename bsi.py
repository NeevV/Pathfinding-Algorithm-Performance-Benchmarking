import matplotlib.pyplot as plt
import networkx as nx
from collections import deque
import time

class BidirectionalVisualizer:
    #tracks perforamce metrics
    def __init__(self):
        self.metrics = {
            'algorithm': 'Bidirectional',
            'nodes_visited': 0,
            'time': 0,
            'path_length': 0
        }

    def visualize(self, graph, start, end, speed=1.0):
        """bidirectional search with adjustable speed"""
        G = nx.Graph(graph)
        pos = nx.spring_layout(G, seed=42)
        
        # Initialize forward and backward search
        forward_visited = {start: [start]}
        forward_queue = deque([(start, [start])])
        
        #backward search
        backward_visited = {end: [end]}
        backward_queue = deque([(end, [end])])
        
        start_time = time.time()
        
        fig = plt.figure("Bidirectional Search Visualization")
        plt.ion()
        
        while forward_queue and backward_queue:
            #forward step
            f_node, f_path = forward_queue.popleft()
            
            plt.clf()
            nx.draw_networkx_nodes(G, pos, node_size=700, node_color='lightblue')
            nx.draw_networkx_edges(G, pos, width=1, alpha=0.3)
            nx.draw_networkx_labels(G, pos)
            
            nx.draw_networkx_nodes(G, pos, nodelist=forward_visited.keys(), node_color='orange')
            nx.draw_networkx_nodes(G, pos, nodelist=backward_visited.keys(), node_color='purple')
            nx.draw_networkx_nodes(G, pos, nodelist=[f_node], node_color='red')
            
            if f_node in backward_visited:
                 # meeting point found, reconstruct path
                final_path = f_path[:-1] + backward_visited[f_node][::-1]
                path_edges = list(zip(final_path[:-1], final_path[1:]))
                nx.draw_networkx_edges(G, pos, edgelist=path_edges, width=3, edge_color='red')
                self.metrics.update({
                    'nodes_visited': len(forward_visited) + len(backward_visited),
                    'time': time.time() - start_time,
                    'path_length': len(final_path)
                })
                plt.title(f"Bidirectional Complete (Path Length: {len(final_path)})", fontsize=12)
                plt.pause(speed)
                break
                
             # adds forward neighbors
            for neighbor in graph[f_node]:
                if neighbor not in forward_visited:
                    forward_visited[neighbor] = f_path + [neighbor]
                    forward_queue.append((neighbor, f_path + [neighbor]))
            
            #backward step
            b_node, b_path = backward_queue.popleft()
            
            if b_node in forward_visited:
                                # meeting point from backward side
                final_path = forward_visited[b_node][:-1] + b_path[::-1]
                path_edges = list(zip(final_path[:-1], final_path[1:]))
                nx.draw_networkx_edges(G, pos, edgelist=path_edges, width=3, edge_color='red')
                self.metrics.update({
                    'nodes_visited': len(forward_visited) + len(backward_visited),
                    'time': time.time() - start_time,
                    'path_length': len(final_path)
                })
                plt.title(f"Bidirectional Complete (Path Length: {len(final_path)})", fontsize=12)
                plt.pause(speed)
                break
                
            # add backward neighbors
            for neighbor in graph[b_node]:
                if neighbor not in backward_visited:
                    backward_visited[neighbor] = b_path + [neighbor]
                    backward_queue.append((neighbor, b_path + [neighbor]))
            
            plt.title("Bidirectional Search Progress", fontsize=12)
            plt.pause(speed)
        
        plt.ioff()
        return self.metrics