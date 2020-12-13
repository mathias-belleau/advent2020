import re 


class Passport:
    def __init__(self, unparsed):
        self.fields = unparsed

    def fetch_field(self, field):
        if(field in self.fields.keys()):
            return self.fields[field]
        else:
            return None

def read_input(filename):
    f = open(filename, "r")
    words = f.read().split('\n\n')
    f.close()
    return words

def parse_passports(data):
    #print(passportList)
    passport_list = []
    #print(data)
    for x in data:
        passport_list.append(parse_passport(x))
    
    return passport_list

def parse_passport(unparsed_passport):
    # byr (Birth Year)
    # iyr (Issue Year)
    # eyr (Expiration Year)
    # hgt (Height)
    # hcl (Hair Color)
    # ecl (Eye Color)
    # pid (Passport ID)
    # cid (Country ID)
    #ecl:gry pid:860033327 eyr:2020 hcl:#fffffd
    #byr:1937 iyr:2017 cid:147 hgt:183cm

    #strip \n    
    unparsed_passport = unparsed_passport.replace('\n', ' ')
    unparsed_passport = unparsed_passport.strip()
    #split by spaces
    split_pass = unparsed_passport.split(" ")

    #build object
    split_pass_fields = {}
    for x in split_pass:
        split_fields = x.split(":")

        if( len(split_fields) < 2):
            print("ERROR")
            print(x)

        split_pass_fields[split_fields[0]] = split_fields[1]

    return Passport(split_pass_fields)


def check_valid(passport_list):
    valid = 0 
    for x in passport_list:
        valid += check_if_valid(x)
    return valid

def check_if_valid(passport):
    if (passport.fetch_field('byr') and
        passport.fetch_field('iyr') and
        passport.fetch_field('eyr') and
        passport.fetch_field('hgt') and
        passport.fetch_field('hcl') and
        passport.fetch_field('ecl') and
        passport.fetch_field('pid')):
        return 1
    else:
        return 0

def check_valid_b(passport_list):
    valid = 0

    for x in passport_list:
        valid += check_if_valid_b(x)
    return valid

def check_if_valid_b(passport):
    
    # byr (Birth Year) - four digits; at least 1920 and at most 2002.
    # iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    # eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    # hgt (Height) - a number followed by either cm or in:
    #     If cm, the number must be at least 150 and at most 193.
    #     If in, the number must be at least 59 and at most 76.
    # hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    # ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    # pid (Passport ID) - a nine-digit number, including leading zeroes.
    # cid (Country ID) - ignored, missing or not.
    if ( (passport.fetch_field('byr') and check_byr(passport.fetch_field('byr')) ) and
         (passport.fetch_field('iyr') and check_iyr(passport.fetch_field('iyr')) ) and
         (passport.fetch_field('eyr') and check_eyr(passport.fetch_field('eyr')) ) and
         (passport.fetch_field('hgt') and check_hgt(passport.fetch_field('hgt')) ) and
         (passport.fetch_field('hcl') and check_hcl(passport.fetch_field('hcl')) ) and
         (passport.fetch_field('ecl') and check_ecl(passport.fetch_field('ecl')) ) and
         (passport.fetch_field('pid') and check_pid(passport.fetch_field('pid')) ) ):
        return 1
    else:
        return 0

def check_byr(byr):
    return (int(byr) <= 2002 and int(byr) >= 1920)

def check_iyr(iyr):
    return (int(iyr) <= 2020 and int(iyr) >= 2010)

def check_eyr(eyr):
    return (int(eyr) <= 2030 and int(eyr) >= 2020)

def check_hgt(hgt):
    if(hgt.endswith('cm')):
        hgt = hgt[:-2]
        return (int(hgt) >= 150 and int(hgt) <= 193)
    elif (hgt.endswith('in')):
        hgt = hgt[:-2]
        return (int(hgt) >= 59 and int(hgt) <= 76)
    else:
        return 0    

def check_hcl(hcl):
    regex = '^#[0-9a-f]{6}$'
    x = re.search(regex, hcl)
    if(x):
        return 1
    else:
        return 0

ecl_list = ['amb','blu','brn','gry','grn', 'hzl','oth']
def check_ecl(ecl):
    return ecl in ecl_list

def check_pid(pid):
    regex = "^[0-9]{9}$"
    x = re.search(regex, pid)
    if(x):
        return 1
    else:
        return 0

def main():
    data = read_input('input')

    passport_list = parse_passports(data)
    print(check_valid(passport_list))

    print(check_valid_b(passport_list))


    
if __name__ == "__main__":
    main()