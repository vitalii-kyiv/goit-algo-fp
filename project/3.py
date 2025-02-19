import heapq

def dijkstra(graph, start):
    """
    Алгоритм Дейкстри для знаходження найкоротших шляхів у зваженому графі.
    Використовує бінарну купу для ефективного вибору вершин.
    
    :param graph: Словник, що представляє граф (формат {вузол: [(сусід, вага), ...]})
    :param start: Початковий вузол
    :return: Словник найкоротших шляхів {вузол: відстань}
    """
    priority_queue = []
    heapq.heappush(priority_queue, (0, start))
    shortest_paths = {node: float('inf') for node in graph}
    shortest_paths[start] = 0
    
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        
        if current_distance > shortest_paths[current_node]:
            continue
        
        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight
            if distance < shortest_paths[neighbor]:
                shortest_paths[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return shortest_paths

def main():
    """
    Тестування алгоритму Дейкстри на зваженому графі.
    """
    graph = {
        'A': [('B', 1), ('C', 4)],
        'B': [('A', 1), ('C', 2), ('D', 5)],
        'C': [('A', 4), ('B', 2), ('D', 1)],
        'D': [('B', 5), ('C', 1)]
    }
    start_node = 'A'
    shortest_paths = dijkstra(graph, start_node)
    print("Найкоротші шляхи від вузла", start_node, ":", shortest_paths)

if __name__ == "__main__":
    main()
