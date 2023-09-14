num = input("Enter a number: ")

index = 0 
exponent = len(num) - 1   
base = 10
result_value = 0

while exponent >= 0:
    result_value += int(num[index]) * (base ** exponent)
    index += 1
    exponent -= 1
print(num,type(num))
print(result_value,type(result_value))  
