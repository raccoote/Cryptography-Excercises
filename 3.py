# εφαρμόζει XOR σε δυο string (πηγή https://stackoverflow.com/questions/36242887/how-to-xor-two-strings-in-python)
def XOR(a, b):
    return ''.join([hex(ord(a[i%len(a)]) ^ ord(b[i%(len(b))]))[2:] for i in range(max(len(a), len(b)))])

# κυκλικη κύλιση προς τα αριστερα κατα a bits
def shift_left(str1, a):
    return str1[a:] + str1[:a]

# κυκλικη κύλιση προς τα δεξια κατα a bits
def shift_right(str1, a):
    return str1[-a:] + str1[:-a]

# αποκωδικοποίηση βαση του τυπου που υπολόγισα
def decipher(a):
    return XOR(XOR(XOR(XOR(a, shift_left(a, 2)), shift_right(a, 2)), shift_right(a, 4)), shift_right(a, 12))

# κωδικοποίηση βαση του τυπου που δινεται στην εκφωνηση
def encode(a):
    return XOR(XOR(a, shift_left(a, 6)), shift_left(a, 10))


m = '0111001110101011'  # αρχικο μηνυμα 16-bits
print( m == decipher(encode(m)))
input("PRESS ENTER TO EXIT")
