def get_length(input_list):
    length = 0
    for i in input_list:
        length += 1
    return length

def get_sum(input_list):
    mysum = 0
    for i in input_list:
        mysum += i
    return mysum

def get_average(input_list):
    mysum = 0
    length = 0
    for i in input_list:
        mysum += i
        length += 1
    return mysum / length

def get_max(input_list):
    maxnum = float('-inf')
    for i in input_list:
        if i > maxnum: maxnum = i
    return maxnum

def get_min(input_list):
    minnum = float('inf')
    for i in input_list:
        if i < minnum: minnum = i
    return minnum