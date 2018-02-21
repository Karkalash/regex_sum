fruit = 'banana'
index = 0
while index < len(fruit):
    letter = fruit[index]
    print(index, letter)
    index += 1

for letter2 in fruit:
    print(letter2)

print('Hi There'.lower())

data = 'From stephen.marquard@utc.ac.za Sat Jan 5 09:14:16 2008'
atpos = data.find('@')
print(atpos)

sppos = data.find(' ', atpos)
print(sppos)

host = data[atpos+1 : sppos]
print(host)

# assignment: filter string and print out just the number as a float
text = "X-DSPAM-Confidence:    0.8475"
zeropos = text.find(' ')
result = text[zeropos :]
print( float( result.lstrip() ) )
