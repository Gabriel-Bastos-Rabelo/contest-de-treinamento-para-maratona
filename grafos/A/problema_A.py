def fluxo_maximo(grafo, fonte, destino):
    # Encontrar um caminho de aumento
    def encontrar_caminho(capacidade_residual, u, v):
        if u == destino:
            return v
        for vizinho in grafo[u]:
            if capacidade_residual[u][vizinho] > 0:
                caminho = encontrar_caminho(capacidade_residual, vizinho, v)
                if caminho is not None:
                    return [u] + caminho
        return None

    # Algoritmo de Ford-Fulkerson
    fluxo = 0
    capacidade_residual = grafo.copy()
    while True:
        caminho = encontrar_caminho(capacidade_residual, fonte, destino)
        if caminho is None:
            break
        capacidade_minima = min(capacidade_residual[u][v] for u, v in zip(caminho[:-1], caminho[1:]))
        for u, v in zip(caminho[:-1], caminho[1:]):
            capacidade_residual[u][v] -= capacidade_minima
            capacidade_residual[v][u] += capacidade_minima
        fluxo += capacidade_minima
    return fluxo

# Leitura da entrada
n, m = map(int, input().split())
grafo = [[] for _ in range(n + 1)]
for _ in range(m):
    x, y, p = map(int, input().split())
    grafo[x].append(y)
    grafo[y].append(x)

# Cálculo do fluxo máximo
resultado = fluxo_maximo(grafo, 1, n)

# Impressão da saída
print(resultado)
