
def read_input(filename):
    f = open(filename, "r") 
    words = f.read().split('\n')
    f.close()
    return words

def run_machine(input):
    acclumator = 0
    run_instructions = set()

    x = 0
    while x < len(input):
        
        #rint(input[x])
        instruct = input[x].split(' ')
        instruct[1] = int(instruct[1])

        if(instruct[0] == "acc"):
            acclumator += instruct[1]
        elif (instruct[0] == "jmp"):
            x += instruct[1]-1
        #elif (instruct[0] == "nop")

        
        if x in run_instructions:
            return acclumator
        run_instructions.add(x)
        x+=1

def fix_machine(input):    
    #for loop over EACH code
    #if jmp or nop swap it
    #   run_machine and check for x == len(input)

    for y in range(7, len(input)-1):
        #check if swp and make copy of input
        copyInput = input.copy()
        if 'nop' in copyInput[y]:
            copyInput[y] = copyInput[y].replace('nop', 'jmp')
        elif 'jmp' in copyInput[y]:
            copyInput[y] = copyInput[y].replace('jmp', 'nop')

        acclumator = 0
        run_instructions = set()

        x = 0
        # print(copyInput)
        # print(len(copyInput))
        while x < len(copyInput):
            #print(copyInput[x])
            if(x > len(copyInput)-1):
                x = 999999999999
            elif(x == len(copyInput)-1):
                print(acclumator)
            #rint(input[x])
            instruct = copyInput[x].split(' ')
            instruct[1] = int(instruct[1])

            if(instruct[0] == "acc"):
                acclumator += instruct[1]
            elif (instruct[0] == "jmp"):
                x += instruct[1]-1
            #elif (instruct[0] == "nop")

            if(x == len(copyInput)-1):
                print(acclumator)

            if x in run_instructions:
                x = 999999999999
                continue
            run_instructions.add(x)
            x+=1

def main():
    input = read_input('input')
    result = run_machine(input)
    print(result)

    result2 = fix_machine(input)
    print(result2)
if __name__ == "__main__":
    main()
