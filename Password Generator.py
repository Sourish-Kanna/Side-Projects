import secrets
import string

class Password:
    def __init__(self, length: int = 12, uppercase: bool = True, symbols: bool = True) -> None:
        self.length = length
        self.use_uppercase = uppercase
        self.use_symbols = symbols

        self.base_characters: str = string.ascii_lowercase + string.digits

        if self.use_uppercase:
            self.base_characters += string.ascii_uppercase
        if self.use_symbols:
            self.base_characters += string.punctuation

    def generate(self) -> str:
        password: list[str] = []

        for i in range(self.length):
            password.append(secrets.choice(self.base_characters))

        return ''.join(password)
    
    def check_strength(self, password: str) -> bool:
        if len(password) < 16:
            return False
        if not any(char.isupper() for char in password):
            return False
        if not any(char in string.punctuation for char in password):
            return False
        return True

def main() -> None:
    password: Password = Password(length=20, uppercase=True, symbols=True)
    generated: str = password.generate()
    print('-'*50)
    print(f'{generated} ({len(generated)} chars)')
    print(f'Strength: {password.check_strength(generated)}')
    print('-'*50)

if __name__ == '__main__':
    main()