import sys

file1 = sys.argv[1]
file2 = sys.argv[2]

with open(file1, 'rb') as f1:
  plain = f1.read()

with open(file2, 'rb') as f2:
  ciphered = f2.read()

binplain = ''
for byte in plain:
  print(chr(byte), byte)
  binbyte = bin(byte)[2:]
  if len(binbyte) < 8:
    binbyte = '0' * (8 - len(binbyte)) + binbyte
  binplain += binbyte
print(len(binplain), 'in:', binplain)

binciphered = ''
for byte in ciphered[:8]:
  binbyte = bin(byte)[2:]
  if len(binbyte) < 8:
    binbyte = '0' * (8 - len(binbyte)) + binbyte
  binciphered += binbyte[:64]
print(len(binciphered), 'out:',  binciphered)

diffs = 0

for i, bit in enumerate(binplain):
  if binplain[i] != binciphered[i]:
    diffs += 1

print('Difference percentual: %.2f%%' % (diffs / (len(binplain)) * 100) )
