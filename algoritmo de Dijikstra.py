import heapq

class Grafo:
    def __init__(self):
        self.rota = []
        self.vertices = {}

    def add_vertice(self, nome, vizinhos):
        self.vertices[nome] = vizinhos

    def dijkstra(self, inicio, fim):
        distancias = {inicio: 0}
        heap = [(0, inicio)]
        visitados = set()
        rota = True

        while heap:
            (dist, atual) = heapq.heappop(heap)

            if atual in visitados:
                continue

            visitados.add(atual)

            for proximo, peso in self.vertices[atual].items():
                distancia = dist + peso
                if proximo not in distancias or distancia < distancias[proximo]:
                    distancias[proximo] = distancia
                    heapq.heappush(heap, (distancia, proximo))

            if atual == fim:
                rota = False
            if rota:
                self.rota.append(atual)
        self.rota.append(fim)
        
        return distancias.get(fim)

grafo = Grafo()
grafo.add_vertice('A', {'B': 4, 'C': 1})
grafo.add_vertice('B', {'A': 4, 'C': 2, 'D': 5})
grafo.add_vertice('C', {'A': 1, 'B': 2, 'D': 1})
grafo.add_vertice('D', {'B': 5, 'C': 1})

print(grafo.dijkstra('A', 'D')) # Output: 3
print(grafo.rota)
