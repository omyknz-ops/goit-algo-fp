import heapq

# Create weighted graph as adjacency list
def create_graph():
    
    graph = {
        'A': [('B', 5), ('C', 2)],
        'B': [('A', 5), ('C', 1), ('D', 3)],
        'C': [('A', 2), ('B', 1), ('D', 6), ('E', 4)],
        'D': [('B', 3), ('C', 6), ('E', 2)],
        'E': [('C', 4), ('D', 2)]
    }
    return graph


def dijkstra_with_heap(graph, start): # Initialize distances
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    
    paths = {vertex: [] for vertex in graph} # Initialize paths
    paths[start] = [start]
    
    # Priority queue (min-heap): (distance, vertex)
    heap = [(0, start)]
    visited = set()
    
    while heap:
        current_distance, current_vertex = heapq.heappop(heap)  # Extract vertex with minimum distance
        
        if current_vertex in visited: # Skip if already visited
            continue
        
        visited.add(current_vertex)
        
        for neighbor, weight in graph[current_vertex]:  # Check all neighbors
            distance = current_distance + weight
            
            if distance < distances[neighbor]: # If found shorter path
                distances[neighbor] = distance
                paths[neighbor] = paths[current_vertex] + [neighbor]
                heapq.heappush(heap, (distance, neighbor)) # Add neighbor to heap
    
    return distances, paths


# Create graph
graph = create_graph()

# Run Dijkstra from vertex 'A'
start_vertex = 'A'
distances, paths = dijkstra_with_heap(graph, start_vertex)

print("=" * 60)
print(f"DIJKSTRA'S ALGORITHM WITH BINARY HEAP")
print(f"Starting from vertex: {start_vertex}")
print("=" * 60)

for vertex in sorted(distances.keys()):
    if vertex != start_vertex:
        path = ' -> '.join(paths[vertex])
        print(f"\nTo {vertex}:")
        print(f"  Shortest distance: {distances[vertex]}")
        print(f"  Path: {path}")