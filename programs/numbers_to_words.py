### Not complete

yourNum = input("Input your number: ")
numLength = len(yourNum)

def numtoword(yourNum, numLength):
    suffixes = ['hundred', 'thousand', 'million', 'billion']
    ones = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    teens = ['eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
    tens = ['ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']