name = input('Enter file name:')
if len(name) < 1 : name = 'mbox-short.txt'
handle = open(name)

#create data structures and populate with emails
emails = dict()
for line in handle:
    #go to next iteration if line does not start with From
    if not line.startswith('From: ') : continue
    #assume line starts with From
    #populate email dict, assuming index 1 is emails
    words = line.split()
    emails[words[1]] = emails.get(words[1], 0) + 1
#count the emails up
bigcount = None
bigemail = None
for key,value in emails.items():
    if bigcount is None or value > bigcount:
        bigemail = key
        bigcount = value
print(bigemail, bigcount)
