import des
from des import DesKey

key0 = DesKey(b"000000000000000000000000")
key1 = DesKey(b"111111111111111111111111")

key0.is_single()

encMSG0 = key0.encrypt(b"blablabla", padding=True)
encMSG1 = key1.encrypt(encMSG0)

def pad(key, size):
    padding = "".join(["0" for i in range(0, size - len(key))])
    paddedKey = padding + key
    evenBytesPaddedKey = []
    for i in range(0,8):
        for j in range(0,7):
            evenBytesPaddedKey.append(paddedKey[i * 7 + j])
            print(paddedKey[i * 7 + j], end = '')
        print(str(evenBytesPaddedKey[i * 8: i * 8 + 7].count('1') % 2))
        evenBytesPaddedKey.append(str(evenBytesPaddedKey[i * 8: i * 8 + 7].count('1') % 2))

    evenBytesPaddedKey = "".join(evenBytesPaddedKey)
    evenBytesPaddedKey = int(evenBytesPaddedKey, 2)
    evenBytesPaddedKey = evenBytesPaddedKey.to_bytes(8, byteorder='big')
    print(evenBytesPaddedKey)
    return evenBytesPaddedKey

print(len(pad("11101000011100010100", 56)))
key0 = DesKey(pad("11101000011100010100", 56))
#key1 = DesKey(pad("10001101111111111111", 56))
