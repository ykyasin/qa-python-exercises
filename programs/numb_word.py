def num2word():
    yourNum = list(input("Input you number: "))
    ones = {'1':'one', '2':'two', '3':'three', '4':'four', '5':'five', '6':'six', '7':'seven', '8':'eight', '9':'nine'}
    teens = {'10':'ten', '11':'eleven', '12':'twelve', '13':'thirteen', '14':'fourteen', '15':'fifteen', '16':'sixteen', '17':'seventeen', '18':'eighteen', '19':'nineteen'}
    numLength = len(yourNum)
    if numLength == 1: 
        return ones[yourNum[0]]
    elif numLength == 2 and yourNum[0] == '1':
        return teens["".join(yourNum)]
    else: 
        return beyond(yourNum)

    
def beyond(yourNum):
    




print(num2word())





