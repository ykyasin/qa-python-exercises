def sorter(input):
    input = input.split()
    input.sort()
    input = list(dict.fromkeys(input))
    return " ".join(input)

print(sorter("hello world and practice makes perfect and hello world again"))

