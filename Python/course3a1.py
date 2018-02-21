import re

hand = open('regex_sum_67575.txt')
numlist = list()
for line in hand:
    line = line.rstrip()
    number = re.findall('[0-9]+', line)
    if len(number) == 0: continue
    for values in number:
        numlist.append(int(values))
print(sum(numlist))
