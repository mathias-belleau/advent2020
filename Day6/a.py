def read_input(filename):
    f = open(filename, "r") 
    words = f.read().split('\n\n')
    f.close()
    return words

def make_groups(answers):
    group_answers = []
    for group in answers:
        group_answers.append(group.split('\n'))

    return group_answers


def count_yes(group_answers):
    total_yes = 0
    for group in group_answers:
        answer_set = set()
        for answers in group:
            for answer in answers:
                answer_set.add(answer)
        total_yes+= len(answer_set)
    print(total_yes)

def count_yes_matches(group_answers):
    total_yes = 0 
    for group in group_answers:
        answer_set = set()
        for answers in group:
            for answer in answers:
                answer_set.add(answer)

        #find which answer was not in ever group member's answers
        answer_check = answer_set.copy() 
        for x in answer_set:
            for answers in group:
                if x not in answers:
                    if x in answer_check:
                        answer_check.remove(x)
        
        total_yes += len(answer_check)
    print(total_yes)


    

def main():
    answers = read_input('input')
    group_answers = make_groups(answers)

    count_yes(group_answers)
    count_yes_matches(group_answers)
    #print(group_answers)

if __name__ == "__main__":
    main()