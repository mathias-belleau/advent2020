class Bus:
    def __init__(self, bus_id):
        self.bus_id = bus_id

    def get_earliest_bus(self, depart):
        self.timestamp = 0
        while self.timestamp < depart:
            self.timestamp += self.bus_id
        
        self.time_diff = self.timestamp - depart
        return self.time_diff

def find_earliest_bus(depart, buses):
    earliest = None
    for bus in buses:
        waiting_time = bus.get_earliest_bus(depart)

        if earliest is None or waiting_time < earliest.time_diff:
            earliest = bus

    print(earliest.bus_id)
    print(earliest.time_diff)
    print(earliest.bus_id * earliest.time_diff)

def parse_bus_timetable(unparsed):
    depart = int(unparsed[0])
    print("depart time: " + str(depart))

    buses = []
    busList = unparsed[1].split(',')
    for bus in busList:
        if bus != 'x':
            newBus = Bus(int(bus))
            buses.append(newBus)
    
    find_earliest_bus(depart, buses)

def read_input(filename):
    f = open(filename, "r") 
    words = f.read().split('\n')
    f.close()
    return words


def main():
    #unparsed = read_input("test")
    unparsed = read_input("input")

    parse_bus_timetable(unparsed)
    

if __name__ == "__main__":
    main()