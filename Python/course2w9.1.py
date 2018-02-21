#9.1 Dictionaries
# purse = dict()
# purse['money'] = 12
# purse['candy'] = 3
# purse['tissues'] = 75
# print(purse)
#
# #can literally type out dictionary using curly braces
# jjj = { 'chuck' : 1, 'fred' : 42, 'jan' : 100}
# print(jjj)
# #can even make an empty one
# ooo = {}
# print(ooo)

# 9.2 - counting in dictionaries and creating conditional statements
# counts = dict()
# names = ['csev', 'cwen', 'zqian', 'cwen', 'csev']
# for name in names:
#     #if name not in counts:
#         # counts[name] = 1
#     #else:
#     #    counts[name] += 1
#     #alternative using get() method
#     counts[name] = counts.get(name, 0) + 1 #were 0 is default
#     #how does it work:
#     #get returns false: if name(key) not in count, add it default value is 0 then add 1 to it
#     #get returns true: then simply add 1 to that key, default value 0 is ignored in this case
# print(counts)
#9.3 - Putting it all together
# counts = dict()
# print('Enter a line of text:')
# line = input('')
# words = line.split()
# print('Words', words)
# print('Counting...')
# for word in words:
#     counts[word] = counts.get(word, 0) + 1
# print(counts.keys())
# print(counts.values())
# print(counts.items()) #tuples in each item list
# print('Counts', counts)

#last example:
name = input('Enter file name:')
handle = open(name)

#create dictionary and populate it with the words from the file
counts = dict()
for line in handle:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

#count the words up
bigcount = None
bigword = None
for key,value in counts.items():
    if bigcount is None or value > bigcount:
        bigword = key
        bigcount = value
print(bigword, bigcount)
