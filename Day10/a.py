from tqdm import tqdm

class jolts:
    def __init__(self, joltList):
        self.joltArray = self.parseJolts(joltList)
        #print(self.joltArray)

        self.currentJolt = 0
    
    def parseJolts(self, joltList):
        joltArray = []
        for j in joltList:
            joltArray.append(int(j))
        
        joltArray.sort()
        joltArray.append(joltArray[ len(joltArray) - 1] + 3)

        return joltArray

    def find_differences(self):
        differences = [0,0,0,0]
        adapter_found = True
        while adapter_found:
            adapter_found = False
            for x in range(1,4):
                if x + self.currentJolt in self.joltArray:
                    adapter_found = True
                    self.currentJolt = x + self.currentJolt
                    differences[x] +=1
                    break
        print(differences)
        print(differences[1] * differences[3])
        
    def find_connections(self):
        self.joltArray.insert(0,0)
        
        self.node_paths = {}
        for x in range(len(self.joltArray)):
            #amount +=  self.find_connection(x) ** x + 1
            test = self.find_connection(x)
            if len(test) != 0:
                self.node_paths[self.joltArray[x]] = test

       

        self.find_paths()

    def find_connection(self, i):
        connections_found = []
        for x in range(1,4):
                if x + self.joltArray[i] in self.joltArray:
                    #print(x+self.joltArray[i])

                    connections_found.append(x+self.joltArray[i])
                    #connections_found.append(x+i)
        return connections_found

    def find_paths(self):
        #for loop over each path recursively?
        total = 0

        # self.node_paths[5] = []
        # self.node_paths[6] = []
        # self.node_paths[7] = []


        #rint(self.joltArray)
    # print(self.node_paths)
        # for node in self.node_paths.keys():
        #     print(str(node) + ':' + str(self.node_paths[node]))

        total = self.find_path(0)
        print(total + 1)

            
    def find_path(self,node):
        if node % 100000 == 0:
            print(node)
        if node not in self.node_paths:
            return 0

        total = len(self.node_paths[node]) - 1

        for x in self.node_paths[node]:
            total += self.find_path(x)
        
        return total

def read_input(filename):
    f = open(filename, "r") 
    words = f.read().split('\n')
    f.close()
    return words


def main():
    #unparsed = read_input('smallTest')
    #unparsed = read_input('test.txt')
    unparsed = read_input('input')
    joltA = jolts(unparsed)
    joltA.find_differences()
    joltA.find_connections()

if __name__ == "__main__":
    main()