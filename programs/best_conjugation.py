### Not complete

word_file = open("programs/wordlist.txt","r")

wordlist = []
for line in word_file:
  stripped_line = line.strip()
  line_list = stripped_line.split()
  wordlist.append(line_list)

word_file.close()

yourword = input("input your word: ")

def conjugation(yourword):
    checklist = []
    for i in wordlist:
        i = "".join(i)
        if i in yourword:
            checklist.append(i)
    return "Sub words that make up your word: " + ", ".join(checklist)

print(conjugation(yourword))

    

