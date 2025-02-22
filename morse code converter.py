morse_code_dict: dict[str, str] = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..',
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----',
    ' ': '/', '!': '-.-.', '?': '..--..', ',': '--..--', '.': '.-.-.-', 
    ':': '---...', "'": '.----.', '-': '-....-', '/': '-..-.', '@': '.--.-.', 
    ')': '-.--.-', '&': '.-...', ';': '-.-.-.', '=': '-...-', '_': '..--.-',
    '+': '.-.-.', '$': '...-..-', '"': '.-..-.','(': '-.--.', '%': '...-.',
    '*': '-..-', '#': '...-.-', '~': '.-...', '^': '..--', '`': '.--..',
    '<': '----', '>': '----.', '[': '-.--.', ']': '-.--.-', '{': '-.--.',
    '}': '-.--.-', '\\': '.----.', '|': '.-...',
}

def convert_to_morse(text: str) -> str:
    return ' '.join(morse_code_dict.get(char.upper(), '') for char in text)

def convert_from_morse(morse_code: str) -> str:
    reverse_morse_code_dict: dict[str, str] = {value: key for key, value in morse_code_dict.items()}
    return ''.join(reverse_morse_code_dict.get(code, '') for code in morse_code.split(' '))

def main() -> None:
    test_text: str = input("Enter text to convert to Morse code: ")
    converted_morse: str = convert_to_morse(test_text)
    print(f"Text to Morse: {converted_morse}")
    reverted_text: str = convert_from_morse(converted_morse)
    print(f"Morse to Text: {reverted_text}")
    print('-'*50, end="\n\n")

if __name__ == "__main__":
    main()