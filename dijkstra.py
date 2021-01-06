from heapq import heappush, heappop


def dijkstra(graph, start):

    visited = [0] * len(graph)
    distances = [(float('inf'), -1)] * len(graph)
    distances[start] = (0, -1)
    heap = []
    heappush(heap, (distances[start], start))

    while heap:
        path, vertex_from = heappop(heap)
        if not visited[vertex_from]:
            visited[vertex_from] = 1
            for vertex_to in graph[vertex_from]:
                path, previous = distances[vertex_to]
                new_path = (
                    distances[vertex_from][0] + graph[vertex_from][vertex_to]
                )
                if path > new_path:
                    distances[vertex_to] = (new_path, vertex_from)
                if not visited[vertex_to]:
                    heappush(heap, (distances[vertex_to], vertex_to))
    return distances


if __name__ == '__main__':
    with open('input.txt', 'r') as file:
        vertices, edges = map(int, file.readline().split())
        start, destination = map(int, file.readline().split())
        graph = [{} for _ in range(vertices)]
        for _ in range(edges):
            vert1, vert2, weight = map(int, file.readline().split())
            graph[vert1][vert2] = weight
            graph[vert2][vert1] = weight
    distanses = dijkstra(graph, start)
    if distanses[destination][0] == float('inf'):
        print(-1)
    else:
        final_distance, previous = distanses[destination]
        route = [destination]
        while previous != -1:
            route.append(previous)
            _, previous = distanses[previous]

        print(final_distance)
        print(len(route))
        print(' '.join(map(str, route[::-1])))

