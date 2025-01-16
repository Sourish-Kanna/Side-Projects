import json

def load_rates(json_file: str) -> dict[str, dict]:
    with open(json_file, 'r') as file:
        return json.load(file)

def convert(amount: float, base: str, to: str, rates: dict[str, dict]) -> float:

    base = base.lower()
    to = to.lower()

    from_rates: dict | None = rates.get(base)
    to_rates: dict | None = rates.get(to)

    if base == 'eur':
        return amount * to_rates['rate']  # type: ignore
    else:
        return amount * (to_rates['rate'] / from_rates['rate'])  # type: ignore

def main() -> None:
    rates: dict[str, dict] = load_rates('rates.json')

    result: float = convert(amount=75, base='eur', to='dkk', rates=rates)
    print(result)

if __name__ == '__main__':
    main()

"""
Homework:
1. Right now it works fine if you insert a rate that exists, but make it so that if the user
enters a rate that doesn't exist, the program tells them that the currency is invalid, then
show them a list of all the valid currency options.
2. Edit the script so that the "to" currency can also be specified as euro. 
3. [Hard] Instead of loading the data from a local JSON file, try loading the data from an API. 
This task will require you to search online for a free API for currency exchange rates, and to make
a request to it so that you can load that data in this script. 

"""