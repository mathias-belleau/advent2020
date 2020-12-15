# 939
# 7,13,x,x,59,x,31,19



# 1068781 vs 1068782 vs 1068785

def testing():
    x = 0
    while True:
        # if x > 1068791:
        #     print("failure")
        #     return

        # if x == 1068781:
        #     print('here')

        # if ((x - 4) % 7 == 0 and
        #     (x - 3) % 13 == 0 and
        #     (x + 0) % 59 == 0 and
        #     (x + 2) % 31 == 0 and
        #     (x + 3) % 19 == 0):
        #     print("found")
        #     print(x - 4)
        #     return
        # x+=59

        # if ((x - 3) % 1789 == 0 and
        #     (x - 2) % 37 == 0 and
        #     (x - 1) % 47 == 0 and
        #     (x + 0) % 1889 == 0):
        #     print("found")
        #     print(x - 3)
        #     return
        # x+=1889

# value: 17 = 0
# value: 37 = 11
# value: 439 = 17
# value: 29 = 19
# value: 13 = 30
# value: 23 = 40
# value: 787 = 48
# value: 41 = 58
# value: 19 = 67

        if ( (x- 48) % 17 == 0 and
           (x - 37) % 37 == 0 and
           (x - 31) % 439 == 0 and
           (x - 29) % 29 == 0 and
           (x - 18) % 13 == 0 and
           (x - 8) % 23 == 0 and
           (x + 0) % 787 == 0 and
           (x + 10) % 41 == 0 and
           (x + 19) % 19 == 0):
               print("found")
               print(x-48)
               return
        x+=787

def find_adds():
    #test = [17, 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 37, 'x', 'x', 'x', 'x', 'x', 439, 'x', 29, 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 13, 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 23, 'x', 'x', 'x', 'x', 'x', 'x', 'x', 787, 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 41, 'x', 'x', 'x', 'x', 'x', 'x', 'x', 'x', 19]
    #test = [7,13,'x','x',59,'x',31,19]
    test = [1789,37,47,1889]
    for x in range(len(test)):
        if test[x] != 'x':
            print('value: ' + str(test[x]) + ' = ' + str(x))


testing()
#find_adds()
        