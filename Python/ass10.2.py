name = input('Enter file name:')
if len(name) < 1 : name = 'mbox-short.txt'
handle = open(name)

zeropos = 0
#create data structures and populate with emails
hours = dict()
for line in handle:
    #go to next iteration if line does not start with From
    if not line.startswith('From ') : continue
    #assume line starts with From
    #populate email dict, assuming index 1 is emails
    line = line.strip()
    zeropos = line.find(':')
    result = line[zeropos - 2 : zeropos ]
    hours[result] = hours.get(result, 0) + 1

for key, value in sorted(hours.items()):
    print(key, value)
