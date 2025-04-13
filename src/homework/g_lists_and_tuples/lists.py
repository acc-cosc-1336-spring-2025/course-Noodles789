def get_p_distance(list1, list2):
    if len(list1) != len(list2):
        raise ValueError("Needs to be same length")
    
    differences = sum(1 for a, b in zip(list1, list2) if a != b)
    return differences / len(list1)

def get_p_distance_matrix(lists):
    n = len(lists)
    distance_matrix = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(i + 1, n):
            distance = get_p_distance(lists[i], lists[j])
            distance_matrix[i][j] = distance
            distance_matrix[j][i] = distance

    return distance_matrix