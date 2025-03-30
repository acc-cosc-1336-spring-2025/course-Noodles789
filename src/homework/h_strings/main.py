def handle_hamming_distance():
    dna1 = input("Enter The First DNA String")
    dna2 = input("Enter The Second DNA String")
    if len(dna1) != len(dna2):
        print("DNA strings must be of equal length!")
        return

    hamming_distance = 0
    for i in range(len(dna1)):
        if dna1[i] != dna2[i]:
            hamming_distance += 1
    
    print(f"Hamming Distance: {hamming_distance}")
def get_dna_complement(dna: str) -> str:
    complement_map = {'A': 'T', 'T':'A', 'C':'G','G':'C'}
    return ''.join(complement_map[n] for n in reversed(dna))


def handle_dna_complement():
    dna = input("Enter A DNA String")
    complement = get_dna_complement(dna)
    print(f"DNA Complement: {complement}")
def goodbye():
    print("GOODBYE")

def main():
    options = {
        "1": handle_hamming_distance,
        "2": handle_dna_complement,
        "3": goodbye
    }

    while True:
        print("1 - Hamming Distance")
        print("2 - DNA Complement")
        print("3 - EXIT")
        num = input("Enter a Number")
        if num == "3":
            options[num]()
            break
        elif num in options:
            options[num]()
        else:
            print("Invalid, try it again")

main()