import random
symbols = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R' , 'S', 'T', 'U' , 'V', 'W', 'X', 'Y', 'Z', '.', '!', '?', '(', ')', '-']


# δημιουργει ενα τυχαίο δυαδικό αριθμό συγκεκριμένου μήκους bit, ώστε να χρησιμοποιηθει ως κλειδι του OTP
def random_binary(length):
    result = ""
    for i in range(length):
        result += str(random.randint(0, 1))
    return result

# μετατρεπει δεκαδικό αριθμό (str) σε 5-bit δυαδικό (str)
def decimal_to_binary(n):
    return bin(n).replace("0b", "").zfill(5)

# μετατρεπει δυαδικο αριθμό (str) σε δεκαδικό (str)
def binary_to_decimal(binary):
    return str(int(binary, 2))

# μετατρέπει κάθε χαρακτηρα σε δεκαδικό αριθμο βάση της αρχικης λιστας symbols και ύστερα απο δεκαδικό σε δυαδικό αριθμο(str) 
def text_to_binary(a):
    result = ""
    for char in a:
        result += decimal_to_binary(symbols.index(char))
    return result

# παίρνει ανα 5αδα τα ψηφια ενος δυαδικου αριθμου (str) και τα μετατρεπει σε δεκαδικους αριθμους και υστερα σε γραμματα απο την λιστα symbols
def binary_to_text(a):
    result = ""
    temp = ""
    for char in a:
        temp += char
        if len(temp) == 5:
            result += symbols[int(binary_to_decimal(temp))]
            temp = ""
    return result

# εφαρμόζει XOR σε δυο string (πηγή https://stackoverflow.com/questions/36242887/how-to-xor-two-strings-in-python)
def XOR(a, b):
    return ''.join([hex(ord(a[i%len(a)]) ^ ord(b[i%(len(b))]))[2:] for i in range(max(len(a), len(b)))])

# κρυπτογράφηση one time pad
def encryptOTP(m, k):
    c = binary_to_text(XOR(text_to_binary(m), k))
    return c

# αποκρυπτογράφηση one time pad
def decryptOTP(c, k):
    m = binary_to_text(XOR(text_to_binary(c), k))
    return m

#παράδειγμα
m = 'ITHINKCRYPTOGRAPHYISAMAZING!!!-'
k = random_binary(len(m)*5)
c = encryptOTP(m, k)
print("plaintext = ", m)
print("ciphertext = ", c)
print("plaintext2 = ", decryptOTP(c, k))
input("PRESS ENTER TO EXIT")
k = "" # destroy the key
