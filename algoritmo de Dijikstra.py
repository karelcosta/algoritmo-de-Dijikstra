import heapq

def dijkstra(grafo, start):
    dis = {no: float('inf') for no in grafo}  
    dis[start] = 0  
    heap = [(0, start)]  

    while heap:
        (dis_atual, no_atual) = heapq.heappop(heap)  
        if dis_atual > dis[no_atual]: 
            continue
        for vizinho, peso in grafo[no_atual].items():
            distancia = dis_atual + peso  
            if distancia < dis[vizinho]:  
                dis[vizinho] = distancia  
                heapq.heappush(heap, (distancia, vizinho))  

    menor_dis = sorted(dis.items(), key=lambda x: x[1])
    return menor_dis

# o dicionario grafo serve para informar todos os pontos e as distancias que ele tem para os proximos pontos
grafo = {
    'A': {'B': 7, 'C': 2},
    'B': {'A': 7, 'C': 2, 'D': 1},
    'C': {'A': 2, 'B': 2, 'D': 4, 'E': 3},
    'D': {'B': 1, 'C': 4, 'E': 3, 'F': 7},
    'E': {'C': 3, 'D': 3, 'F': 9},
    'F': {'D': 7, 'G': 4},
    'G': {'F': 4}
}

menor_dis = dijkstra(grafo, 'A')
print(menor_dis)  