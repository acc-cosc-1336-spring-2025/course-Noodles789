
def get_lowest_list_value(first):
    if not first:
        raise ValueError("there is no list, try again")
    lowest = first[0]
    for num in first[1:]:
        if num < lowest:
            lowest = num
            return lowest
        
def get_highest_list_value(first):
    if not first:
        raise ValueError("there is no list, try again")
    highest = first[0]
    for num in first[1:]:
        if num > highest:
            highest = num
        return highest
def main():
    while True:
        print("\n1-Show the list low/high values")
        print("2-Exit")
        choice = input("Choose an option: ")

        if choice == "2":
            print("Exiting program.")
            break

        elif choice == "1":
            numbers = []
            while True:
                try:
                    num = int(input("Enter a list value: "))
                    numbers.append(num)
                    if len(numbers) >= 3:
                        cont = input("Do you want to enter another value? (yes/no): ")
                        if cont.lower() != "yes":
                            break
                except ValueError:
                    print("Invalid input. Please enter a number.")

            if numbers:
                print(f"Lowest value: {get_lowest_list_value(numbers)}")
                print(f"Highest value: {get_highest_list_value(numbers)}")
            else:
                print("No values were entered.")
        else:
            print("Invalid option. Please try again.")



main()