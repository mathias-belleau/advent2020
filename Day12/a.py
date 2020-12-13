class Ship:
    def __init__(self):
        self.direction = 'E'

        self.north = 0
        self.east = 0

        self.rotateRight = ['E','S','W','N']
        self.rotateLeft = ['E','N','W','S']

    def follow_cmds(self, cmds):
        for x in cmds:
            # print(x)
            self.follow_cmd(x)
            # print('direction: ' + self.direction + '  - east/north: ' + str(self.east) + '/' + str(self.north))


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
            direction = self.direction

        if direction == 'E':
            self.east += amount
        elif direction == 'W':
            self.east -= amount
        if direction == 'N':
            self.north += amount
        if direction == 'S':
            self.north -= amount
        return

    def rotate(self, direction, amount):
        # print('------------- rotation')

        rotations = int(amount / 90 )
        # print('rotations: ' + str(rotations))
        if direction == 'R':
            # print('right rotate')
            current = self.rotateRight.index(self.direction)
            # print('current: ' + str(current))
            self.direction = self.rotateRight[(current + rotations) % 4]
            # print(self.rotateRight[(current + rotations) % 4])
        elif direction == 'L':
            current = self.rotateLeft.index(self.direction)
            self.direction = self.rotateLeft[(current + rotations) % 4]
        #left or right
        #degrees = amount / 90


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
    #unparsed = read_input("test")
    unparsed = read_input("input")
    parsed = parse_instructions(unparsed)

    shipA = Ship()
    shipA.follow_cmds(parsed)
    #unparsed = read_input("input")

if __name__ == "__main__":
    main()