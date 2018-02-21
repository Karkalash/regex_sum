#assignment 1 romeo.txt
fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
    words = line.split() #split lines into a new list words
    for i in range(len(words)): #cycle through words list using a controllable index
        if words[i] in lst: continue #move to next iteration if item already in list
        lst.append(words[i]) #append if not
lst.sort() #sort the list
print(lst) #print it

#assigment 2
#parsing mail data
fhand = open('mbox-short.txt')
count = 0
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From ') : continue #if the line does not start with "From"
    words = line.split()
    email = words[1]
    count += 1
    print(email)
print("There were", count, "lines in the file with From as the first word")
