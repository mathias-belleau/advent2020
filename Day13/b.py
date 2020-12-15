class Bus:
    def __init__(self, depart):
        self.depart = depart
        self.timetable = []

    def generate_timetable(self, times):
        for x in range(times):
            if x % self.depart == 0:
                self.timetable.append(x)

def parse_bus_timetable(unparsed):
    bus_ids = unparsed[1].split(',')

    for x in range( len(bus_ids) ):
        if bus_ids[x] != 'x':
            bus_ids[x] = int(bus_ids[x])

    print(bus_ids)

    current_time = 0

    biggest = 17
    biggest_index = bus_ids.index(biggest)
    
    biggest -= biggest_index
    print(biggest)

    found = False
    while not found:

        # if current_time % 100000 == 0:
        #     print(current_time)
        # elif current_time > 1078781:
        #     print(current_time)
        #     print('fail')
        #     return
        # elif current_time == 1068782:
        #     print(bus_ids)

        found = True
        for x in range( len(bus_ids) ):
            

            if bus_ids[x] == 'x':
                continue
            # else:
            #     if current_time == 1068781:
            #         print((current_time + x) % bus_ids[x] == 0)
            #         print((current_time + x) )
            #         print(bus_ids[x])
            #         print("---------")
                    
                    
            if (current_time + x) % bus_ids[x] != 0:
                found = False
                break

        if found:
            print('found')
        else:
            current_time+=17
    print(current_time)
            
    

    


def read_input(filename):
    f = open(filename, "r") 
    words = f.read().split('\n')
    f.close()
    return words


def main():
    #unparsed = read_input("test")
    unparsed = read_input("input")
    #unparsed = read_input("test2")

    parse_bus_timetable(unparsed)
    

if __name__ == "__main__":
    main()