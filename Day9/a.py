class XMAS:
    def __init__(self, preamble, input):
        self.preamble = preamble
        self.cypher = []

        self.makeCypher(input)
    
    def makeCypher(self, input):   
        for x in input:
            self.cypher.append(int(x))

    def find_bad_number(self):
        # iterate through list starting just past preamble amount and find a number that can't be made from previous preamble numbers
        for x in range(self.preamble, len(self.cypher)):
            current = self.cypher[x]
            currentPre = self.cypher[x-self.preamble:x]
            found_match = False

            for y in range(len(currentPre)):
                if(current - currentPre[y] in currentPre):
                    found_match = True
            if not found_match:
                return self.cypher[x]

    def find_contin(self, a):
        for x in range(len(self.cypher)):
            newCheck = []
            for y in range(x, len(self.cypher)):
                newCheck.append(self.cypher[y])
                if sum(newCheck) == a:
                    return newCheck
                elif sum(newCheck) > a:
                    break
    
    def find_cypher(self,b):
        b.sort()
        print(b[0] + b[len(b)-1])

def read_input(filename):
    f = open(filename, "r") 
    words = f.read().split('\n')
    f.close()
    return words


def main():
    partA = XMAS(25, read_input('input'))
    #partA = XMAS(5, read_input('test'))

    #print(partA.cypher)
    a = partA.find_bad_number()

    b = partA.find_contin(a)
    print(b)
    partA.find_cypher(b)

if __name__ == "__main__":
    main()