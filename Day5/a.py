def read_input(filename):
    f = open(filename, "r")
    words = f.read().split('\n')
    f.close()
    return words

max_seat = 128
max_col = 8

# 128
# B

def find_row(current_block, side):
    if(side == 'F'):
        current_block= [ current_block[0], (current_block[0] + current_block[1]) /2 ]
    else:
        current_block= [ (current_block[0] + current_block[1]) /2, current_block[1] ]

    return current_block

def find_column(current_block, side):
    if(side == 'R'):
        current_block= [ (current_block[0] + current_block[1]) /2, current_block[1] ]
    else:
        current_block= [ current_block[0], (current_block[0] + current_block[1]) /2 ]
    return current_block

def find_seat(boardingPass):
    current_block = [0,max_seat]

    for x in range(6):
        current_block = find_row(current_block, boardingPass[x])
        #print(current_block)

    row = 1
    #print(boardingPass[6])
    if(boardingPass[6] == 'F'):
        row = current_block[0]
    else:
        row = current_block[1] - 1
    #print(row)

    current_block = [0,8]
    for x in range(7,9):
        current_block = find_column(current_block, boardingPass[x])    
        #print(current_block)

    col = 999
    if(boardingPass[9] == 'R'):
        col = current_block[1] -1
    else:
        col = current_block[0]
    

    #print(col)
    return [row,col,row*8+col]
    
def get_boarding_passes(unparsed):
    boardingPasses = []
    for x in unparsed:
        boardingPasses.append( find_seat(x) )
    #print(boardingPasses)

    highest = -9999
    for x in boardingPasses:
        if x[2] > highest:
            highest = x[2]

    print(highest)
    boardingPasses.sort(key=sortID)

    seat_ids = []
    for x in boardingPasses:
        seat_ids.append(x[2])

    for y in range(77,955):
        if y not in seat_ids:
            print(y)

    #for x in range(0,len(boardingPasses)):
        #print('------------------------')
        #print(boardingPasses[x][2]+1)
        #print(boardingPasses[x+1][2])
        #if(boardingPasses[x][2]+1 != boardingPasses[x+1][2]):
         #   print(boardingPasses[x+1])



def sortID(seat):
    return seat[2]    

def main():
    unparsed = read_input('input')
    #print(unparsed)

    get_boarding_passes(unparsed)
    #find_seat(unparsed[0])

if __name__ == "__main__":
    main()