
#count lines in file
fhand = open('words.txt', 'r')
for words in fhand:
    words = words.rstrip()
    print(words.upper())
fhand.close()

#assing file to a string is easy
fhand2 = open('mbox-short.txt', 'r')
inp = fhand2.read() #placement order matters
print(len(inp))
print(inp[:20])
fhand2.close()

#search for particular criteria in file
fhand3 = open('mbox-short.txt', 'r')
for line in fhand3:
    line = line.rstrip() #prevent inessecary newlines
    #if line.startswith('From:'):
    #    print(line)
    #alternative reverse logic might make it go faster
    if not line.startswith('From:'):
        continue
    # print(line)
fhand3.close()

#finding criteria within lines
fhand4 = open('mbox-short.txt', 'r')
for line2 in fhand4:
    line2 = line2.rstrip()
    if not '@uct.ac.za' in line2:
        continue
    print(line2)

#teaching python to ask for filenames and adding catch logic
fname = input('Enter the file name: ')
try:
    fhand5 = open(fname)
except:
    print('File cannot be opened: ', fname)
    quit()
count = 0
for line3 in fhand5:
    if line3.startswith('Subject:'):
        count += 1
print('There were', count, 'subject lines in', fname)
