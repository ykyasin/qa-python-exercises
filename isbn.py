isbn = input("Input the isbn number (no dashes or spaces): ")
# E.g. input: 978030640615
isbn = list(isbn)

check = 0
for i in range(len(isbn)):
    c = int(isbn[i])
    if i % 2 == 1: 
        x = c*3
        check = check + x
    elif i % 2 == 0: 
        check = check + c

check = 10 - (check%10) 

isbn.insert(3,"-")
isbn.insert(5,"-")
isbn.insert(9,"-")
isbn.insert(15,"-")
isbn = "".join(isbn)
print("For ISBN: " + isbn + "?")
print("check digit is --------->", str(check))
