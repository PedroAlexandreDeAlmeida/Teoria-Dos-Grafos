from abc import ABC, abstractmethod
import itertools

class Grafo(ABC):
    def __init__(self):
        self.vertices = set()
        self.arestas = set()

    @abstractmethod
    def add_vertice(self, v):
        pass

    @abstractmethod
    def add_aresta(self, u, v):
        pass

    def get_vertices(self):
        return self.vertices

    def get_arestas(self):
        return self.arestas

    # Atividade 5: Métodos do grafo
    def is_simples(self):
        for u, v in self.arestas:
            if u == v or (v, u) in self.arestas:
                return False
        return True

    def is_nulo(self):
        return len(self.arestas) == 0

    def is_completo(self):
        n = len(self.vertices)
        return len(self.arestas) == n * (n - 1) // 2

    # Atividade 6: Métodos de subgrafos
    def is_subgrafo(self, H):
        return H.vertices.issubset(self.vertices) and H.arestas.issubset(self.arestas)

    def is_subgrafo_gerador(self, H):
        return self.is_subgrafo(H) and H.vertices == self.vertices

    def is_subgrafo_induzido(self, H):
        if not self.is_subgrafo(H):
            return False
        for u in H.vertices:
            for v in H.vertices:
                if u != v and (u, v) in self.arestas and (u, v) not in H.arestas and (v, u) not in H.arestas:
                    return False
        return True

    # Atividade 7: Verificar isomorfismo
    def is_isomorfo(self, outro_grafo):
        """
        Verifica se dois grafos são isomorfos usando força bruta
        com poda por invariantes.
        """
        if len(self.vertices) != len(outro_grafo.vertices):
            return False
        if len(self.arestas) != len(outro_grafo.arestas):
            return False
        if sorted([len([v for v in self.arestas if u in v]) for u in self.vertices]) != \
           sorted([len([v for v in outro_grafo.arestas if u in v]) for u in outro_grafo.vertices]):
            return False

        vertices_self = list(self.vertices)
        vertices_outro = list(outro_grafo.vertices)

        for perm in itertools.permutations(vertices_outro):
            mapping = dict(zip(vertices_self, perm))
            arestas_mapeadas = set()
            for u, v in self.arestas:
                arestas_mapeadas.add((mapping[u], mapping[v]))
                arestas_mapeadas.add((mapping[v], mapping[u]))

            if set(outro_grafo.arestas) == arestas_mapeadas:
                return True

        return False

class GrafoDenso(Grafo):
    def __init__(self):
        super().__init__()

    def add_vertice(self, v):
        self.vertices.add(v)

    def add_aresta(self, u, v):
        if u in self.vertices and v in self.vertices:
            self.arestas.add((u, v))

class GrafoEsparso(Grafo):
    def __init__(self):
        super().__init__()

    def add_vertice(self, v):
        self.vertices.add(v)

    def add_aresta(self, u, v):
        if u in self.vertices and v in self.vertices:
            self.arestas.add((u, v))

# ==============================
# Testes organizados por atividade
# ==============================

# Atividade 5: Testando is_simples(), is_nulo(), is_completo()
print("=== Atividade 5 ===")
grafo1 = GrafoEsparso()
for v in [1, 2, 3]:
    grafo1.add_vertice(v)

grafo1.add_aresta(1, 2)
grafo1.add_aresta(2, 3)

print("Grafo simples:", grafo1.is_simples())  # True
print("Grafo nulo:", grafo1.is_nulo())        # False
print("Grafo completo:", grafo1.is_completo()) # False

# Criando grafo completo
completo = GrafoEsparso()
for v in [1, 2, 3]:
    completo.add_vertice(v)

completo.add_aresta(1, 2)
completo.add_aresta(2, 3)
completo.add_aresta(1, 3)

print("Grafo completo:", completo.is_completo())  # True

# Atividade 6: Testando get_vertices(), get_arestas(), is_subgrafo(), is_subgrafo_gerador(), is_subgrafo_induzido()
print("\n=== Atividade 6 ===")
grafo2 = GrafoEsparso()
for v in [1, 2, 3, 4]:
    grafo2.add_vertice(v)

grafo2.add_aresta(1, 2)
grafo2.add_aresta(2, 3)
grafo2.add_aresta(3, 4)

grafo_sub = GrafoEsparso()
for v in [1, 2, 3]:
    grafo_sub.add_vertice(v)

grafo_sub.add_aresta(1, 2)
grafo_sub.add_aresta(2, 3)

print("Subgrafo:", grafo2.is_subgrafo(grafo_sub))              # True
print("Subgrafo gerador:", grafo2.is_subgrafo_gerador(grafo_sub))  # False
print("Subgrafo induzido:", grafo2.is_subgrafo_induzido(grafo_sub)) # True

# Atividade 7: Testando is_isomorfo()
print("\n=== Atividade 7 ===")
grafo3 = GrafoEsparso()
for v in ["A", "B", "C"]:
    grafo3.add_vertice(v)

grafo3.add_aresta("A", "B")
grafo3.add_aresta("B", "C")
grafo3.add_aresta("A", "C")

grafo4 = GrafoEsparso()
for v in [1, 2, 3]:
    grafo4.add_vertice(v)

grafo4.add_aresta(1, 2)
grafo4.add_aresta(2, 3)
grafo4.add_aresta(1, 3)

print("Grafo3 e Grafo4 são isomorfos:", grafo3.is_isomorfo(grafo4))  # True

# Exemplo de grafos não isomorfos
grafo5 = GrafoEsparso()
for v in ["X", "Y", "Z"]:
    grafo5.add_vertice(v)

grafo5.add_aresta("X", "Y")

print("Grafo3 e Grafo5 são isomorfos:", grafo3.is_isomorfo(grafo5))  # False
