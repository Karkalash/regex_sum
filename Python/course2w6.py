#10 tuples
#use () instead of [], are exactly like lists
x = ('Glen', 'Sally', 'Joseph')
print(x[2])
t = tuple()
dir(t)
#tuples are not mutable, are immutable just like strings
#can't sort, can't append, can't extend it
#when making temp variables tuples can be prefered over lists
#since python does not have to worry about changing them
#tuples can be added on the left hand side of the assignment
(a, b) = (99, 98) #one to one assignment
#sorting tuples
d = {'a' : 10, 'c' : 22, 'b' : 1 }
y = d.items()
print("YYŸ`", y)
print( d.items() )
t = sorted( d.items()) #gives you back a list of the sorted version
print(t)
#sorting by keys
for k, v in sorted(d.items()):
    print(k, v)
#sorting by values
tmp = list()
for k, v in sorted(d.items()):
    tmp.append( (v, k) ) #append a tuple into the list!
print(tmp)
tmp = sorted(tmp)
print(tmp)

#10 most common words putting it all together
fhand = open('romeo.txt')
counts = dict()
for line in fhand: #split the words add to dictionary
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
#reverse the keys
lst = list()
for key, val in counts.items():
    lst.append( (val, key) ) #append a tuple to the list with reverse roles

lst = sorted(lst, reverse = True) #sort by biggest to smallest number
for val, key in lst[:10]:
    print(key, val)
