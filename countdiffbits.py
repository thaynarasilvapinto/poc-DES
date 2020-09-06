import sys

plain = sys.argv[1]
ciphered = sys.argv[2]

binplain = bin(int(plain, 16))[2:]
binciphered = bin(int(ciphered, 16))[2:]

diffs = 0

if len(binplain) < len(binciphered):
  binplain = ('0' * (len(binciphered) - len(binplain))) + binplain
elif len(ciphered) < len(binplain):
  binciphered = ('0' * (len(binplain) - len(binciphered))) + binciphered

print(plain + ':', binplain)
print(ciphered + ':', binciphered)

for i, bit in enumerate(binplain):
  if binplain[i] != binciphered[i]:
    diffs += 1

print('Difference percentual: %.2f%%' % (diffs / (len(binplain)) * 100) )
