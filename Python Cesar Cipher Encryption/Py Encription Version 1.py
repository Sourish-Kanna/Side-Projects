Cap = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
Num = ' 0123456789_-=+/*'
LETTERS = Cap+Num+Cap.lower()
end = len(LETTERS)

def encrypt(message, key):
    encrypted = ''
    for chars in message:
        if chars in LETTERS:
            num = LETTERS.find(chars)
            num += key
            if num>end-1:
                num-=end
                encrypted +=  '?'
            encrypted +=  LETTERS[num]
    return encrypted

def decrypt(message, key):
    decrypted = ''
    cc=0
    for chars in message:
        if chars in LETTERS:
            num = LETTERS.find(chars)
            num -= key
            if chars=="?":
                cc=1
                pass
            if cc==1:
                num=end-num
                cc=0
            decrypted +=  LETTERS[num]
    return decrypted

if __name__ == '__main__':

    message = str(input('Enter your message: '))
    key = int(input('Enter you key [1 - 26]: '))
    choice = input('Encrypt or Decrypt? [E/D]: ')

    if choice.lower().startswith('e'):
        print('Your code',encrypt(message, key))
    else:
        print('Your message ',decrypt(message, key))