# 22nd Dec 2021
# Advent of code day 1 

#read data from file:
def runBaby():
    file = open("input1", "r")
    lines = file.read().splitlines()
    #print(len(lines))
    #print(lines[1999])
    prevLine = lines[0]
    count = 0

    for depth in lines[1:]:
        if depth > prevLine:
            count += 1
        prevLine = depth
    return count 

count = runBaby()
print(count)

 
