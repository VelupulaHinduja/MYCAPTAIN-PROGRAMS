n = int(input("How many words u want to enter : "))
wordList = list()

for i in range (0,n):
	name = str(input("Enter the string :"))
	wordList.append(name)

count = -1
index = 0
max = len(wordList[0])
for string in wordList:
	count = count + 1
	if(max<len(string)):
		index = count
	
print(wordList[index])

