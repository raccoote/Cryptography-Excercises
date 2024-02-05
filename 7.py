# πηγή https://gist.github.com/hsauers5/491f9dde975f1eaa97103427eda50071
def key_scheduling(k):
    i = 0
    S = list(range(256))
    for j in range(0, 256):
        i = (i + S[j] + k[j % len(k)]) % 256
        tmp = S[j]
        S[j] = S[i]
        S[i] = tmp
    return S
    
def stream_generation(S):
    stream = []
    i = 0
    j = 0
    while True:
        i = (1 + i) % 256
        j = (S[i] + j) % 256
        tmp = S[j]
        S[j] = S[i]
        S[i] = tmp
        yield S[(S[i] + S[j]) % 256]

def encrypt(m, k):
    m = [ord(char) for char in m]
    k = [ord(char) for char in k]
    S = key_scheduling(k)
    key_stream = stream_generation(S)
    c = ''
    for char in m:
        enc = str(hex(char ^ next(key_stream))).upper()
        c += (enc)
    return c

def decrypt(c, k):
    c = c.split('0X')[1:]
    c = [int('0x' + char.lower(), 0) for char in c]
    k = [ord(char) for char in k]
    S = key_scheduling(k)
    key_stream = stream_generation(S)
    m = ""
    for char in c:
        dec = str(chr(char ^ next(key_stream)))
        m += dec
    return m

k = 'HOUSE'
m = 'MISTAKESAREASSERIOUSASTHERESULTSTHEYCAUSE'
c = encrypt(m, k)
print("c = ", c)
print("m = ", decrypt(c, k))
input("PRESS ENTER TO EXIT")


