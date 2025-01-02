from collections import Counter
import re


def get_frequency(text: str) -> list[tuple[str, int]]:
    lowered_text: str = text.lower()
    words: list[str] = re.findall(r'\b\w+\b', lowered_text)
    word_counts: Counter = Counter(words)
    return word_counts.most_common()


def main() -> None:
    print('-'*50)
    ask_open_file:str = input('Do you want to open a file? (y/n): ').lower()
    if ask_open_file == 'y':
        from tkinter.filedialog import askopenfilename
        filename = askopenfilename()
        with open(filename, 'r') as file:
            text = file.read()
    else:
        text: str = input('Enter your text: ')
    word_frequencies: list[tuple[str, int]] = get_frequency(text)
    for word, count in word_frequencies:
        print(f'{word}: {count}')
    print('-'*50)


if __name__ == "__main__":
    main()
