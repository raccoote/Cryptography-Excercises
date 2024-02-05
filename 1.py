
# α -> 1, β -> 2, ..., ω -> 24
def greek_to_num(char):
    if ord(char) < 962: return ord(char) - 944
    return ord(char) - 945

# 1 -> α, 2 -> β, ..., 24 -> ω
def num_to_greek(num):
    if num < 18: return chr(num + 944) 
    return chr(num + 945)

def f(x):
    return x**5 + 3*x**3 + 7*x**2 + 3*x**4 + 5*x + 4


x0 = (-3 - 5**(1/2))/2   #  or x0 = (-3 + 5**(1/2))/2
c = 'οκηθμφδζθγοθχυκχσφθμφμχγ'


for char in c: print(num_to_greek(int(((greek_to_num(char) - f(x0)) % 24) + 1)), end="")
input("\nPRESS ENTER TO EXIT")

