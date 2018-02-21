#tale of two loops 8.1

friends = ['joseph', 'glenn', 'sally']
for friend in friends:
    print('Happy new year:', friend)
#if you want to know exactly were the index is
for i in range(len(friends)):
    friend = friends[i]
    print('Happy new Year:', friend)
#8.2 - using list to calculate average as opposed to manually doing it
numlist = list()
while True:
    inp = input("Enter a number: ")
    if inp == "done" : break
    value = float(inp)
    numlist.append(value)

average = sum(numlist) / len(numlist)
print("Average:", average)
#8.3 spliting strings
abc = 'with three words'
stuff = abc.split() #splits string and returns a list
print(stuff)

#parsing mail data
fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From ') : continue
    words = line.split()
    email = words[1]
    print(pieces[1])

t = [9, 41, 12, 3, 74, 15]
print(t[2:4])
