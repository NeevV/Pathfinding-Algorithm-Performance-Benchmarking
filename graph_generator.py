import random

class GraphGenerator:
    @staticmethod
    def generate_random_graph(num_nodes, edge_prob=0.3):
        # Create a random undirected graph
        graph = {i: [] for i in range(num_nodes)}
        for i in range(num_nodes):
            for j in range(i+1, num_nodes):
                if random.random() < edge_prob:
                    graph[i].append(j)
                    graph[j].append(i)
        return graph

    @staticmethod
    def generate_grid_graph(rows, cols):
        #create a 2D grid graph
        graph = {}
        for i in range(rows):
            for j in range(cols):
                node = i*cols + j
                neighbors = []
                if i > 0: neighbors.append((i-1)*cols + j)
                if i < rows-1: neighbors.append((i+1)*cols + j)
                if j > 0: neighbors.append(i*cols + (j-1))
                if j < cols-1: neighbors.append(i*cols + (j+1))
                graph[node] = neighbors
        return graph