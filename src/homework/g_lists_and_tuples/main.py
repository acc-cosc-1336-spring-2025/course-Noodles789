from lists import get_p_distance_matrix

def main():
    while True:
        print("\n1 - Get p distance matrix\n2 - Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            n = int(input("Number of DNA strings: "))
            sequences = [list(input(f"DNA string {i+1}: ").strip()) for i in range(n)]
            matrix = get_p_distance_matrix(sequences)
            for row in matrix:
                print(" ".join(f"{x:.5f}" for x in row))
        elif choice == "2":
            break

main()