num = input("Enter a number: ")
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
base = input("Enter a base: ")
result_value = 0

while exponent >= 0:
    result_value += lookup_table[num[index]] * (int(base) ** exponent)
    index += 1
    exponent -= 1
print(num,type(num))
print(result_value,type(result_value))
