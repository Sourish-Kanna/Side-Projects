Cap = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
Num = ' 0123456789_-=+/*'
LETTERS = Cap+Num+Cap.lower()
end = len(LETTERS)

def encrypt(message):
    encrypted = []
    for chars in message:
        txt=ord(chars)
        encrypted.append(txt)
    return encrypted

def decrypt(message):
    decrypted = ''
    cc=0
    for chars in message:
        txt=chr(chars)
        decrypted += txt
    return decrypted

if __name__ == '__main__':
    message = str(input('Enter your message: '))
    choice = input('Encrypt or Decrypt? [E/D]: ')

    if choice.lower()=="e":
        print('Your code',encrypt(message))
    else:
        print('Your message ',decrypt(eval(message)))
