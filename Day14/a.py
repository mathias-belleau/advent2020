class Memory():
    def __init__(self, mask, inputs):
        self.mask = mask
        self.inputs = inputs
        self.addresses = {}

    def apply_mask(self):
        for inp in self.inputs:
            l = list(inp[1])

            for x in range(len(self.mask)):
                if self.mask[x] == 'X':
                    continue
                else:
                    l[x] = self.mask[x]
            inp[1] = ''.join(l)


    def write_memory(self):
        for inp in self.inputs:
            self.addresses[inp[0]] = int(inp[1], 2)

    def get_memory_sum(self):
        total = 0
        print('---------')
        for key in self.addresses.keys():
            print(self.addresses[key])
            total += self.addresses[key]
        print(total)
        return total

def pad_binary(bin_2_pad):
    return bin_2_pad.rjust(36, '0')

def make_memories(unparsed):
    masks = 0
    memories = []

    mask = ''
    inputs = []
    for x in unparsed:
        if 'mask' in x:
            masks+=1
            #if mask is not null we need to create our current memory before wiping it
            if mask != '':
                memory = Memory(mask, inputs)
                memories.append(memory)

            #new mask
            mask = x.split('=')
            mask = mask[1].strip()
            # print("mask: " + mask)
            inputs = []
        else:
            bleh2 = x.split('=')
            mem = bleh2[0]
            mem = mem.replace('mem[', '')
            mem = mem.replace(']', '')

            
            target = bleh2[1].strip()
            # print('mem: ' + mem)
            # print('target: ' + target)
            
            formatted = format(int(target) ,"b")
            padded = pad_binary( str(formatted) )
            # print('target Bin: ' + padded)
            inputs.append( [mem, padded])
    
    #last one needs to be made as well
    memory = Memory(mask, inputs)
    memories.append(memory)

    return memories
        
def apply_masks(memories):
    for memory in memories:
        memory.apply_mask()

def get_sum(memories):
    total = 0
    for x in memories:
        x.write_memory()
        total += x.get_memory_sum()

    print('----')
    print(total)

def read_input(filename):
    f = open(filename, "r") 
    words = f.read().split('\n')
    f.close()
    return words


def main():
    unparsed = read_input("test")
    #unparsed = read_input("test2.txt")
    #unparsed = read_input("input")
    memories = make_memories(unparsed)
    apply_masks(memories)

    get_sum(memories)
   

if __name__ == "__main__":
    main()