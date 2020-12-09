def alpha(input):
    input = input.replace(" ", "")
    lower_count = 0 
    upper_count = 0
    for i in input:
        if i.isupper(): 
            upper_count += 1
        elif i.lower(): 
            lower_count += 1
    
    return [upper_count, lower_count]

print(alpha('hello Mate'))


