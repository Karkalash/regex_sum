# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count = 0
tAdd = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") :
        continue
    line = line.strip()
    zeropos = line.find(':')
    result = line[zeropos + 1 :]
    tAdd = tAdd + float(result.strip())
    count += 1
print("Average spam confidence:", tAdd / count) #they have a round off mechanism in autograder but answer is correct
