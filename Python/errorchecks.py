

numDict = [] #array to store number intakes
def getLargest(): #get largest number by looping through numDict
    largest_number = None
    for num in numDict:
        if largest_number is None: #check to see if there is no largest known yet, assign it to the first value
            largest_number = num
        elif num > largest_number:
            largest_number = num
    print("Maximum is", int(largest_number)) #print it out

def getSmallest(): #get smallest number by looping through numDict
    smallest_number = None
    for num in numDict:
        if smallest_number is None: #check to see if there is no smallest known yet, assign it the first value
            smallest_number = num
        elif num < smallest_number:
            smallest_number = num
    print("Minimum is", int(smallest_number) ) #print it out

def getInput():
    while True:
        sval = input("Enter a Number:") #prompt for inputs
        if sval == "done": #break out of loop
            break
        try :
            fval = float(sval) #error check for non numbers
            numDict.append(fval) #add to next index in numDict
        except:
            print("Invalid input")
            continue #move onto the next iteration
getInput()
getLargest()
getSmallest()
