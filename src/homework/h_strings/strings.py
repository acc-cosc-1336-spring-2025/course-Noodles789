def get_hamming_distance(dna1: str, dna2: str) -> int:
    if len(dna1) != len(dna2):
        raise ValueError("DNA strings are not equal length")
    return sum(1 for a, b in zip(dna1, dna2) if a != b)
def get_dna_complement(dna: str) -> str:
    complement_map = {'A': 'T', 'T':'A', 'C':'G','G':'C'}
    return ''.join(complement_map[n] for n in reversed(dna))
