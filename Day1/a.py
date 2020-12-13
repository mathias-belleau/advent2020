def read_input(filename):
    f = open(filename, "r")
    words = f.read().splitlines()
    f.close()
    return words

def change_to_int(parsed):
    for x in range(0, len(parsed)):
        parsed[x] = int(parsed[x])
    return parsed

def find_to_sum(parsed, targetNum):
    for x in range(0, len(parsed)):
        for y in range(0, len(parsed)):
            if(x == y):
                continue
            #print("x: {x} + y: {y} == {result}".format(x=parsed[x],y=parsed[y],result=parsed[x]+parsed[y]))
            #check if the two values sum to 2020
            if (parsed[x] + parsed[y] == 2020):
                return [parsed[x], parsed[y]]

def multiply_results(a,b):
    return a*b

def find_to_sum_3(parsed, targetNum):
     for x in range(0, len(parsed)):
        for y in range(0, len(parsed)):
            for z in range(0, len(parsed)):
                if(x == y or x == z or y == z):
                    continue
                if (parsed[x] + parsed[y] + parsed[z] == 2020):
                    return [parsed[x], parsed[y], parsed[z]]

def task_a(parsed):
    #find two values that sum to 2020
    values = find_to_sum(parsed, 2020)
    print(values)
    
    #multiply those values
    print(multiply_results(values[0],values[1]))

def task_b(parsed):
    values = find_to_sum_3(parsed, 2020)
    print(values)

    print(values[0] * values[1]*values[2])

def main():
    parsed = read_input("input.txt")
    parsed = change_to_int(parsed)
    #task_a(parsed)
    task_b(parsed)

if __name__ == "__main__":
    main()