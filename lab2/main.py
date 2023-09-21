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
def add_two_numbers(num1, num2, base):
    result = ""
    
    num2 = num2.zfill(len(num1))
    num1 = num1.zfill(len(num2))

    index = len(num1) - 1
    carry = 0
    while index >= 0:
        digit1 = lookup_table1[num1[index]]
        digit2 = lookup_table1[num2[index]]   
        
        sum_of_digits = digit1 + digit2 + carry 

        result = lookup_table2[sum_of_digits % base] + result
        if sum_of_digits >= base:
            
            carry = 1   
        else:
            carry = 0

        index -= 1
    if carry == 1:
        return lookup_table2[carry] + result
    else:
        return result
base = 16
num1 = "9"
num2 = "1"
print("call to add_two_numbers: ",add_two_numbers(num1, num2, base))
