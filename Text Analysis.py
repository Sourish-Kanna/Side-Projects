from collections import Counter

def open_file(path: str) -> str:
    with open(path, 'r') as file:
        text: str = file.read()
        return text

def analyse(text: str) -> dict[str, int|list]:
    most_common =   Counter(text.split()).most_common(5)
    result: dict[str, int|list] = {
        'Total Characters (including spaces)': len(text),
        'Total Characters (excluding spaces)': len(text.replace(' ', '')),
        'Total Spaces': text.count(' '),
        'Total Words': len(text.split()),
        'Most Common Words': [word for word, _ in most_common]
    }
    return result

def main() -> None:
    print('-'*50)
    text: str = open_file(path='note.txt')
    print(f'Text: "{text}"')
    analysis: dict[str, int|list] = analyse(text.lower())
    print("This text file contains:")
    for key, value in analysis.items():
        print(f'{key}: {value}')
    print('-'*50)

if __name__ == '__main__':
    main()
