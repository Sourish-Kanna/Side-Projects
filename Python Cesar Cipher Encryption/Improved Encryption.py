Cap = 'QWERTYUIOPASDFGHJKLZXCVBNM'
Num = '0123456789'
Sym = '_-=+/*!@#$%^&:;"\'\\<>,.?`()}{[] '
LETTERS = Cap+Num+Cap.lower()+Sym
end = len(LETTERS)

def encrypt(message, key):
    encrypted = ''
    encrypted_next = []
    for chars in message:
        if chars in LETTERS:
            num = LETTERS.find(chars)
            num += key
            if num>end-1:
                num-=end
                encrypted +=  '~'
            encrypted +=  LETTERS[num]
    for chars in encrypted:
        txt=ord(chars)
        encrypted_next.append(txt)

    return encrypted_next

def decrypt(message, key):
    decrypted = ''
    decrypted_next = ''
    cc=0
    for chars in message:
        txt=chr(chars)
        decrypted_next += txt
    for chars in decrypted_next:
        if chars in LETTERS:
            num = LETTERS.find(chars)
            num -= key
            if chars=="~":
                cc=1
                pass
            if cc==1:
                num=end-num
                cc=0
            decrypted +=  LETTERS[num]

    return decrypted


message = str(input('Enter your message: '))
key = int(input('Enter you key [1 - 26]: '))
choice = input('Encrypt or Decrypt? [E/D]: ')

if choice.lower().startswith('e'):
    print('Your code',encrypt(message, key))
else:
    print('Your message ',decrypt(eval(message), key))
