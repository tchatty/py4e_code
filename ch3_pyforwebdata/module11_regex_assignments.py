import re
def sample():
    handle = open('regex_sum_2064913.txt')
    numlist = list()
    for line in handle:
        line = line.strip()
        stuff = re.findall('[0-9]+', line)
        for n in stuff:
            num = int(n)
            numlist.append(num)
    total_sum = sum(numlist)
    print(total_sum)
sample()