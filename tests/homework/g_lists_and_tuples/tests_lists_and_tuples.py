import unittest
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
class TestListsAndTuples(unittest.TestCase):

    def test_p_distance(self):
        List1 = ['T', 'T', 'T', 'C', 'C', 'A', 'T', 'T', 'T', 'A']
        List2 = ['G', 'A', 'T', 'T', 'C', 'A', 'T', 'T', 'T', 'C']
        
        # Expected p-distance: 0.4
        self.assertAlmostEqual(get_p_distance(List1, List2), 0.4, places=3)

    def test_p_distance_matrix(self):
        lists = [
            ['T', 'T', 'T', 'C', 'C', 'A', 'T', 'T', 'T', 'A'],
            ['G', 'A', 'T', 'T', 'C', 'A', 'T', 'T', 'T', 'C'],
            ['T', 'T', 'T', 'C', 'C', 'A', 'T', 'T', 'T', 'T'],
            ['G', 'T', 'T', 'C', 'C', 'A', 'T', 'T', 'T', 'A']
        ]
        
        expected_matrix = [
            [0.0, 0.4, 0.1, 0.1],
            [0.4, 0.0, 0.4, 0.3],
            [0.1, 0.4, 0.0, 0.2],
            [0.1, 0.3, 0.2, 0.0]
        ]
        
        result_matrix = get_p_distance_matrix(lists)
        
        for i in range(len(expected_matrix)):
            for j in range(len(expected_matrix[i])):
                self.assertAlmostEqual(result_matrix[i][j], expected_matrix[i][j], places=3)