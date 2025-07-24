from graph_generator import GraphGenerator

test_graphs = [
    {
        'name': 'Small Sparse (10 nodes)',
        'graph': GraphGenerator.generate_random_graph(10, 0.2),
        'start': 0,
        'end': 9
    },
    {
        'name': 'Medium Dense (15 nodes)',
        'graph': GraphGenerator.generate_random_graph(15, 0.4),
        'start': 0,
        'end': 14
    },
    {
        'name': '3x5 Grid',
        'graph': GraphGenerator.generate_grid_graph(3, 5),
        'start': 0,
        'end': 14
    }
]

performance_results = []

def add_result(result):
    """Store results with test case info"""
    performance_results.append(result)
    print(f"{result['algorithm']} on {result['test_name']}: "
          f"Visited {result['nodes_visited']} nodes, "
          f"Time {result['time']:.3f}s, "
          f"Path length {result['path_length']}")

def generate_report():
    """Generate performance report"""
    if not performance_results:
        print("No results to report")
        return
    
    print("\nPerformance Summary:")
    print("{:<15} {:<20} {:<10} {:<10} {:<10}".format(
        "Algorithm", "Test Case", "Visited", "Time(s)", "Path Len"))
    print("-"*65)
    
    for algo in {r['algorithm'] for r in performance_results}:
        algo_results = [r for r in performance_results if r['algorithm'] == algo]
        avg_visited = sum(r['nodes_visited'] for r in algo_results)/len(algo_results)
        avg_time = sum(r['time'] for r in algo_results)/len(algo_results)
        avg_path = sum(r['path_length'] for r in algo_results)/len(algo_results)
        
        print("{:<15} {:<20} {:<10.1f} {:<10.3f} {:<10.1f}".format(
            algo, "Average", avg_visited, avg_time, avg_path))

if __name__ == "__main__":
    print("Test cases loaded successfully!")
    print(f"Available test graphs: {[t['name'] for t in test_graphs]}")