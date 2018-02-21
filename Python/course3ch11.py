#regular expression:  a form of a language, way to say a set of strings match or not match
#more intelligent form of search
#not naturaly to python, must import using below
import re

#extracting digits
x = 'My 2 favorite numbers are 19 and 42'
#[0-9] the type of data to extract which is digits from 0-9
#+ one or more
y = re.findall('[0-9]+', x)
#returns a string list
print(y)
#same concept but trying to find uppercase vowels (which there are none so returns empty list)
y = re.findall('[AEIOU]+', x)
print(y)
#greedy matching always returns the largest thing, example:
x = 'From: Using the : character'
#find characters that match F, then match any character up to :
y = re.findall('^F.+:', x)
#two matches are 'From:' and 'From: Using the :', greedy match will return the biggest one which is not always good
print(y)
#can be fixed by simply doing non-greedy with ?
y = re.findall('^F.+?:', x)
print(y)

#email example:
text = 'From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
#simply saying find any non blank characters followed by an @ sign and non blank character again
email = re.findall('\S+@\S+', text)
#in this case greedyness is good, otherwise you get the shortest one being d@d
print(email)
#parentheses can be used to say when to start and stop extracting
email = re.findall('^From (\S+?@\S+)', text)
print(email)
#if i want to extract the host only
#[^ ] = match any non blank character, example @uct... the u is non blank character
#* match any of them from there on
email2 = re.findall('@([^ ]*)', text)
#in other words, extract a single non blank character zero or more times (stops once blank character is reached)
print(email2)
#fine tunning even more
email2 = re.findall('^From .*@([^ ]*)', text)
print(email2)
#putting it together to repeat the max confidence exercise
hand = open('mbox-short.txt')
numlist = list()
for line in hand:
    line = line.rstrip()
    stuff = re.findall('^X-DSPAM-Confidence: ([0-9.]+)', line) #match any character in a 0-9 range and extract it
    if len(stuff) != 1 : continue #if the list comesback empty, move to next iteration
    num = float(stuff[0])
    numlist.append(num)
print('Max: ', max(numlist))
