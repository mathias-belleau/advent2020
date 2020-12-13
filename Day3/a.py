class Sledder:
    def __init__(self, slopeX, slopeY, startX, startY):
        self.slopeX = slopeX
        self.slopeY = slopeY
        self.currX = startX
        self.currY = startY
        self.targetX = self.currX
        self.targetY = self.currY

slopes = [ [1,1], [3,1], [5,1], [7,1], [1,2] ] 

def read_input(filename):
    f = open(filename, "r")
    words = f.read().splitlines()
    f.close()
    return words

def buildBaseMap(parsed):
    #parsed[0][0] = 'y'
    baseMap = parsed[:]
    #baseMap[0] += baseMap[0]
    return baseMap

def expandMap(baseMap, bluePrint, sledder):
    if(sledder.targetY >= len(baseMap)):
        return

    while (sledder.targetX >= len(baseMap[sledder.targetY])) :
        baseMap[sledder.targetY] += bluePrint[sledder.targetY]
    #return baseMap

def findRoute(baseMap, bluePrint, slope):
    sledder = Sledder(slope[0],slope[1],0,0)
    trees = 0
    while sledder.currY <= len(baseMap):
        #set target
        sledder.targetX = sledder.currX + sledder.slopeX
        sledder.targetY = sledder.currY + sledder.slopeY

        if(sledder.targetY >= len(baseMap)):
            return trees
            
        else:
            expandMap(baseMap, bluePrint, sledder)
            #set our current pos
            sledder.currX = sledder.targetX
            sledder.currY = sledder.targetY

            #check if we hit a tree
            if(baseMap[sledder.currY][sledder.currX] == '#'):
                trees+=1
        #print(baseMap[1])
        
def findRoutes(baseMap, bluePrint):
    treesHit = []
    for slope in slopes:
        treesHit.append(findRoute(baseMap, bluePrint, slope))
    
    total = 1
    for x in treesHit:
        total *= x
        
    print(treesHit)
    print(total)

def main():
    #need to create a blueprint for the ever expanding map
    #create first map.
    #check if new position would be out of a rows index. expand it, try again
    #while(len(map[x]) < targetPos.y)) { expand map[x]}
    #currentPos == tree? +=1
    bluePrint = read_input('test')

    baseMap = buildBaseMap(bluePrint)
    #print(bluePrint)

    #print(baseMap)
    #print(len(baseMap))
    findRoute(baseMap,bluePrint, slopes[1])
    
    findRoutes(baseMap,bluePrint)
    

if __name__ == "__main__":
    main()