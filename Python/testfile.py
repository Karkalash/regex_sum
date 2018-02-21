
# get name of file and open it
fileName = input('Enter file name:')
fileReader = open(fileName, 'r')

#count words and frequency of words
counts = dict()
for line in fileReader:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
        print(word + " ")

#find the most commont words
bigCount = None
bigWords = None
for word, count in counts.items():
    if bigCount is None or count > bigCount:
        bigWords = word
        bigCount = count

#print results
print( "Most Frequent Word: " + str(bigWords) + ", count: " + str(bigCount) )
