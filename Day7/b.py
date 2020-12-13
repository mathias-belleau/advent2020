

def read_input(filename):
    f = open(filename, "r") 
    words = f.read().split('\n')
    f.close()
    return words

def process_rules(rules):
    for rule in rules:
        process_rule(rule)


def process_rule(rule):
    #need to split on contain. [0] == bag type
    #                          [1] == what it can hold
    rule = rule.split('contain')
    bagType = rule[0][:-6]

    #print(bagType)
    #print(rule[1])
    
    #need to split what it can hold
    #for each in holds trim bag+
    rule[1] = rule[1].replace(',', '')
    rule[1] = rule[1].replace('.', '')
    rule[1] = rule[1].replace('bags', 'bag')
    result = [x.strip() for x in rule[1].split('bag')]
    #print(result)

    #results in 
    # (#number) (word1 word2)
    # no other -> if empty
    # '' -> just ignore
    # print('new bagtype: ' + bagType)
    bags[bagType] = {}
    for bagHold in result:
        if(bagHold == '' or 'no other' in bagHold):
            continue
        bagHoldSplit = bagHold.split(' ', 1)
        bags[bagType][bagHoldSplit[1]] = int(bagHoldSplit[0])
        


def dive_into_bag(currentBag):
    print('\n')
    print(currentBag)
    global found_target
    total = 1
  
    # print('looking in: ')
    # print(currentBag)
    for bag in currentBag.keys():
        multiplier = max(currentBag[bag],1)
        dive = dive_into_bag(bags[bag])
        print('---')
        print(multiplier)
        print(dive)
        total += dive * multiplier
    return total



def main():
    global bags
    bags = {}
    global found_target
    found_target = 0


    rules = read_input('input')
    process_rules(rules)
    found_target += dive_into_bag(bags['shiny gold'])
    print('+++++')
    print(found_target)

if __name__ == "__main__":
    main()