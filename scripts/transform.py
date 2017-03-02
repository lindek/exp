import re
import sys
import collections

digit=re.compile('[0-9]')

vocab = set()
total = 0.0;
vocab_size = int(sys.argv[2])

for i, line in enumerate(open(sys.argv[1])):
    if i < vocab_size:
        fields = line.strip().split('\t')
        vocab.add(fields[0])
out = []
for line in sys.stdin:
    words = line.strip().split()
    sentence = []
    unk = 0;
    for word in words:
        word = re.sub(digit, '0', word).lower()
        if word in vocab:
            sentence.append(word)
        else:
            sentence.append("<unk>")
            unk += 1
    if unk < 0.1 * len(sentence):
        out.append(' '.join(sentence))

print(' <eos> '.join(out))


