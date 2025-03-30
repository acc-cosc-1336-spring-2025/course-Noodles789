import unittest
from tests.homework.h_strings import tests_strings

def get_hamming_distance(dna1: str, dna2: str) -> int:
    if len(dna1) != len(dna2):
        raise ValueError("DNA strings are not equal length")
    return sum(1 for a, b in zip(dna1, dna2) if a != b)
def get_dna_complement(dna: str) -> str:
    complement_map = {'A': 'T', 'T':'A', 'C':'G','G':'C'}
    return ''.join(complement_map[n] for n in reversed(dna))

class TestStrings(unittest.TestCase):
    def test_get_hamming_distance(self):
         self.assertEqual(get_hamming_distance("GAGCCTACTAACGGGAT", "CATCGTAATGACGGCCT"), 7)
    def test_get_dna_complement(self):
         self.assertEqual(get_dna_complement("AAAACCCGGT"),"ACCGGGTTTT")
suite = unittest.TestLoader().loadTestsFromModule(tests_strings)
unittest.TextTestRunner(verbosity=2).run(suite)
