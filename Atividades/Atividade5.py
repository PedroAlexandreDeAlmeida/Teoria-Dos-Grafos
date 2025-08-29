class GrafoDenso:
    # Construtor: inicializa a lista de vértices e a matriz de adjacência
    def __init__(self, labels=None):
        self.vertices = []
        self.matriz_adjacencia = []
        if labels is not None:
            for label in labels:
                self.adicionar_vertice(label)

    # Adiciona um vértice ao grafo
    def adicionar_vertice(self, label):
        if label in self.vertices:
            return
        self.vertices.append(label)
        for linha in self.matriz_adjacencia:
            linha.append(0)
        self.matriz_adjacencia.append([0] * len(self.vertices))

    # Adiciona uma aresta entre dois vértices
    def adicionar_aresta(self, v1, v2):
        if v1 in self.vertices and v2 in self.vertices:
            i = self.vertices.index(v1)
            j = self.vertices.index(v2)
            self.matriz_adjacencia[i][j] += 1
            if i != j:
                self.matriz_adjacencia[j][i] += 1

    # Imprime a matriz de adjacência
    def imprimir(self):
        print("Matriz de Adjacência:")
        print("   " + " ".join(self.vertices))
        for i, linha in enumerate(self.matriz_adjacencia):
            print(self.vertices[i], linha)

    # Verifica se o grafo é simples (sem laços e sem múltiplas arestas)
    def is_simples(self):
        for i in range(len(self.vertices)):
            if self.matriz_adjacencia[i][i] != 0:
                return False
            for j in range(i+1, len(self.vertices)):
                if self.matriz_adjacencia[i][j] > 1:
                    return False
        return True

    # Verifica se o grafo é nulo (sem arestas)
    def is_nulo(self):
        for i in range(len(self.vertices)):
            for j in range(len(self.vertices)):
                if self.matriz_adjacencia[i][j] != 0:
                    return False
        return True

    # Verifica se o grafo é completo (todos os vértices conectados entre si)
    def is_completo(self):
        for i in range(len(self.vertices)):
            for j in range(len(self.vertices)):
                if i != j and self.matriz_adjacencia[i][j] == 0:
                    return False
        return True


if __name__ == "__main__":
    vertices_labels = ['A', 'B', 'C', 'D']

    print("=== Testando Grafo Denso ===")
    g3 = GrafoDenso(labels=vertices_labels)
    g3.imprimir()
    print("Simples?", g3.is_simples())
    print("Nulo?", g3.is_nulo())
    print("Completo?", g3.is_completo())

    g3.adicionar_aresta('A', 'B')
    g3.adicionar_aresta('A', 'C')
    g3.adicionar_aresta('B', 'D')
    g3.adicionar_aresta('C', 'D')
    g3.imprimir()
    print("Simples?", g3.is_simples())
    print("Nulo?", g3.is_nulo())
    print("Completo?", g3.is_completo())

    g4 = GrafoDenso(labels=vertices_labels)
    for i in range(len(vertices_labels)):
        for j in range(i+1, len(vertices_labels)):
            g4.adicionar_aresta(vertices_labels[i], vertices_labels[j])
    g4.imprimir()
    print("Simples?", g4.is_simples())
    print("Nulo?", g4.is_nulo())
    print("Completo?", g4.is_completo())
