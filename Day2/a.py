from collections import Counter


def read_input(filename):
    f = open(filename, "r")
    words = f.read().splitlines()
    f.close()
    return words

def parse_input(input):
    parsed = []
    for x in input:
        newRow = {}
        
        firstSplit = x.split(':')
        newRow['pass'] = firstSplit[1].strip()

        secondSplit = firstSplit[0].split(' ')
        newRow['qualifier'] = secondSplit[1]

        thirdSplit = secondSplit[0].split('-')
        newRow['range'] = [ int(thirdSplit[0]), int(thirdSplit[1]) ]
        parsed.append(newRow)
    return parsed

def find_valid(parsed):
    valid = 0
    for x in parsed:
        if(check_valid(x)):
            valid += 1
    print(valid)


def check_valid(row):
    #pass
    #qualifer
    #range
    c = Counter(row["pass"])
    
    #print(row)
    #print("qual: {qual}, qualCount: {qualCount} range: {range1}-{range2}".format(qualCount=c[row["qualifier"]],qual=row["qualifier"],range1=row["range"][0],range2=row["range"][1]))
    return( c[row["qualifier"]] >= row["range"][0] and c[row["qualifier"]] <= row["range"][1])

def find_valid_b(parsed):
    valid = 0
    for x in parsed:
        if(check_valid_b(x)):
            valid +=1
    print("b: {}".format(valid))

def check_valid_b(row):
    #pass
    #qualifer
    #range
    #c = Counter(row["pass"])
    #print("qual: {qual}, password: {password} range: {range1}-{range2}".format(password=row['pass'],qual=row["qualifier"],range1=row["range"][0],range2=row["range"][1]))
    #need to check if values at pass[range[0]] or pass[range[1]] == qualifier and make sure within length of pass
    return( (len(row['pass']) >= row['range'][0] and row['pass'][row['range'][0]-1] == row['qualifier']) is not
        (len(row['pass']) >= row['range'][1] and row['pass'][row['range'][1]-1] == row['qualifier']) )

    #print( (len(row['pass']) >= row['range'][0] and row['pass'][row['range'][0]-1] == row['qualifier']))
    #print( (len(row['pass']) >= row['range'][1] and row['pass'][row['range'][1]-1] == row['qualifier']) )
    

def main():
    parsed = read_input("input")
    parsed = parse_input(parsed)

    ##-## A: abcdef
    find_valid(parsed)
    find_valid_b(parsed)




if __name__ == "__main__":
    main()