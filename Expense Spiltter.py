def calculate_split(total_amount: float, number_of_people: int, type_of_split:str, split_share:list[float], currency: str) -> None:
    if number_of_people < 1:
        raise ValueError('Number of people must be greater than one.')
    
    print(f'Total expense: {currency}{total_amount:,.2f}')
    print(f'Number of people: {number_of_people}')

    if type_of_split == "N":
        share_per_person: float = total_amount / number_of_people
        print(f'Each person should pay: {currency}{share_per_person:,.2f}')

    else:
        for index,share in enumerate(split_share):
            print(f"Person {index+1}: {currency}{total_amount*(share/100)}")

    print('-'*50,end="\n\n")


def main() -> None:
    try:
        print('-'*50)
        total_amount: float = float(input('Enter the total amount of the expense: '))
        number_of_people: int = int(input('Enter the number of people sharing the expense: '))
        type_of_split:str = input('Do you want to split unevenly? \nType "Y" or "N": ').upper()
        split_share: list[float] = []
        if type_of_split == "Y":
            split_share = [float(i) for i in input("Enter Shares with space in between: ").split()]
        calculate_split(total_amount, number_of_people, type_of_split, split_share, currency='₹')

    except ValueError as e:
        print("Enter Correct Value")
        main()


if __name__ == '__main__':
    main()
