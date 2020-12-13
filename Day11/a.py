from copy import deepcopy

class Waiting_Area:
    def __init__(self, tables):
        #self.tables = tables
        self.setup_tables(tables)
        self.x = len( self.tables)
        self.y = len(self.tables[0])

        self.changed = True

        while(self.changed):
            self.do_step()

        self.count_occupied()

    
    def count_occupied(self):
        occu = 0
        for x in range( len(self.tables)):
            for y in range( len(self.tables[x])):
                if self.tables[x][y] == '#':
                    occu+=1
        print(occu)

    def setup_tables(self, tables):
        self.tables = []
        for row in tables:
            newRow = []
            for space in row:
                newRow.append(space) 
            self.tables.append(newRow)


    def do_step(self):
        self.changed = False
        cloneTable = deepcopy(self.tables)
        for x in range(self.x):
            for y in range(self.y):            
                if(self.tables[x][y] != '.'):
                    neighs = self.get_neighbours([x,y])

                    if(neighs == 0 and self.tables[x][y] == 'L'):
                        cloneTable[x][y] = '#'
                        self.changed = True
                    elif(neighs >= 4 and self.tables[x][y] == '#'):
                        cloneTable[x][y] = 'L'
                        self.changed = True

        self.tables = cloneTable
        

    def get_neighbours(self, coords):
        coordX = coords[0]
        coordY = coords[1]
        # print(str(coordX) +','+str(coordY))
        #need to get ortho and diag neihgbours and check if they are occupied
        occupied = 0
        for x in range(-1, 2):
            for y in range(-1, 2):
                # print('checking: ' + str(x+coordX) + ',' + str(coordY+y))
                
                if(y == 0 and x == 0):
                    continue
                elif(coordX + x < 0 or coordX + x >= self.x):
                    continue
                elif(coordY + y < 0 or coordY + y >= self.y):
                    continue
                else:
                    # print('found: ' +self.tables[x+coordX][coordY+y])
                    #check if occopied seat
                    if(self.tables[x+coordX][coordY+y] == '#'):
                        occupied +=1
        return occupied

def print_grind(grid):
    for x in grid:
        print(x)
    print('\n++++++++++++++++++++++++++++++++++++')
    

def read_input(filename):
    f = open(filename, "r") 
    words = f.read().split('\n')
    f.close()
    return words


def main():
    #unparsed = read_input("test")
    unparsed = read_input("input")
    waitA = Waiting_Area(unparsed)

if __name__ == "__main__":
    main()