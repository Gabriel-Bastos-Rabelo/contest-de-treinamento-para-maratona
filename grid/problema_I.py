def area(x1, y1, x2, y2, x3, y3):
    return abs((x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2)) / 2.0)

def inside_quadrilateral(points, x, y):
    ax, ay, bx, by, cx, cy, dx, dy = points

    lista = []
    lista.append([ax, ay])
    lista.append([bx, by])
    lista.append([cx, cy])
    lista.append([dx, dy])

    inside = 0

    p1 = lista[0]
    for i in range(1, 5):
        p2 = lista[i % 4]
        if y > min(p1[1], p2[1]):
            # Check if the point is below the maximum y coordinate of the edge
            if y < max(p1[1], p2[1]):
                # Check if the point is to the left of the maximum x coordinate of the edge
                if x < max(p1[0], p2[0]):
                    # Calculate the x-intersection of the line connecting the point to the edge
                    x_intersection = (y - p1[1]) * (p2[0] - p1[0]) / (p2[1] - p1[1]) + p1[0]
 
                    # Check if the point is on the same line as the edge or to the left of the x-intersection
                    if p1[0] == p2[0] or x < x_intersection:
                        # Flip the inside flag
                        inside = 1 if inside == 0 else 1
 
        # Store the current point as the first point for the next iteration
        p1 = p2

    return inside


# Exemplo de uso
while True:
    try:
        
        pontos = list(map(int, input().split()))
        print(inside_quadrilateral(pontos[:8], pontos[8], pontos[9]))
    except EOFError:
        break

