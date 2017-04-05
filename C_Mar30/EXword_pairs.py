import sys

#pay attention to what is indented within the line reading of the file
#and then the only other for is to print
pairs = list() #a list of lists

for line in sys.stdin:#no parenthesis after stdin WHY?
    line = line.strip() #remove all white space
    words = line.split (" ") #separate each word from the line with white space

#If the file has less than 2 words (which are arranged in the previos list) then
#it will stop here...so make sure it is not the case otherwise erase this line
    if len(words) < 2:#this if needs to be in the fro otherwise continue is not taken
        continue

# iterate through the whole list of words un til the last one (-1)< this is
#very important as it guarantees you don't go beyond the length of the list
    for i in range(len(words) - 1):
        pair = words[i:i+2] #A pair is every element in the list (i) plus the next one
        #why + 2 and not +1
        pairs.append(pair) #pairs was an empty list so we are adding every new pair as
        #a new elemnt

for pair in pairs:
    print' '.join(pair) #turn the pair in the list into a string separated by " "
