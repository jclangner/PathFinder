from math import inf, sqrt

def manhattan_distance(node1, node2):
    return abs(node1[0] - node2[0]) + abs(node1[1] - node2[1])

def euclidean_distance(node1, node2):
    return sqrt((node1[0] - node2[0])**2 + (node1[1] - node2[1])**2)

def neighbor_list(node, grid_length):
    to_remove = []
    neighbor_list = [(node[0]+1, node[1]), (node[0], node[1]+1), 
                     (node[0]-1, node[1]), (node[0], node[1]-1)]
    for node in neighbor_list:
        if (node[0] < 0 or node[0] == grid_length or node[1] < 0 or node[1] == grid_length):
            to_remove.append(node)
    for i in to_remove:
        neighbor_list.remove(i)
    return neighbor_list

def reconstruct_path(came_from, current):
    full_path = [current]

    while current in came_from.keys():
        current = came_from[current]
        full_path.append(current)

    return list(reversed(full_path))

def A_Star(start, end, grid, distance_metric=manhattan_distance):
    open_set = [start]
    closed_set = []
    came_from = {}
    g_score = {start: 0}
    f_score = {start: distance_metric(start, end)}
    forbidden_set = [(ix,iy) for ix, row in enumerate(grid) 
                    for iy, i in enumerate(row) if i == 1]

    while open_set:
        current = min(open_set, key=f_score.get)
        if current == end:
            return reconstruct_path(came_from, current), closed_set
            
        #print(open_set); print(current); print(f_score); print(came_from)
        open_set.remove(current)
        closed_set.append(current)
        for node in neighbor_list(current, len(grid)):
            if node not in forbidden_set:
                if node not in g_score:
                    g_score[node] = inf
                
                tentative_g_score = g_score[current] + distance_metric(current, node)
                if tentative_g_score < g_score[node]:
                    came_from[node] = current
                    g_score[node] = tentative_g_score
                    f_score[node] = g_score[node] + distance_metric(node, end)

                    if node not in open_set:
                        open_set.append(node)
    return 