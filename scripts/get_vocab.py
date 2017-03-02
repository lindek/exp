import re
import sys
import collections

digit=re.compile('[0-9]')

counts = collections.Counter()
total = 0.0;
for line in sys.stdin:
    for word in line.strip().split(' '):
        if word != '':
            counts[re.sub(digit, '0', word).lower()] += 1
            total += 1
words = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
s = 0
for i, (word, count) in enumerate(words[0:10000]):
    s += count
    print("%s\t%d\t%d\t%f" % (word, i, count, s / total))

