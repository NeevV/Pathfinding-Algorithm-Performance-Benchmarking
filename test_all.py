import time
import matplotlib.pyplot as plt
from bfs import BFSVisualizer
from dfs import DFSVisualizer
from bsi import BidirectionalVisualizer
from graph_generator import GraphGenerator

#configuration
ANIMATION_SPEED = 1.0  #seconds between steps (increase to slow down further)
TEST_GRAPH = GraphGenerator.generate_random_graph(10, 0.3)
START_NODE = 0
END_NODE = 9

def run_algorithm(visualizer, title):
    """Run algorithm with separate window and slower visualization"""
    plt.figure(title)  # creates a separate window
    visualizer.visualize(TEST_GRAPH, START_NODE, END_NODE, speed=ANIMATION_SPEED)
    plt.show(block=False)

def main():
    print("=== Pathfinding Visualizations ===")
    print(f"Testing on 10-node graph (Start: {START_NODE}, End: {END_NODE})")
    
    #create three separate windows
    run_algorithm(BFSVisualizer(), "BFS Visualization")
    run_algorithm(DFSVisualizer(), "DFS Visualization") 
    run_algorithm(BidirectionalVisualizer(), "Bidirectional Search Visualization")
    
    # kepep windows open
    print("\nAll visualizations are running in separate windows")
    plt.show()  # this blocks until all windows are closed

if __name__ == "__main__":
    main()