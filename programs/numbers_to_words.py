### Not complete

def numtoword():
    #suffixes = ['hundred', 'thousand', 'million', 'billion']
    #ones = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    #teens = ['eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
    #tens = ['ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
    suffixes = ['hundred', 'thousand', 'million', 'billion']
    ones = {'1':'one', '2':'two', '3':'three', '4':'four', '5':'five', '6':'six', '7':'seven', '8':'eight', '9':'nine'}
    teens = {'11':'eleven', '12':'twelve', '13':'thirteen', '14':'fourteen', '15':'fifteen', '16':'sixteen', '17':'seventeen', '18':'eighteen', '19':'nineteen'}
    tens = {'1':'ten', '2':'twenty', '3':'thirty', '4':'forty', '5':'fifty', '6':'sixty', '7':'seventy', '8':'eighty', '9':'ninety'}

    yourNum = input("Input your number: ")
    numLength = len(yourNum)

    yourNum = list(yourNum)
    
    if numLength < 2: 
        word = under_ten(yourNum)
        return word
    
    if numLength < 3:
        word = under_hundred(yourNum, tens, teens)
        return word

def under_ten(yourNum):
    ones = {'1':'one', '2':'two', '3':'three', '4':'four', '5':'five', '6':'six', '7':'seven', '8':'eight', '9':'nine'}
    return ones[yourNum[0]]

def under_hundred(yourNum, tens, teens): 
    if yourNum[0] == '1' and yourNum[1] != 0:
        return teens["".join(yourNum)]
    else:
        word = [tens[yourNum[0]]]
        word2 = under_ten(yourNum[1])
        word.append(word2)

        return " ".join(word)

print(numtoword())
        

