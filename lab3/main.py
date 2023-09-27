lookup_table1 = {
    '0':0,
    '1':1,
    '2':2,
    '3':3,
    '4':4,
    '5':5,
    '6':6,
    '7':7,
    '8':8,
    '9':9,
    'a':10,
    'b':11,
    'c':12,
    'd':13,
    'e':14,
    'f':15
}

lookup_table2 = {
    0:'0',
    1:'1',
    2:'2',
    3:'3',
    4:'4',
    5:'5',
    6:'6',
    7:'7',
    8:'8',
    9:'9',
    10:'a',
    11:'b',
    12:'c',
    13:'d',
    14:'e',
    15:'f'
}
def weighted_sum(num: str,base = 10):
    lookup_table = {
    '0': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    'a': 10,
    'b': 11,
    'c': 12,
    'd': 13,
    'e': 14,
    'f': 15
    }

    index = 0
    exponent = len(num) - 1
    result_value = 0

    while exponent >= 0:
        result_value += lookup_table[num[index]] * (int(base) ** exponent)
        index += 1
        exponent -= 1
    return result_value

def repeated_division(num,base):

    Q = weighted_sum(num)
    R = 0
    result = ''

    while Q != 0:
        R = Q % base
        Q = Q // base
        result = lookup_table2[R] + result
    return result

#print(weighted_sum('01100010',2))

print(repeated_division('11',2))
