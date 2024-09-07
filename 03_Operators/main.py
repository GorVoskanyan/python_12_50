# Arithmetic operators
# a = b = c = 1
# a, b = 5, 3

# print(a + b)
# print(a - b)

# print(a * b)
# print(a ** b)

# print(a / b)
# print(a // b)
# print(a % b)
# print(((a + b) * 3) ** (a / 2))


# Comparison operators
# a, b = 6, 5
# poqr = a < b
# mets = a > b

# poqr_kam_havasar = a <= b
# mets_kam_havasar = a >= b

# ardyoq_havasar_en = a == b
# havasar_chen = a != b
# print(not_equal)

# print(a + -b)


# --------------
surchi_gin = float(input('Mutqagreq surchi arjeqy: '))
gumar = float(input('Mutqagreq gumary: '))

gumar = gumar - surchi_gin

dram_500 = 500
dram_200 = 200
dram_100 = 100

qanak_500 = gumar // dram_500
gumar = gumar % dram_500
qanak_200 = gumar // dram_200
gumar = gumar % dram_200
qanak_100 = gumar // dram_100
gumar = gumar % dram_100

print('500 -', qanak_500)
print('200 -', qanak_200)
print('100 -', qanak_100)