def get_city_most_connections(train_data: list[tuple[int,int]]) -> int:
    connections = {}
    
    for connection in train_data:
        source_city = connection[0]
        if source_city not in connections:
            connections[source_city] = 1
        else:
            connections[source_city] += 1
    
    max_connections = 0
    max_city = 0
    for city, num_connections in connections.items():
        if num_connections > max_connections:
            max_connections = num_connections
            max_city = city
            
    return max_city