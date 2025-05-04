from class_a import die

def main():
    d = die()
    while True:
        d.roll()
        print(d)  # Uses __str__() as required
        if input("Roll again? (y/n): ").lower() != 'y':
            break

if __name__ == "__main__":
    main()