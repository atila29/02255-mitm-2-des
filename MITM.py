import des
from des import DesKey
import ast 

key0 = DesKey(b"000000000000000000000000")
key1 = DesKey(b"111111111111111111111111")

key0.is_single()

encMSG0 = key0.encrypt(b"blablabla", padding=True)
encMSG1 = key1.encrypt(encMSG0)

def pad(key, size):
    padding = "".join(["0" for i in range(0, size - len(key)-8)])
    paddedKey = padding + key
    evenBytesPaddedKey = []
    for i in range(0,8):
        for j in range(0,7):
            evenBytesPaddedKey.append(paddedKey[i * 7 + j])
        evenBytesPaddedKey.append(str(evenBytesPaddedKey[i * 8: i * 8 + 7].count('1') % 2))

    evenBytesPaddedKey = "".join(evenBytesPaddedKey)
    evenBytesPaddedKey = int(evenBytesPaddedKey, 2)
    evenBytesPaddedKey = evenBytesPaddedKey.to_bytes(size // 8, byteorder='big')
    return evenBytesPaddedKey

keys = range(0, 2 ** 20)
# print(keys[3])
# print("{0:b}".format(keys[3]))
# print("{0:b}".format(23))

keysInBinary = [pad("{0:b}".format(k), 64) for k in keys]

k0 = pad("11101000011100010100", 64)
k1 = pad("10001101111111111111", 64)

print('keys')
print(k0)
print(k1)
print('end keys')

key0 = DesKey(k0)
key1 = DesKey(k1)

plaintext = b"dakkedak"

# encryptedTable = [[k, DesKey(k).encrypt(plaintext, padding = False)] for k in keysInBinary]

# with open("encryptedTable.txt", "w") as f:
#     for s in encryptedTable:
#         f.write(str(s) +"\n")

encryptedTable = []

with open("encryptedTable.txt", "r") as f:
    for line in f:
        encryptedTable.append(ast.literal_eval(line))

# encryptedTable.sort(lambda x: x[1])
print(type(encryptedTable[1]))
print(encryptedTable[2])
print(encryptedTable[3])

# des2
cipher = key1.encrypt(key0.encrypt(plaintext, padding=False), padding=False)
print(cipher)


# decryptedTable = [[k, DesKey(k).decrypt(cipher, padding = False)] for k in keysInBinary]
# # decryptedTable.sort(lambda x: x[1])
# print("step 2")

# with open("decryptedTable.txt", "w") as f:
#     for s in decryptedTable:
#         f.write(str(s) +"\n")

decryptedTable = []

with open("decryptedTable.txt", "r") as f:
    for line in f:
        decryptedTable.append(ast.literal_eval(line))

result = set(map(lambda x: x[1], encryptedTable)).intersection(map(lambda x: x[1], decryptedTable)).pop()
print(result)

encResult = filter(lambda entry: entry[1] == result, encryptedTable)
k0_entry = list(encResult)[0]

decResult = filter(lambda entry: entry[1] == result, decryptedTable)
k1_entry = list(decResult)[0]

print('our first entry')
print(k0_entry)

print('our second entry')
print(k1_entry)

