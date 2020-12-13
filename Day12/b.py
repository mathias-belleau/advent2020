class Ship:
    def __init__(self):

        self.north = 0
        self.east = 0

        self.wpDirection = 'E'

        self.waypointNorth = 1
        self.waypointEast = 10

        self.rotateRight = ['E','S','W','N']
        self.rotateLeft = ['E','N','W','S']

    def follow_cmds(self, cmds):
        for x in cmds:
            # print(x)
            self.follow_cmd(x)
            # print('east/north: ' + str(self.east) + '/' + str(self.north))
            # print('direction: ' + self.wpDirection +  ' -- ' + str(self.waypointEast) + '/' + str(self.waypointNorth))
            # print('\n')


        print(self.east)
        print(self.north)
        print( abs(self.north) + abs(self.east))

    def follow_cmd(self, cmd):
        order = cmd[0]
        amount = cmd[1]

        if order == 'R' or order == 'L':
            #rotate
            self.rotate(order,amount)
        else:
            #move this direction
            self.move(order, amount)
        
    def move(self, direction, amount):
        if direction == 'F':
            for x in range(amount):
                self.east += self.waypointEast
                self.north += self.waypointNorth

        elif direction == 'E':
            self.waypointEast += amount
        elif direction == 'W':
            self.waypointEast -= amount
        if direction == 'N':
            self.waypointNorth += amount
        if direction == 'S':
            self.waypointNorth -= amount

    def rotate(self, direction, amount):
        rotations = int(amount / 90 )
        # print('rotations: ' + str(rotations))
        if direction == 'R':
            # current = self.rotateRight.index(self.wpDirection)
            for x in range(rotations):
                self.shift_direction_right()
        elif direction == 'L':
            # current = self.rotateLeft.index(self.wpDirection)
            for x in range(rotations):
                self.shift_direction_left()
    
    def shift_direction_right(self):
        # east 10,4 
        # south 4,-10 -> swap / * -1
        # west -10, -4 -> swap /, *-1
        # north -4, 10 -> swap, /,abs()
        # east -> swap, /, abs()

        
        # print('------------- rotation')
        if self.wpDirection == 'E':
            # print('direction: ' + self.wpDirection +  ' -- ' + str(self.waypointEast) + '/' + str(self.waypointNorth))
            swap = [self.waypointNorth, self.waypointEast * - 1]
            # 
            self.wpDirection = 'S'        
        elif self.wpDirection == 'S':
            swap = [self.waypointNorth, self.waypointEast * -1]
            self.wpDirection = 'W'
        elif self.wpDirection == 'W':
            swap = [self.waypointNorth, abs(self.waypointEast)]
            self.wpDirection = 'N'
        elif self.wpDirection == 'N':
            swap = [abs(self.waypointNorth), abs(self.waypointEast)]
            self.wpDirection = 'E'
        else:
            print("PRINT ERROR :" + self.wpDirection)
        
        self.waypointEast = swap[0]
        self.waypointNorth = swap[1]

    def shift_direction_left(self):
        # east 10,4
        # north -4,10 -> swap, *-1, /
        # west -10,-4 -> swap, *-1 /
        # south 4,10 -> swap, abs/abs
        # east -> swap

        # print('\ndirection: ' + self.wpDirection +  ' -- ' + str(self.waypointEast) + '/' + str(self.waypointNorth))
        if self.wpDirection == 'E':
            # print("rotating North")
            swap = [self.waypointNorth * -1, self.waypointEast]
            self.wpDirection = 'N'        
        elif self.wpDirection == 'N':
            # print("rotating West")
            swap = [self.waypointNorth * -1, self.waypointEast]
            self.wpDirection = 'W'
        elif self.wpDirection == 'W':
            # print("rotating south")
            swap = [abs(self.waypointNorth), abs(self.waypointEast)]
            self.wpDirection = 'S'
        elif self.wpDirection == 'S':
            # print("rotating east")
            swap = [self.waypointNorth, self.waypointEast]
            self.wpDirection = 'E'
        
        # print(swap)
        self.waypointEast = swap[0]
        self.waypointNorth = swap[1]


def parse_instructions(instructs):
    instructions = []
    for x in instructs:
        instructions.append([x[0], int(x[1:])])
    # print(instructions)
    return instructions


def read_input(filename):
    f = open(filename, "r") 
    words = f.read().split('\n')
    f.close()
    return words


def main():
    unparsed = read_input("test")
    #unparsed = read_input("input")
    parsed = parse_instructions(unparsed)

    shipA = Ship()
    shipA.follow_cmds(parsed)
    #unparsed = read_input("input")

if __name__ == "__main__":
    main()