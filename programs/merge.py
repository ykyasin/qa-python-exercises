def zipper(input1, input2):
    if len(input1) == len(input2):
        input1 = list(input1)
        input2 = list(input2)
        result = []
        for i in range(len(input1)*2):
            if i % 2 == 0:
                result.append(input1[0])
                input1.pop(0)
            elif i % 2 == 1:
                result.append(input2[0])
                input2.pop(0)
        return "".join(result)
    return "nothing"

def zipper2(input1,input2):
    if len(input1) == len(input2):
        return ''.join(''.join(x) for x in zip(input1,input2))

print(zipper2("Dog","Cat"))
    

