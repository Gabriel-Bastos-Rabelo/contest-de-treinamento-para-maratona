def flood_fill(matriz, x, y, n, m, visited):
    if (x, y) in visited:
        return
    if x < 0 or x >= n or y < 0 or y >= m or matriz[x][y] == 'X':
        return  # Fora dos limites ou não é uma célula vazia
    
    matriz[x][y] = 'T'  # Marca a célula atual como inundada
    # Repete o processo para todas as células adjacentes
    visited.add((x, y))
    flood_fill(matriz, x + 1, y, n, m, visited)
    flood_fill(matriz, x - 1, y, n, m, visited)
    flood_fill(matriz, x, y + 1, n, m, visited)
    flood_fill(matriz, x, y - 1, n, m, visited)

def process_map(n, m, mapa):
    for i in range(n):
        for j in range(m):
            if mapa[i][j] == 'T':  # Encontra um ponto de vazamento
                visited = set()
                flood_fill(mapa, i, j, n, m, visited)  # Inicia o preenchimento a partir deste ponto
    
    # Imprime o mapa após a aplicação do flood fill
    for linha in mapa:
        print("".join(linha))
    print()  # Linha em branco após cada mapa

# Exemplo de como você processaria a entrada
# Substitua esta parte pela leitura real da entrada
entradas = [
    (6, 7, ["XXAAXXX", "XXAAXAX", "XXXXAXX", "XAAAAAX", "TAAXAAA", "XXXXXXX"]),
    (3, 3, ["TTT", "XXX", "AAA"])
]

for n, m, mapa_str in entradas:
    mapa = [list(linha) for linha in mapa_str]  # Converte cada string do mapa para uma lista de caracteres
    process_map(n, m, mapa)
