from collections import Counter

# εφαρμόζει XOR σε δυο string (πηγή https://stackoverflow.com/questions/36242887/how-to-xor-two-strings-in-python)
def XOR(a, b):
    return ''.join([hex(ord(a[i%len(a)]) ^ ord(b[i%(len(b))]))[2:] for i in range(max(len(a), len(b)))])

# επιστρέφει τον πλήθος του πιο συχνού στοιχείου σε μια λίστα
def max_count_occurences(my_list):
    count = Counter(my_list)
    return max(count.most_common(), key=lambda x: x[1])[1]

# μετατρέπει ένα 6-bit σε 4-bit σύμφωνα με τον πίνακα S-box
def S(str_num, sbox):
    return sbox[int(str_num[0] + str_num[5], 2)][int(str_num[1:5], 2)]

# υπολογίζει το Differential Uniformity
def diff(sbox, n, max_diff = 0):
    for x in range(1, n):
        y = []
        for z in range(n): y.append(XOR(S(XOR("{0:06b}".format(z), "{0:06b}".format(x)), sbox), S("{0:06b}".format(z), sbox)))
        if max_count_occurences(y) > max_diff: max_diff = max_count_occurences(y)
    return max_diff

# το S-box που μας δόθηκε στην εκφώνηση
sbox = [["0000", "0010", "0011", "0111", "1001", "1100", "1111", "0111", "0110", "1111", "1111", "0001", "0111", "0011", "0001", "0000"],
        ["0001", "0101", "0110", "1101", "0100", "0001", "0101", "1011", "0111", "1000", "0111", "0001", "0001", "0011", "0010", "1101"],
        ["0101", "0011", "0101", "1100", "1011", "0001", "0001", "0101", "1101", "0000", "1111", "0111", "0010", "0010", "1101", "0000"],
        ["0011", "1100", "0011", "1011", "0010", "0010", "0010", "0100", "0110", "0101", "0101", "0000", "0100", "0011", "0001", "0000"]]
print("Differential Uniformity = " + str(diff(sbox, 64)))
input("PRESS ENTER TO EXIT")
